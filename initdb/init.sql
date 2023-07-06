CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(120) NOT NULL
);

CREATE TABLE posts(
    post_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    text TEXT,
    created_at TIMESTAMP
);
