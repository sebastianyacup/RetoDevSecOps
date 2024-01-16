CREATE TABLE IF NOT EXISTS vulnerability (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT
);