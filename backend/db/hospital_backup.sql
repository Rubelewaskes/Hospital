--
-- PostgreSQL database dump
--

-- Dumped from database version 16rc1
-- Dumped by pg_dump version 16rc1

-- Started on 2024-12-10 15:30:21

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 5 (class 2615 OID 19754)
-- Name: hospital; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA hospital;


ALTER SCHEMA hospital OWNER TO postgres;

--
-- TOC entry 6 (class 2615 OID 19938)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 4904 (class 0 OID 0)
-- Dependencies: 6
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS '';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 226 (class 1259 OID 19785)
-- Name: address_area; Type: TABLE; Schema: hospital; Owner: postgres
--

CREATE TABLE hospital.address_area (
    id integer NOT NULL,
    street character varying(100) NOT NULL,
    house character varying(10) NOT NULL,
    building character varying(15),
    flat integer,
    area_id integer NOT NULL
);


ALTER TABLE hospital.address_area OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 19784)
-- Name: address_area_address_id_seq; Type: SEQUENCE; Schema: hospital; Owner: postgres
--

ALTER TABLE hospital.address_area ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hospital.address_area_address_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 224 (class 1259 OID 19779)
-- Name: area; Type: TABLE; Schema: hospital; Owner: postgres
--

CREATE TABLE hospital.area (
    id integer NOT NULL
);


ALTER TABLE hospital.area OWNER TO postgres;

--
-- TOC entry 236 (class 1259 OID 19863)
-- Name: area_doctor; Type: TABLE; Schema: hospital; Owner: postgres
--

CREATE TABLE hospital.area_doctor (
    id integer NOT NULL,
    doctor_id integer NOT NULL,
    area_id integer NOT NULL
);


ALTER TABLE hospital.area_doctor OWNER TO postgres;

--
-- TOC entry 235 (class 1259 OID 19862)
-- Name: area_doctor_area_doctor_id_seq; Type: SEQUENCE; Schema: hospital; Owner: postgres
--

ALTER TABLE hospital.area_doctor ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hospital.area_doctor_area_doctor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 232 (class 1259 OID 19818)
-- Name: check_up; Type: TABLE; Schema: hospital; Owner: postgres
--

CREATE TABLE hospital.check_up (
    id integer NOT NULL,
    check_up_place_id integer NOT NULL,
    check_up_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    doctor_id integer NOT NULL,
    patient_id integer NOT NULL,
    diagnosis_id integer,
    prescription character varying(700) NOT NULL
);


ALTER TABLE hospital.check_up OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 19817)
-- Name: check_up_check_up_id_seq; Type: SEQUENCE; Schema: hospital; Owner: postgres
--

ALTER TABLE hospital.check_up ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hospital.check_up_check_up_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 219 (class 1259 OID 19762)
-- Name: check_up_place; Type: TABLE; Schema: hospital; Owner: postgres
--

CREATE TABLE hospital.check_up_place (
    id integer NOT NULL,
    place character varying(11) NOT NULL
);


ALTER TABLE hospital.check_up_place OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 19761)
-- Name: check_up_place_check_up_place_id_seq; Type: SEQUENCE; Schema: hospital; Owner: postgres
--

ALTER TABLE hospital.check_up_place ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hospital.check_up_place_check_up_place_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 223 (class 1259 OID 19774)
-- Name: diagnosis; Type: TABLE; Schema: hospital; Owner: postgres
--

CREATE TABLE hospital.diagnosis (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE hospital.diagnosis OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 19773)
-- Name: diagnosis_diagnosis_id_seq; Type: SEQUENCE; Schema: hospital; Owner: postgres
--

ALTER TABLE hospital.diagnosis ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hospital.diagnosis_diagnosis_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 230 (class 1259 OID 19812)
-- Name: doctor; Type: TABLE; Schema: hospital; Owner: postgres
--

CREATE TABLE hospital.doctor (
    id integer NOT NULL,
    first_name character varying(100) NOT NULL,
    second_name character varying(100) NOT NULL,
    third_name character varying(100),
    phone_number character(12) NOT NULL,
    experience integer NOT NULL,
    user_id uuid
);


ALTER TABLE hospital.doctor OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 19811)
-- Name: doctor_doctor_id_seq; Type: SEQUENCE; Schema: hospital; Owner: postgres
--

ALTER TABLE hospital.doctor ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hospital.doctor_doctor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 217 (class 1259 OID 19756)
-- Name: gender; Type: TABLE; Schema: hospital; Owner: postgres
--

