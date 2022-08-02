CREATE TABLE admin_users (
    admin_id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE shop (
    shop_id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE customers (
    order_id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE categorys (
    category_id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    price INT NOT NULL,
    model VARCHAR(255) NOT NULL
);

CREATE TABLE cart (
    cart_id SERIAL PRIMARY KEY NOT NULL,
    quantity INT NOT NULL,
    total_cost INT NOT NULL
);

CREATE TABLE payment (
    payment_id SERIAL PRIMARY KEY NOT NULL,
    amount VARCHAR(255) NOT NULL,
    payment_type VARCHAR(255) NOT NULL
);