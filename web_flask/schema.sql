-- Schemas
DROP SCHEMA IF EXISTS auth;
CREATE SCHEMA auth;


-- Tables
DROP TABLE IF EXISTS auth.users;
CREATE TABLE auth.users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);