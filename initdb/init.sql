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

CREATE TABLE likes(
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    CONSTRAINT likes_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES users (user_id) ON DELETE CASCADE,
    CONSTRAINT likes_post_id_fkey FOREIGN KEY (post_id)
        REFERENCES posts (post_id) ON DELETE CASCADE,
    PRIMARY KEY (post_id, user_id)
);

CREATE TABLE dislikes(
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    CONSTRAINT likes_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES users (user_id) ON DELETE CASCADE,
    CONSTRAINT likes_post_id_fkey FOREIGN KEY (post_id)
        REFERENCES posts (post_id) ON DELETE CASCADE,
    PRIMARY KEY (post_id, user_id)
);

CREATE TABLE reactions(
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    reaction BOOLEAN,
    CONSTRAINT likes_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES users (user_id) ON DELETE CASCADE,
    CONSTRAINT likes_post_id_fkey FOREIGN KEY (post_id)
        REFERENCES posts (post_id) ON DELETE CASCADE,
    PRIMARY KEY (post_id, user_id)
);