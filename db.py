import mysql.connector

statements = (
    "create database if not exists cli_chat;",
    "use cli_chat;",
    "create table if not exists users( "\
        "id int not null auto_increment, "\
        "name varchar(150) not null, "\
        "primary key (id));",
    "show databases;",
    "show tables;"
)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "CromegaStudio08*"
)

cursor = db.cursor(buffered = True)

for statement in statements: cursor.execute(statement)

for dbs in cursor: print(dbs)


cursor.execute("drop database cli_chat;")