CREATE TABLE hospital.gender (
    id integer NOT NULL,
    description character(7) NOT NULL
);


ALTER TABLE hospital.gender OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 19755)
-- Name: gender_gender_id_seq; Type: SEQUENCE; Schema: hospital; Owner: postgres
--

ALTER TABLE hospital.gender ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hospital.gender_gender_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 228 (class 1259 OID 19796)
-- Name: patient; Type: TABLE; Schema: hospital; Owner: postgres
--

CREATE TABLE hospital.patient (
    id integer NOT NULL,
    first_name character varying(100) NOT NULL,
    second_name character varying(100) NOT NULL,
    third_name character varying(100),
    phone_number character(12) NOT NULL,
    address_id integer NOT NULL,
    gender_id integer NOT NULL,
    born_date date,
    user_id uuid
);


ALTER TABLE hospital.patient OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 19795)
-- Name: patient_patient_id_seq; Type: SEQUENCE; Schema: hospital; Owner: postgres
--

ALTER TABLE hospital.patient ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hospital.patient_patient_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 221 (class 1259 OID 19768)
-- Name: symptom; Type: TABLE; Schema: hospital; Owner: postgres
--

CREATE TABLE hospital.symptom (
    id integer NOT NULL,
    name character varying(400) NOT NULL
);


ALTER TABLE hospital.symptom OWNER TO postgres;

--
-- TOC entry 234 (class 1259 OID 19847)
-- Name: symptom_check_up; Type: TABLE; Schema: hospital; Owner: postgres
--

CREATE TABLE hospital.symptom_check_up (
    id integer NOT NULL,
    check_up_id integer NOT NULL,
    symptom_id integer,
    description character varying(200)
);


ALTER TABLE hospital.symptom_check_up OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 19846)
-- Name: symptom_check_up_symptom_check_up_id_seq; Type: SEQUENCE; Schema: hospital; Owner: postgres
--

ALTER TABLE hospital.symptom_check_up ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hospital.symptom_check_up_symptom_check_up_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 220 (class 1259 OID 19767)
-- Name: symptom_symptom_id_seq; Type: SEQUENCE; Schema: hospital; Owner: postgres
--

ALTER TABLE hospital.symptom ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hospital.symptom_symptom_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 238 (class 1259 OID 19947)
-- Name: accesstoken; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.accesstoken (
    user_id uuid NOT NULL,
    token character varying(43) NOT NULL,
    created_at timestamp with time zone NOT NULL
);


ALTER TABLE public.accesstoken OWNER TO postgres;

--
-- TOC entry 237 (class 1259 OID 19939)
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    is_doctor boolean,
    id uuid NOT NULL,
    email character varying(320) NOT NULL,
    hashed_password character varying(1024) NOT NULL,
    is_active boolean NOT NULL,
    is_superuser boolean NOT NULL,
    is_verified boolean NOT NULL
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- TOC entry 4886 (class 0 OID 19785)
-- Dependencies: 226
-- Data for Name: address_area; Type: TABLE DATA; Schema: hospital; Owner: postgres
--

COPY hospital.address_area (id, street, house, building, flat, area_id) FROM stdin;
1	ул. 8 Марта	14	\N	1	1
2	ул. 8 Марта	11	корпус 3	1	2
3	ул. 8 Марта	11	корпус 3	2	2
4	ул. Бахвалова	22	\N	\N	3
5	ул. Бахвалова	1/28	\N	\N	3
\.


--
-- TOC entry 4884 (class 0 OID 19779)
-- Dependencies: 224
-- Data for Name: area; Type: TABLE DATA; Schema: hospital; Owner: postgres
--

COPY hospital.area (id) FROM stdin;
1
2
3
\.


--
-- TOC entry 4896 (class 0 OID 19863)
-- Dependencies: 236
-- Data for Name: area_doctor; Type: TABLE DATA; Schema: hospital; Owner: postgres
--

COPY hospital.area_doctor (id, doctor_id, area_id) FROM stdin;
1	1	1
2	1	2
3	2	3
\.


--
-- TOC entry 4892 (class 0 OID 19818)
-- Dependencies: 232
-- Data for Name: check_up; Type: TABLE DATA; Schema: hospital; Owner: postgres
--

