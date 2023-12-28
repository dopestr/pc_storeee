CREATE TABLE Users (
id INT PRIMARY KEY,
username VARCHAR(255),
email VARCHAR(255),
password VARCHAR(255)
);

CREATE TABLE Workers (
id2 INT PRIMARY KEY,
name VARCHAR(255),
position VARCHAR(255),
salary DECIMAL(10, 2)
);

CREATE TABLE Store (
id3 INT PRIMARY KEY,
name VARCHAR(255),
location VARCHAR(255),
capacity INT
);


CREATE TABLE Providers (
id5 INT PRIMARY KEY,
name VARCHAR(255),
contact VARCHAR(255),
address VARCHAR(255)
);

CREATE TABLE Orders (
id6 INT PRIMARY KEY,
date DATE,
user_id INT,
product_id INT,
FOREIGN KEY (user_id) REFERENCES Users(id),
FOREIGN KEY (product_id) REFERENCES Product(id)
);


INSERT INTO Users (id, username, email, password)
VALUES (1, 'JohnDoe', 'johndoe@example.com', 'password1'),
(2, 'JaneSmith', 'janesmith@example.com', 'password2');

INSERT INTO Workers (id2, name, position, salary)
VALUES (1, 'Mike Johnson', 'Manager', 5000.00),
(2, 'Emily Davis', 'Cashier', 2500.00);

INSERT INTO Store (id3, name, location, capacity)
VALUES (1, 'SuperMart', '123 Main St', 1000),
(2, 'Grocery World', '456 Elm St', 1500);


INSERT INTO Providers (id5, name, contact, address)
VALUES (1, 'ABC Produce', 'John Smith', '123 Oak St'),
(2, 'XYZ Groceries', 'Jane Doe', '456 Maple Ave');

INSERT INTO Orders (id6, date, user_id, product_id)
VALUES (1, '2021-01-01', 1, 1),
(2, '2021-01-02', 2, 2);
