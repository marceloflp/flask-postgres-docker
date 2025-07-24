FROM postgres:15

ENV POSTGRES_DB=bd_aplicacao
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=admin

COPY init.sql /docker-entrypoint-initdb.d/
