import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import model

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def arquivo_permitido(filename):
    """Verifica se a extensão do arquivo é de uma imagem válida."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def texto_limpo(valor):
    """Remove espaços nas pontas e retorna None se sobrar só espaço/vazio."""
    if valor is None:
        return None
    valor = valor.strip()
    return valor or None

@app.template_filter('formatar_numero')
def formatar_numero(valor):
    try:
        return f"{int(valor):,}".replace(",", ".")
    except (ValueError, TypeError):
        return valor

@app.route("/buscar", methods=["GET"])
def buscar():
    termo = request.args.get("nome_musica", "").strip().lower()
    categoria = model.listar_categorias()

    if not termo:
        return render_template("listar_musicas.html", musica=model.listar_musicas(), categoria=categoria)

    categoria_encontrada = model.buscar_categoria_por_nome(termo)

    if categoria_encontrada:
        resultado = model.buscar_musicas_por_categoria(termo)
        mensagem = None if resultado else f"Nenhuma música encontrada na categoria '{categoria_encontrada['name']}'."
    else:
        resultado = model.buscar_musicas(termo)
        mensagem = None if resultado else "Nenhuma música encontrada para sua busca."

    return render_template("listar_musicas.html", musica=resultado, categoria=categoria, mensagem=mensagem)


@app.route("/")
def nome_musica():
    return render_template("home.html", musica=model.listar_musicas(), categoria=model.listar_categorias())


@app.route("/listar")
def listar():
    return render_template("listar_musicas.html", musica=model.listar_musicas(), categoria=model.listar_categorias())


@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = texto_limpo(request.form.get("nome_musica")).strip()
    artista = texto_limpo(request.form.get("nome_artista")).strip()

    capa_da_musica = request.files.get("imagem")
    nome_capa = None

    if capa_da_musica and capa_da_musica.filename != '':
        if arquivo_permitido(capa_da_musica.filename):
            nome_capa = secure_filename(capa_da_musica.filename)
            capa_da_musica.save(os.path.join(app.config['UPLOAD_FOLDER'], nome_capa))

    if titulo and artista:
        model.adicionar_musica(
            titulo=titulo,
            artista=artista,
            streams=request.form.get("streams"),
            nome_categoria=texto_limpo(request.form.get("categoria")),
            capa=nome_capa
        )
    return render_template("listar_musicas.html", musica=model.listar_musicas(), categoria=model.listar_categorias())


@app.route("/deletar/<int:id>")
def deletar(id):
    model.deletar_musica(id)
    return render_template("listar_musicas.html", musica=model.listar_musicas(), categoria=model.listar_categorias())


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    if request.method == "POST":
        titulo = texto_limpo(request.form.get("nome_musica")).strip()
        artista = texto_limpo(request.form.get("nome_artista")).strip()
        capa_da_musica = request.files.get("imagem")

        if titulo and artista:
            model.editar_musica(
                id_musica=id,
                titulo=titulo,
                artista=artista,
                streams=request.form.get("streams"),
                nome_categoria=texto_limpo(request.form.get("categoria")),
                capa_da_musica=capa_da_musica.read() if capa_da_musica else None
            )
        return render_template("listar_musicas.html", musica=model.listar_musicas(), categoria=model.listar_categorias())
    else:
        m = model.obter_musica(id)
        return render_template("editar.html", musica=m, id=id, categoria=model.listar_categorias())


@app.route("/gerenciar")
def gerenciar_categorias():
    return render_template("listar_categorias.html", musica=model.listar_musicas(), categoria=model.listar_categorias())


@app.route("/adicionar_categoria", methods=["POST"])
def adicionar_categoria():
    nome = texto_limpo(request.form.get("nome_categoria")).strip()
    if nome:
        model.adicionar_categoria(nome)
    return render_template("listar_categorias.html", musica=model.listar_musicas(), categoria=model.listar_categorias())


@app.route("/deletar_categoria/<nome_categoria>")
def deletar_categoria(nome_categoria):
    model.deletar_categoria(nome_categoria)
    return redirect(url_for("gerenciar_categorias"))


if __name__ == "__main__":
    app.run(debug=True)