COPY hospital.check_up (id, check_up_place_id, check_up_date, doctor_id, patient_id, diagnosis_id, prescription) FROM stdin;
1	1	2024-06-10 14:30:00	1	1	1	
2	1	2024-11-10 14:55:00	1	2	1	
3	1	2024-11-15 15:30:00	1	3	\N	Пациент отправлен на прохождение дальнейшего обследования.
4	1	2024-11-16 15:30:00	1	3	2	
5	1	2024-11-21 14:30:00	2	4	2	
6	2	2024-11-25 17:30:00	2	5	2	
7	2	2024-11-26 17:00:00	1	1	1	
\.


--
-- TOC entry 4879 (class 0 OID 19762)
-- Dependencies: 219
-- Data for Name: check_up_place; Type: TABLE DATA; Schema: hospital; Owner: postgres
--

COPY hospital.check_up_place (id, place) FROM stdin;
1	Поликлиника
2	На дому
\.


--
-- TOC entry 4883 (class 0 OID 19774)
-- Dependencies: 223
-- Data for Name: diagnosis; Type: TABLE DATA; Schema: hospital; Owner: postgres
--

COPY hospital.diagnosis (id, name) FROM stdin;
1	ОРВИ
2	Ангина
\.


--
-- TOC entry 4890 (class 0 OID 19812)
-- Dependencies: 230
-- Data for Name: doctor; Type: TABLE DATA; Schema: hospital; Owner: postgres
--

COPY hospital.doctor (id, first_name, second_name, third_name, phone_number, experience, user_id) FROM stdin;
2	Марк	Ильин	Петрович	+79999999912	15	04876166-8c1b-4477-b752-be9eecbcecf8
1	Дана	Князева	Тимофеевна	+79999999911	5	e58350cf-2e95-4750-b1c2-395de3768c04
\.


--
-- TOC entry 4877 (class 0 OID 19756)
-- Dependencies: 217
-- Data for Name: gender; Type: TABLE DATA; Schema: hospital; Owner: postgres
--

COPY hospital.gender (id, description) FROM stdin;
1	Мужской
2	Женский
\.


--
-- TOC entry 4888 (class 0 OID 19796)
-- Dependencies: 228
-- Data for Name: patient; Type: TABLE DATA; Schema: hospital; Owner: postgres
--

COPY hospital.patient (id, first_name, second_name, third_name, phone_number, address_id, gender_id, born_date, user_id) FROM stdin;
2	Вероника	Королёва	Павловна	+79999999992	2	2	1994-11-26	2ab132c3-7327-418b-b674-5b3303b4afa4
3	Вячеслав	Беляев	Маркович	+79999999993	3	1	1984-11-26	d97056db-1fc1-41eb-a832-91e67d5601e0
4	Андрей	Соловьев	Романович	+79999999994	4	1	1974-11-26	5e5bc9c4-23a7-4bba-a0da-7fb9626488cc
5	Ульяна	Лебедева	Платоновна	+79999999995	5	2	1964-11-26	d8950454-5d26-44fe-8672-478fd2d63efe
1	Евангелина	Федорова	Александровна	+79999999991	1	2	2004-10-26	4141eac9-f104-458c-abd8-ac114e25cf0b
\.


--
-- TOC entry 4881 (class 0 OID 19768)
-- Dependencies: 221
-- Data for Name: symptom; Type: TABLE DATA; Schema: hospital; Owner: postgres
--

COPY hospital.symptom (id, name) FROM stdin;
1	Головная боль
2	Насморк
3	Кашель
4	Повышенная температура
5	Воспаление гланд
\.


--
-- TOC entry 4894 (class 0 OID 19847)
-- Dependencies: 234
-- Data for Name: symptom_check_up; Type: TABLE DATA; Schema: hospital; Owner: postgres
--

COPY hospital.symptom_check_up (id, check_up_id, symptom_id, description) FROM stdin;
1	1	1	\N
2	2	1	\N
3	2	2	\N
4	3	1	\N
5	4	1	\N
6	4	2	\N
7	5	2	\N
8	6	1	\N
9	7	1	\N
10	7	2	\N
11	1	3	\N
12	2	3	\N
13	3	3	\N
14	4	3	\N
15	5	3	\N
16	6	3	\N
17	7	3	\N
18	1	4	\N
19	2	4	\N
20	3	4	\N
21	4	4	\N
22	5	4	\N
23	6	4	\N
24	7	4	\N
25	4	5	\N
26	5	5	\N
27	6	5	\N
\.


