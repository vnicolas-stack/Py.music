import psycopg2
from psycopg2.extras import RealDictCursor

HOST = "127.0.0.1"
PORT = "5432"
DB_NAME = "Py.music"
USER = "postgres"
PASSWORD = "postgres"


def get_conn():
    """Abre uma conexão nova com o banco. Use sempre dentro de um 'with'."""
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        cursor_factory=RealDictCursor,
        options="-c lc_messages=C",
    )
    conn.set_client_encoding('UTF8')
    return conn


#                    CATEGORIAS 

def listar_categorias():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, titulo AS name FROM public.categorias ORDER BY titulo")
        return cur.fetchall()


def adicionar_categoria(nome):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO public.categorias (titulo) VALUES (%s) ON CONFLICT (titulo) DO NOTHING",
            (nome,),
        )
        conn.commit()


def deletar_categoria(nome):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM public.categorias WHERE titulo = %s", (nome,))
        conn.commit()


def _id_categoria_por_nome(cur, nome_categoria):
    if not nome_categoria:
        return None
    cur.execute("SELECT id FROM public.categorias WHERE titulo = %s", (nome_categoria,))
    row = cur.fetchone()
    return row["id"] if row else None


#                    MÚSICAS 

_SELECT_MUSICA = """
    SELECT m.id, m.titulo AS title, m.artista, m.streams,
           COALESCE(c.titulo, '') AS categoria
    FROM public.musicas m
    LEFT JOIN public.categorias c ON c.id = m.id_categoria
"""


def listar_musicas():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(_SELECT_MUSICA + " ORDER BY m.id")
        return cur.fetchall()


def buscar_musicas(termo):
    """Busca por título ou artista (case-insensitive)."""
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            _SELECT_MUSICA + """
            WHERE LOWER(m.titulo) LIKE %s OR LOWER(m.artista) LIKE %s
            ORDER BY m.id
            """,
            (f"%{termo}%", f"%{termo}%"),
        )
        return cur.fetchall()


def buscar_musicas_por_categoria(nome_categoria):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            _SELECT_MUSICA + " WHERE LOWER(c.titulo) = %s ORDER BY m.id",
            (nome_categoria.lower(),),
        )
        return cur.fetchall()


def buscar_categoria_por_nome(nome_categoria):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            "SELECT id, titulo AS name FROM public.categorias WHERE LOWER(titulo) = %s",
            (nome_categoria.lower(),),
        )
        return cur.fetchone()


def obter_musica(id_musica):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(_SELECT_MUSICA + " WHERE m.id = %s", (id_musica,))
        return cur.fetchone()


def adicionar_musica(titulo, artista, streams, nome_categoria):
    with get_conn() as conn, conn.cursor() as cur:
        id_categoria = _id_categoria_por_nome(cur, nome_categoria)
        cur.execute(
            """
            INSERT INTO public.musicas (titulo, artista, streams, id_categoria)
            VALUES (%s, %s, %s, %s)
            """,
            (titulo, artista, streams or 0, id_categoria),
        )
        conn.commit()


def editar_musica(id_musica, titulo, artista, streams, nome_categoria):
    with get_conn() as conn, conn.cursor() as cur:
        id_categoria = _id_categoria_por_nome(cur, nome_categoria)
        cur.execute(
            """
            UPDATE public.musicas
            SET titulo = %s, artista = %s, streams = %s, id_categoria = %s
            WHERE id = %s
            """,
            (titulo, artista, streams or 0, id_categoria, id_musica),
        )
        conn.commit()


def deletar_musica(id_musica):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM musica WHERE id = %s", (id_musica,))
        conn.commit()
