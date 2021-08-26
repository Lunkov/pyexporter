CREATE SEQUENCE public.news_id_seq;
CREATE TABLE public.news
(
    id      bigint       NOT NULL DEFAULT nextval('news_id_seq'),
    title   varchar(255) NOT NULL DEFAULT '',
    author  varchar(255) NOT NULL DEFAULT '',
    article text         NOT NULL DEFAULT '',
    PRIMARY KEY (id),
    CONSTRAINT "news_title_author" UNIQUE (title, author)
);
