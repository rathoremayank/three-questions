# Create mysql server based on the official image from the dockerhub
FROM mysql:latest as builder

# Add a database & root password
ENV MYSQL_DATABASE todo-database
ENV MYSQL_ROOT_PASSWORD=Welcome01
ENV MYSQL_USER dev
ENV MYSQL_PASSWORD GodMode@94

# Optionally, run initial scripts for creating tables
COPY ./sql-scripts/03-create-table.sql /docker-entrypoint-initdb.d/
COPY ./sql-scripts/04-create-dummy-data.sql /docker-entrypoint-initdb.d/
