from flask import Flask, render_template, request, redirect, url_for
import model

app = Flask(__name__)


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

    if titulo and artista:
        model.adicionar_musica(
            titulo=titulo,
            artista=artista,
            streams=request.form.get("streams"),
            nome_categoria=texto_limpo(request.form.get("categoria")),
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

        if titulo and artista:
            model.editar_musica(
                id_musica=id,
                titulo=titulo,
                artista=artista,
                streams=request.form.get("streams"),
                nome_categoria=texto_limpo(request.form.get("categoria")),
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
