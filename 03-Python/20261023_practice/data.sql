CREATE DATABASE IF NOT EXISTS python_course CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE python_course;

CREATE TABLE IF NOT EXISTS learners (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    weekly_hours DECIMAL(5, 1) NOT NULL,
    goal VARCHAR(255) NOT NULL
);