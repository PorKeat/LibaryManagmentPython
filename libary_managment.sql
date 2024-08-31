-- TODO Roles Table
CREATE TABLE Roles (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(20)
);

INSERT INTO Roles (role_name) VALUES ('Admin');
INSERT INTO Roles (role_name) VALUES ('Librarian');
INSERT INTO Roles (role_name) VALUES ('Member');


-- TODO Authors Table
CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(50)
);

-- TODO Category Table
CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(20)
);

-- TODO User Table
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    password VARCHAR(100),
    phone_number VARCHAR(15),
    membership_date DATE,
    role_id INT REFERENCES Roles(role_id) ON DELETE SET NULL
);

-- TODO Books Table
CREATE TABLE Books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    created_at DATE,
    copies_available INT,
    year_of_publisher INT,
    category_id INT REFERENCES Categories(category_id) ON DELETE SET NULL,
    author_id INT REFERENCES Authors(author_id) ON DELETE SET NULL
);

-- TODO Publisher Table
CREATE TABLE Publishers (
    publisher_id INT PRIMARY KEY,
    publisher_name VARCHAR(100),
    address VARCHAR(255),
    phone_number VARCHAR(15)
);

-- TODO Borrow Table
CREATE TABLE BorrowedBooks (
    borrow_id INT PRIMARY KEY,
    user_id INT REFERENCES Users(user_id) ON DELETE SET NULL,
    book_id INT REFERENCES Books(book_id) ON DELETE SET NULL,
    borrow_date DATE,
    return_date DATE,
    status VARCHAR(50)
);

-- TODO Reservations Table
CREATE TABLE Reservations (
    reservation_id INT PRIMARY KEY,
    user_id INT REFERENCES Users(user_id) ON DELETE SET NULL,
    book_id INT REFERENCES Books(book_id) ON DELETE SET NULL,
    reservation_date DATE,
    status VARCHAR(50)
);

-- TODO Fines Table
CREATE TABLE Fines (
    fine_id INT PRIMARY KEY,
    status VARCHAR(50),
    amount DECIMAL(10, 2),
    borrow_id INT REFERENCES BorrowedBooks(borrow_id) ON DELETE SET NULL
);
