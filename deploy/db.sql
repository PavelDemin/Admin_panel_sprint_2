-- Create schema 'content':
CREATE SCHEMA IF NOT EXISTS content;

-- Add new schema 'content' in search_path:
SET search_path TO content,public;

-- Create table 'film_work':
CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title VARCHAR(250) NOT NULL,
    description TEXT,
    creation_date DATE,
    certificate TEXT,
    file_path VARCHAR(100),
    rating FLOAT,
    type VARCHAR(50) not null,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- Create table 'genre':
CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- Create table 'genre_film_work':
CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid REFERENCES content.film_work NOT NULL,
    genre_id uuid REFERENCES content.genre NOT NULL,
    created_at timestamp with time zone
);

-- Create table 'person':
CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    birth_date DATE,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- Create table 'person_film_work':
CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid REFERENCES content.film_work NOT NULL,
    person_id uuid REFERENCES content.person NOT NULL,
    role VARCHAR(150) NOT NULL,
    created_at timestamp with time zone
);

-- Create index 'film_work_person_role_idx':
CREATE UNIQUE INDEX IF NOT EXISTS film_work_person_role_idx ON content.person_film_work (film_work_id, person_id, role);

-- Create index 'film_work_genre_idx':
CREATE UNIQUE INDEX IF NOT EXISTS film_work_genre_idx ON content.genre_film_work (film_work_id, genre_id);

-- Create index 'film_work_creation_date_rating_idx':
CREATE INDEX IF NOT EXISTS film_work_creation_date_rating_idx ON content.film_work (creation_date, rating);