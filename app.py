from flask import Flask, render_template, request, redirect, url_for
import psycopg2 
from psycopg2.extras import RealDictCursor
import uuid
import json
import os

app = Flask(__name__)
def conectar():
    return psycopg2.connect(
        host = "localhost",
        database = "Py.music",
        user = "postgres",
        password = "postgres"
        )

@app.template_filter('formatar_numero')
def formatar_numero(valor):
    try:
        return f"{int(valor):,}".replace(",", ".")
    except (ValueError, TypeError):
        return valor

ARQUIVO_MUSICA = "database/musica.json"
ARQUIVO_CATEGORIA = "database/categoria.json"

def carregar_json(arquivo):
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_json(arquivo, dados):
    os.makedirs(os.path.dirname(arquivo), exist_ok=True)
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

musica = carregar_json(ARQUIVO_MUSICA)
categoria = carregar_json(ARQUIVO_CATEGORIA)

def gerar_id():
    return str(uuid.uuid4())

def buscar_musica_por_nome(nome):
    for m in musica:
        if isinstance(m, dict) and m.get("title", "").lower() == nome.lower():
            return m
    return None

@app.route("/buscar", methods=["GET"])
def buscar():
    termo = request.args.get("nome_musica", "").strip().lower()
    if not termo:
        return render_template("listar_musicas.html", musica=musica, categoria=categoria)
 
    categoria_encontrada = next((c for c in categoria if c.get("name", "").lower() == termo), None)
 
    if categoria_encontrada:
        resultado = [m for m in musica if m.get("categoria", "").lower() == termo]
        mensagem = None if resultado else f"Nenhuma música encontrada na categoria '{categoria_encontrada['name']}'."
    else:
        resultado = [m for m in musica if termo in m.get("title", "").lower() or termo in m.get("artista", "").lower()]
        mensagem = None if resultado else "Nenhuma música encontrada para sua busca."
 
    return render_template("listar_musicas.html", musica=resultado, categoria=categoria, mensagem=mensagem)

@app.route("/")
def nome_musica():
    return render_template("home.html", musica=musica, categoria=categoria)

@app.route("/listar")
def listar():
    return render_template("listar_musicas.html", musica=musica, categoria=categoria)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    nova_musica = {
        "id": gerar_id(),
        "title": request.form.get("nome_musica"),
        "artista": request.form.get("nome_artista"),
        "streams": request.form.get("streams"),
        "categoria": request.form.get("categoria")
    }
    musica.append(nova_musica)
    salvar_json(ARQUIVO_MUSICA, musica)
    return render_template("listar_musicas.html", musica=musica, categoria=categoria)

@app.route("/deletar/<int:id>")
def deletar(id):
    if 0 <= id < len(musica):
        del musica[id]
        salvar_json(ARQUIVO_MUSICA, musica)
    return render_template("listar_musicas.html", musica=musica, categoria=categoria)

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    if request.method == "POST":
        if 0 <= id < len(musica):
            musica[id]["title"] = request.form.get("nome_musica")
            musica[id]["artista"] = request.form.get("nome_artista")
            musica[id]["streams"] = request.form.get("streams")
            musica[id]["categoria"] = request.form.get("categoria")
            salvar_json(ARQUIVO_MUSICA, musica)
        return render_template("listar_musicas.html", musica=musica, categoria=categoria)
    else:
        m = musica[id] if 0 <= id < len(musica) else None
        return render_template("editar.html", musica=m, id=id, categoria=categoria)

@app.route("/gerenciar")
def gerenciar_categorias():
    return render_template("listar_categorias.html", musica=musica, categoria=categoria)

@app.route("/adicionar_categoria", methods=["POST"])
def adicionar_categoria():
    nova_categoria = {
        "name": request.form.get("nome_categoria")
    }
    categoria.append(nova_categoria)
    salvar_json(ARQUIVO_CATEGORIA, categoria)
    return render_template("listar_categorias.html", musica=musica, categoria=categoria)

@app.route("/deletar_categoria/<nome_categoria>") 
def deletar_categoria(nome_categoria):
    global categoria, musica

    categoria = [c for c in categoria if c.get("name") != nome_categoria]
    salvar_json(ARQUIVO_CATEGORIA, categoria)

    for m in musica:
        if m.get("categoria") == nome_categoria:
            m["categoria"] = ""

    salvar_json(ARQUIVO_MUSICA, musica)

    return redirect(url_for("gerenciar_categorias"))

if __name__ == "__main__":
    app.run(debug=True)
