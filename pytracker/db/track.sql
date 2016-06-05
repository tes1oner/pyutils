DROP TABLE IF EXISTS "bugs";
CREATE TABLE "bugs" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  UNIQUE ,
    "title" VARCHAR(60) UNIQUE ,
    "details" TEXT (512),
    "status" INTEGER,
    "id_user" INTEGER);
DROP TABLE IF EXISTS "tasks";
CREATE TABLE "tasks" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  UNIQUE ,
    "title" VARCHAR(60) UNIQUE ,
    "details" TEXT (512),
    "status" INTEGER,
    "id_user" INTEGER);
DROP TABLE IF EXISTS "users";
CREATE TABLE "users" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  UNIQUE ,
    "name" VARCHAR (128),
    "email" VARCHAR(45) UNIQUE,
    "username" VARCHAR(32) UNIQUE
    );