--
-- TOC entry 4898 (class 0 OID 19947)
-- Dependencies: 238
-- Data for Name: accesstoken; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.accesstoken (user_id, token, created_at) FROM stdin;
2be29343-d5c6-40fc-aae2-91af1c60d792	F9xSkaVxhjqQm1K6zSlstrcXHkzvEelYYQb_ox2d6Zg	2024-12-10 14:51:10.090525+03
2be29343-d5c6-40fc-aae2-91af1c60d792	hAGbsGgLmnV7nkBSr97KWfzcLT3RCIKu-NTR7eQhP-Q	2024-12-10 15:21:30.971506+03
\.


--
-- TOC entry 4897 (class 0 OID 19939)
-- Dependencies: 237
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."user" (is_doctor, id, email, hashed_password, is_active, is_superuser, is_verified) FROM stdin;
t	04876166-8c1b-4477-b752-be9eecbcecf8	iliyn@example.com	$argon2id$v=19$m=65536,t=3,p=4$owA//Gn+qnzD1KszM8/qFQ$MaZBFa5+Nw4igdCrPo0HixeKXyuWfl/Tl+EOIkHEQfc	t	f	f
f	2ab132c3-7327-418b-b674-5b3303b4afa4	koroleva@example.com	$argon2id$v=19$m=65536,t=3,p=4$IBZS0P2Rc60v+J/WadEulw$MxbvU2W2NyFJFZ6Y8YT03nR80B3lc0hSHjpOi4vSXxE	t	f	f
f	2be29343-d5c6-40fc-aae2-91af1c60d792	admin@example.com	$argon2id$v=19$m=65536,t=3,p=4$rKEZrkeU2ekZ01pxBEKitg$h5hXspLNCkmCv2Q8rTrhbI6yJFsdr7+nSaaORqfIL5g	t	t	f
f	5e5bc9c4-23a7-4bba-a0da-7fb9626488cc	solovyov@example.com	$argon2id$v=19$m=65536,t=3,p=4$rF8UI1Hkwz5/CMkbfT6tDA$5fSfu37sX1QMNjMqZlhROMcb7zAZc2tAj7jYEwC+e9w	t	f	f
f	d8950454-5d26-44fe-8672-478fd2d63efe	lebedeva@example.com	$argon2id$v=19$m=65536,t=3,p=4$0vzwo1WVZmybyafmEf4J7Q$KWCFxQJ5vVnV6UPUzlvRyJRJ8YQ3qmWatRLM6N8WqJc	t	f	f
f	d97056db-1fc1-41eb-a832-91e67d5601e0	belyaev@example.com	$argon2id$v=19$m=65536,t=3,p=4$Ra9xNZNMSwcHYdAPWv2kkA$gPhQX96XNlA6iUX7ezAvl+85SGaup/y1to4Xc8M+DPc	t	f	f
t	e58350cf-2e95-4750-b1c2-395de3768c04	knyazeva@example.com	$argon2id$v=19$m=65536,t=3,p=4$WV9cFWjLlAbINZaMozpfzA$OccouIBQfU0errr/v831efhw8sHyiL6TeY9k6TIHO7Y	t	f	f
f	4141eac9-f104-458c-abd8-ac114e25cf0b	fedorova@example.com	$argon2id$v=19$m=65536,t=3,p=4$URwCnFuigKOcNQEcgnvF7w$MvzjyAZzpQ7KAtwuxuTLHAA/fWcp/ytFX2TCpodrUGg	t	f	f
\.


--
-- TOC entry 4906 (class 0 OID 0)
-- Dependencies: 225
-- Name: address_area_address_id_seq; Type: SEQUENCE SET; Schema: hospital; Owner: postgres
--

SELECT pg_catalog.setval('hospital.address_area_address_id_seq', 8, true);


--
-- TOC entry 4907 (class 0 OID 0)
-- Dependencies: 235
-- Name: area_doctor_area_doctor_id_seq; Type: SEQUENCE SET; Schema: hospital; Owner: postgres
--

SELECT pg_catalog.setval('hospital.area_doctor_area_doctor_id_seq', 11, true);


--
-- TOC entry 4908 (class 0 OID 0)
-- Dependencies: 231
-- Name: check_up_check_up_id_seq; Type: SEQUENCE SET; Schema: hospital; Owner: postgres
--

SELECT pg_catalog.setval('hospital.check_up_check_up_id_seq', 27, true);


--
-- TOC entry 4909 (class 0 OID 0)
-- Dependencies: 218
-- Name: check_up_place_check_up_place_id_seq; Type: SEQUENCE SET; Schema: hospital; Owner: postgres
--

