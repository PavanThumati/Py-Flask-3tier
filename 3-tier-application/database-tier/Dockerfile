FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=userdb

COPY init.sql /docker-entrypoint-initdb.d/
