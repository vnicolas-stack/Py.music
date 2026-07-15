--
-- PostgreSQL database dump
--


-- Dumped from database version 17.10
-- Dumped by pg_dump version 17.10

-- Started on 2026-07-13 20:04:30

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
-- TOC entry 220 (class 1259 OID 24589)
-- Name: categorias; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categorias (
    id integer NOT NULL,
    titulo character varying(300) NOT NULL
);


ALTER TABLE public.categorias OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 24588)
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
-- TOC entry 5030 (class 0 OID 0)
-- Dependencies: 219
-- Name: categorias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categorias_id_seq OWNED BY public.categorias.id;


--
-- TOC entry 222 (class 1259 OID 24598)
-- Name: musicas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.musicas (
    id integer CONSTRAINT musica_id_not_null NOT NULL,
    titulo character varying(150) CONSTRAINT musica_titulo_not_null NOT NULL,
    artista character varying(100) CONSTRAINT musica_artista_not_null NOT NULL,
    streams bigint DEFAULT 0,
    id_categoria integer
);


ALTER TABLE public.musicas OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 24597)
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
-- TOC entry 5031 (class 0 OID 0)
-- Dependencies: 221
-- Name: musica_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.musica_id_seq OWNED BY public.musicas.id;


--
-- TOC entry 4861 (class 2604 OID 24592)
-- Name: categorias id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categorias ALTER COLUMN id SET DEFAULT nextval('public.categorias_id_seq'::regclass);


--
-- TOC entry 4862 (class 2604 OID 24601)
-- Name: musicas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musicas ALTER COLUMN id SET DEFAULT nextval('public.musica_id_seq'::regclass);


--
-- TOC entry 5022 (class 0 OID 24589)
-- Dependencies: 220
-- Data for Name: categorias; Type: TABLE DATA; Schema: public; Owner: postgres
--

-- Dados convertidos de COPY para INSERT (public.categorias)
INSERT INTO public.categorias (id, titulo) VALUES ('3', 'Indie Rock');
INSERT INTO public.categorias (id, titulo) VALUES ('4', 'Indie Pop');
INSERT INTO public.categorias (id, titulo) VALUES ('5', 'Trilha Sonora de Jogos');


--
-- TOC entry 5024 (class 0 OID 24598)
-- Dependencies: 222
-- Data for Name: musicas; Type: TABLE DATA; Schema: public; Owner: postgres
--

-- Dados convertidos de COPY para INSERT (public.musicas)
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('6', 'Sweater Weather', 'The Neighbourhood', '1850000000', '3');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('7', 'Daddy Issues', 'The Neighbourhood', '620000000', '3');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('8', 'Softcore', 'The Neighbourhood', '180000000', '3');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('9', 'Afraid', 'The Neighbourhood', '210000000', '3');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('10', 'Cry Baby', 'The Neighbourhood', '150000000', '3');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('11', 'Reflections', 'The Neighbourhood', '135000000', '3');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('12', 'Prey', 'The Neighbourhood', '95000000', '3');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('13', 'Void', 'The Neighbourhood', '88000000', '3');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('14', 'Lovers Rock', 'TV Girl', '980000000', '4');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('15', 'Cigarettes Out the Window', 'TV Girl', '210000000', '4');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('16', 'Painting Flowers', 'TV Girl', '175000000', '4');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('17', 'Not Allowed', 'TV Girl', '95000000', '4');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('18', 'Come On Now', 'TV Girl', '60000000', '4');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('19', 'Blue Hair', 'TV Girl', '45000000', '4');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('20', 'Megalovania', 'Toby Fox', '210000000', '5');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('21', 'Still Alive', 'Jonathan Coulton', '45000000', '5');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('22', 'Baba Yetu', 'Christopher Tin', '38000000', '5');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('23', 'Dearly Beloved', 'Yoko Shimomura', '22000000', '5');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('24', 'Main Theme (Zelda)', 'Koji Kondo', '30000000', '5');
INSERT INTO public.musicas (id, titulo, artista, streams, id_categoria) VALUES ('25', 'One-Winged Angel', 'Nobuo Uematsu', '18000000', '5');


--
-- TOC entry 5032 (class 0 OID 0)
-- Dependencies: 219
-- Name: categorias_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categorias_id_seq', 5, true);


--
-- TOC entry 5033 (class 0 OID 0)
-- Dependencies: 221
-- Name: musica_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.musica_id_seq', 25, true);


--
-- TOC entry 4865 (class 2606 OID 24596)
-- Name: categorias categorias_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT categorias_pkey PRIMARY KEY (id);


--
-- TOC entry 4867 (class 2606 OID 24632)
-- Name: categorias categorias_titulo_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT categorias_titulo_key UNIQUE (titulo);


--
-- TOC entry 4871 (class 2606 OID 24607)
-- Name: musicas musica_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musicas
    ADD CONSTRAINT musica_pkey PRIMARY KEY (id);


--
-- TOC entry 4868 (class 1259 OID 24614)
-- Name: idx_musica_artista; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_musica_artista ON public.musicas USING btree (lower((artista)::text));


--
-- TOC entry 4869 (class 1259 OID 24613)
-- Name: idx_musica_titulo; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_musica_titulo ON public.musicas USING btree (lower((titulo)::text));


--
-- TOC entry 4872 (class 2606 OID 24608)
-- Name: musicas musica_id_categoria_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musicas
    ADD CONSTRAINT musica_id_categoria_fkey FOREIGN KEY (id_categoria) REFERENCES public.categorias(id);


--
-- TOC entry 4873 (class 2606 OID 24633)
-- Name: musicas musicas_id_categoria_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.musicas
    ADD CONSTRAINT musicas_id_categoria_fkey FOREIGN KEY (id_categoria) REFERENCES public.categorias(id) ON DELETE SET NULL;


-- Completed on 2026-07-13 20:04:30

--
-- PostgreSQL database dump complete
--