SELECT pg_catalog.setval('hospital.check_up_place_check_up_place_id_seq', 2, true);


--
-- TOC entry 4910 (class 0 OID 0)
-- Dependencies: 222
-- Name: diagnosis_diagnosis_id_seq; Type: SEQUENCE SET; Schema: hospital; Owner: postgres
--

SELECT pg_catalog.setval('hospital.diagnosis_diagnosis_id_seq', 12, true);


--
-- TOC entry 4911 (class 0 OID 0)
-- Dependencies: 229
-- Name: doctor_doctor_id_seq; Type: SEQUENCE SET; Schema: hospital; Owner: postgres
--

SELECT pg_catalog.setval('hospital.doctor_doctor_id_seq', 15, true);


--
-- TOC entry 4912 (class 0 OID 0)
-- Dependencies: 216
-- Name: gender_gender_id_seq; Type: SEQUENCE SET; Schema: hospital; Owner: postgres
--

SELECT pg_catalog.setval('hospital.gender_gender_id_seq', 2, true);


--
-- TOC entry 4913 (class 0 OID 0)
-- Dependencies: 227
-- Name: patient_patient_id_seq; Type: SEQUENCE SET; Schema: hospital; Owner: postgres
--

SELECT pg_catalog.setval('hospital.patient_patient_id_seq', 14, true);


--
-- TOC entry 4914 (class 0 OID 0)
-- Dependencies: 233
-- Name: symptom_check_up_symptom_check_up_id_seq; Type: SEQUENCE SET; Schema: hospital; Owner: postgres
--

SELECT pg_catalog.setval('hospital.symptom_check_up_symptom_check_up_id_seq', 51, true);


--
-- TOC entry 4915 (class 0 OID 0)
-- Dependencies: 220
-- Name: symptom_symptom_id_seq; Type: SEQUENCE SET; Schema: hospital; Owner: postgres
--

SELECT pg_catalog.setval('hospital.symptom_symptom_id_seq', 9, true);


--
-- TOC entry 4704 (class 2606 OID 19789)
-- Name: address_area address_area_pkey; Type: CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.address_area
    ADD CONSTRAINT address_area_pkey PRIMARY KEY (id);


--
-- TOC entry 4714 (class 2606 OID 19867)
-- Name: area_doctor area_doctor_pkey; Type: CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.area_doctor
    ADD CONSTRAINT area_doctor_pkey PRIMARY KEY (id);


--
-- TOC entry 4702 (class 2606 OID 19783)
-- Name: area area_pkey; Type: CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.area
    ADD CONSTRAINT area_pkey PRIMARY KEY (id);


--
-- TOC entry 4710 (class 2606 OID 19825)
-- Name: check_up check_up_pkey; Type: CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.check_up
    ADD CONSTRAINT check_up_pkey PRIMARY KEY (id);


--
-- TOC entry 4696 (class 2606 OID 19766)
-- Name: check_up_place check_up_place_pkey; Type: CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.check_up_place
    ADD CONSTRAINT check_up_place_pkey PRIMARY KEY (id);


--
-- TOC entry 4700 (class 2606 OID 19778)
-- Name: diagnosis diagnosis_pkey; Type: CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.diagnosis
    ADD CONSTRAINT diagnosis_pkey PRIMARY KEY (id);


--
-- TOC entry 4708 (class 2606 OID 19816)
-- Name: doctor doctor_pkey; Type: CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.doctor
    ADD CONSTRAINT doctor_pkey PRIMARY KEY (id);


--
-- TOC entry 4694 (class 2606 OID 19760)
-- Name: gender gender_pkey; Type: CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.gender
    ADD CONSTRAINT gender_pkey PRIMARY KEY (id);


--
-- TOC entry 4706 (class 2606 OID 19800)
-- Name: patient patient_pkey; Type: CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.patient
    ADD CONSTRAINT patient_pkey PRIMARY KEY (id);


--
-- TOC entry 4712 (class 2606 OID 19851)
-- Name: symptom_check_up symptom_check_up_pkey; Type: CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.symptom_check_up
    ADD CONSTRAINT symptom_check_up_pkey PRIMARY KEY (id);


--
-- TOC entry 4698 (class 2606 OID 19772)
-- Name: symptom symptom_pkey; Type: CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.symptom
    ADD CONSTRAINT symptom_pkey PRIMARY KEY (id);


--
-- TOC entry 4719 (class 2606 OID 19951)
-- Name: accesstoken accesstoken_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accesstoken
    ADD CONSTRAINT accesstoken_pkey PRIMARY KEY (token);


