CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(30),
    email VARCHAR(30),
    password VARCHAR(30),
    age TINYINT UNSIGNED,
    gender_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (gender_id) REFERENCES genders (id)
          ON DELETE SET NULL
          ON UPDATE CASCADE
);

CREATE TABLE contacts (
    id INT PRIMARY KEY,
    name VARCHAR(30),
    email VARCHAR(30),
    phone VARCHAR(30),
    favorite BOOLEAN,
    user_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);

INSERT INTO genders (id, name)
VALUES (1, 'male'), (2, 'female');

INSERT INTO genders VALUES(2, 'female', '2022-10-11 19:23:46');

INSERT INTO users (id, name, email, password, age, gender_id)
VALUES (1, 'Boris', 'boris@test.com', 'password', 23, 1),
(2, 'Alina', 'alina@test.com', 'password', 32, 2),
(3, 'Maksim', 'maksim@test.com', 'password', 40, 1);

INSERT INTO contacts (id, name, email, phone, favorite, user_id)
VALUES (1, 'Allen Raymond', 'nulla.ante@vestibul.co.uk', '(992) 914-3792', 0, 1),
(2, 'Chaim Lewis', 'dui.in@egetlacus.ca', '(294) 840-6685', 1, 1),
(3, 'Kennedy Lane', 'mattis.Cras@nonenimMauris.net', '(542) 451-7038', 1, 2),
(4, 'Wylie Pope', 'est@utquamvel.net', '(692) 802-2949', 0, 2),
(5, 'Cyrus Jackson', 'nibh@semsempererat.com', '(501) 472-5218', 0, null);

SELECT * FROM users q

SELECT name, phone, id FROM contacts c

SELECT name, phone, id 
   FROM contacts c
ORDER BY name 

SELECT name, phone, id 
   FROM contacts c
ORDER BY 3 DESC

SELECT name, email
   FROM contacts c 
WHERE favorite = TRUE 
ORDER BY name

SELECT *
   FROM users u 
WHERE age > 30
ORDER BY gender_id DESC, name 


SELECT * FROM users u
WHERE id BETWEEN 2 AND 5

SELECT * FROM users u
WHERE name = 'Alina'

SELECT * FROM contacts c 
WHERE email LIKE '%.net'

ALTER TABLE users ADD sallary INTERGER;

SELECT MAX(age), MIN(age), AVG(age) FROM users;

SELECT MAX(sallary) as max_sallary, SUM(sallary)/COUNT(*) as AVG_sallary FROM users;


SELECT c.id, c.name, c.email, u.name AS owner
FROM contacts AS c
JOIN users AS u ON u.id = c.user_id

SELECT c.id, c.name, c.email, u.name AS owner
FROM contacts AS c
LEFT JOIN users AS u ON u.id = c.user_id

SELECT u.id, u.name, g.name AS gender
   FROM users u
  LEFT JOIN genders g ON g.id = u.gender_id
  
  
  
  
  
  
  
  
