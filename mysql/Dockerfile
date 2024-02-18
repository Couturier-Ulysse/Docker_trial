FROM mysql:latest

COPY ./database_students.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

CMD ["mysqld"]