--
-- TOC entry 4717 (class 2606 OID 19945)
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- TOC entry 4720 (class 1259 OID 19957)
-- Name: ix_accesstoken_created_at; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_accesstoken_created_at ON public.accesstoken USING btree (created_at);


--
-- TOC entry 4715 (class 1259 OID 19946)
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- TOC entry 4721 (class 2606 OID 19790)
-- Name: address_area address_area_area_id_fkey; Type: FK CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.address_area
    ADD CONSTRAINT address_area_area_id_fkey FOREIGN KEY (area_id) REFERENCES hospital.area(id) ON DELETE CASCADE;


--
-- TOC entry 4730 (class 2606 OID 19873)
-- Name: area_doctor area_doctor_area_id_fkey; Type: FK CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.area_doctor
    ADD CONSTRAINT area_doctor_area_id_fkey FOREIGN KEY (area_id) REFERENCES hospital.area(id) ON DELETE CASCADE;


--
-- TOC entry 4731 (class 2606 OID 19868)
-- Name: area_doctor area_doctor_doctor_id_fkey; Type: FK CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.area_doctor
    ADD CONSTRAINT area_doctor_doctor_id_fkey FOREIGN KEY (doctor_id) REFERENCES hospital.doctor(id) ON DELETE CASCADE;


--
-- TOC entry 4724 (class 2606 OID 19826)
-- Name: check_up check_up_check_up_place_id_fkey; Type: FK CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.check_up
    ADD CONSTRAINT check_up_check_up_place_id_fkey FOREIGN KEY (check_up_place_id) REFERENCES hospital.check_up_place(id) ON DELETE CASCADE;


--
-- TOC entry 4725 (class 2606 OID 19831)
-- Name: check_up check_up_diagnosis_id_fkey; Type: FK CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.check_up
    ADD CONSTRAINT check_up_diagnosis_id_fkey FOREIGN KEY (diagnosis_id) REFERENCES hospital.diagnosis(id) ON DELETE CASCADE;


--
-- TOC entry 4726 (class 2606 OID 19836)
-- Name: check_up check_up_doctor_id_fkey; Type: FK CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.check_up
    ADD CONSTRAINT check_up_doctor_id_fkey FOREIGN KEY (doctor_id) REFERENCES hospital.doctor(id) ON DELETE CASCADE;


--
-- TOC entry 4727 (class 2606 OID 19841)
-- Name: check_up check_up_patient_id_fkey; Type: FK CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.check_up
    ADD CONSTRAINT check_up_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES hospital.patient(id) ON DELETE CASCADE;


--
-- TOC entry 4722 (class 2606 OID 19801)
-- Name: patient patient_address_id_fkey; Type: FK CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.patient
    ADD CONSTRAINT patient_address_id_fkey FOREIGN KEY (address_id) REFERENCES hospital.address_area(id) ON DELETE CASCADE;


--
-- TOC entry 4723 (class 2606 OID 19806)
-- Name: patient patient_gender_id_fkey; Type: FK CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.patient
    ADD CONSTRAINT patient_gender_id_fkey FOREIGN KEY (gender_id) REFERENCES hospital.gender(id) ON DELETE CASCADE;


--
-- TOC entry 4728 (class 2606 OID 19852)
-- Name: symptom_check_up symptom_check_up_check_up_id_fkey; Type: FK CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.symptom_check_up
    ADD CONSTRAINT symptom_check_up_check_up_id_fkey FOREIGN KEY (check_up_id) REFERENCES hospital.check_up(id) ON DELETE CASCADE;


--
-- TOC entry 4729 (class 2606 OID 19857)
-- Name: symptom_check_up symptom_check_up_symptom_id_fkey; Type: FK CONSTRAINT; Schema: hospital; Owner: postgres
--

ALTER TABLE ONLY hospital.symptom_check_up
    ADD CONSTRAINT symptom_check_up_symptom_id_fkey FOREIGN KEY (symptom_id) REFERENCES hospital.symptom(id) ON DELETE CASCADE;


--
-- TOC entry 4732 (class 2606 OID 19952)
-- Name: accesstoken accesstoken_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accesstoken
    ADD CONSTRAINT accesstoken_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id) ON DELETE CASCADE;


--
-- TOC entry 4905 (class 0 OID 0)
-- Dependencies: 6
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;


-- Completed on 2024-12-10 15:30:21

--
-- PostgreSQL database dump complete
--

