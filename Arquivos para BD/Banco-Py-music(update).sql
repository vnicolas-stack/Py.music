--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

-- Started on 2026-07-15 10:50:12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 217 (class 1259 OID 24614)
-- Name: categorias; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categorias (
    id integer NOT NULL,
    titulo character varying(300) NOT NULL
);


ALTER TABLE public.categorias OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 24617)
-- Name: categorias_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categorias_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.categorias_id_seq OWNER TO postgres;

--
-- TOC entry 4914 (class 0 OID 0)
-- Dependencies: 218
-- Name: categorias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categorias_id_seq OWNED BY public.categorias.id;


--
-- TOC entry 219 (class 1259 OID 24618)
-- Name: musicas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.musicas (
    id integer NOT NULL,
    titulo character varying(150) NOT NULL,
    artista character varying(100) NOT NULL,
    streams bigint DEFAULT 0,
    id_categoria integer,
    capa character varying(400)
);


ALTER TABLE public.musicas OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 24622)
-- Name: musica_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.musica_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.musica_id_seq OWNER TO postgres;

--
-- TOC entry 4915 (class 0 OID 0)
-- Dependencies: 220
-- Name: musica_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.musica_id_seq OWNED BY public.musicas.id;


--
-- TOC entry 4747 (class 2604 OID 24623)
-- Name: categorias id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categorias ALTER COLUMN id SET DEFAULT nextval('public.categorias_id_seq'::regclass);


--
-- TOC entry 4748 (class 2604 OID 24624)
-- Name: musicas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musicas ALTER COLUMN id SET DEFAULT nextval('public.musica_id_seq'::regclass);


--
-- TOC entry 4905 (class 0 OID 24614)
-- Dependencies: 217
-- Data for Name: categorias; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categorias (id, titulo) FROM stdin;
3	Indie Rock
4	Indie Pop
5	Trilha Sonora de Jogos
\.


--
-- TOC entry 4907 (class 0 OID 24618)
-- Dependencies: 219
-- Data for Name: musicas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.musicas (id, titulo, artista, streams, id_categoria, capa) FROM stdin;
6	Sweater Weather	The Neighbourhood	1850000000	3	\N
7	Daddy Issues	The Neighbourhood	620000000	3	\N
8	Softcore	The Neighbourhood	180000000	3	\N
9	Afraid	The Neighbourhood	210000000	3	\N
10	Cry Baby	The Neighbourhood	150000000	3	\N
11	Reflections	The Neighbourhood	135000000	3	\N
12	Prey	The Neighbourhood	95000000	3	\N
13	Void	The Neighbourhood	88000000	3	\N
14	Lovers Rock	TV Girl	980000000	4	\N
15	Cigarettes Out the Window	TV Girl	210000000	4	\N
16	Painting Flowers	TV Girl	175000000	4	\N
17	Not Allowed	TV Girl	95000000	4	\N
18	Come On Now	TV Girl	60000000	4	\N
19	Blue Hair	TV Girl	45000000	4	\N
20	Megalovania	Toby Fox	210000000	5	\N
21	Still Alive	Jonathan Coulton	45000000	5	\N
22	Baba Yetu	Christopher Tin	38000000	5	\N
23	Dearly Beloved	Yoko Shimomura	22000000	5	\N
24	Main Theme (Zelda)	Koji Kondo	30000000	5	\N
25	One-Winged Angel	Nobuo Uematsu	18000000	5	\N
\.


--
-- TOC entry 4916 (class 0 OID 0)
-- Dependencies: 218
-- Name: categorias_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categorias_id_seq', 5, true);


--
-- TOC entry 4917 (class 0 OID 0)
-- Dependencies: 220
-- Name: musica_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.musica_id_seq', 26, true);


--
-- TOC entry 4751 (class 2606 OID 24626)
-- Name: categorias categorias_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT categorias_pkey PRIMARY KEY (id);


--
-- TOC entry 4753 (class 2606 OID 24628)
-- Name: categorias categorias_titulo_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT categorias_titulo_key UNIQUE (titulo);


--
-- TOC entry 4757 (class 2606 OID 24630)
-- Name: musicas musica_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musicas
    ADD CONSTRAINT musica_pkey PRIMARY KEY (id);


--
-- TOC entry 4754 (class 1259 OID 24631)
-- Name: idx_musica_artista; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_musica_artista ON public.musicas USING btree (lower((artista)::text));


--
-- TOC entry 4755 (class 1259 OID 24632)
-- Name: idx_musica_titulo; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_musica_titulo ON public.musicas USING btree (lower((titulo)::text));


--
-- TOC entry 4758 (class 2606 OID 24633)
-- Name: musicas musica_id_categoria_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musicas
    ADD CONSTRAINT musica_id_categoria_fkey FOREIGN KEY (id_categoria) REFERENCES public.categorias(id);


--
-- TOC entry 4759 (class 2606 OID 24638)
-- Name: musicas musicas_id_categoria_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musicas
    ADD CONSTRAINT musicas_id_categoria_fkey FOREIGN KEY (id_categoria) REFERENCES public.categorias(id) ON DELETE SET NULL;


-- Completed on 2026-07-15 10:50:13

--
-- PostgreSQL database dump complete
--

