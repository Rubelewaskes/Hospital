FROM postgres:15

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=1234
ENV POSTGRES_DB=hospital

COPY hospital_backup.sql /docker-entrypoint-initdb.d/

EXPOSE 1266