-- TODO Roles Table
CREATE TABLE Roles (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(20)
);

-- INSERT INTO Roles (role_name) VALUES ('Admin');
-- INSERT INTO Roles (role_name) VALUES ('Librarian');
-- INSERT INTO Roles (role_name) VALUES ('Member');

-- TODO Category Table
CREATE TABLE Genre (
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(20)
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
    author_name VARCHAR(100),
    publisher_name VARCHAR(100),
    copies_available INT,
    year_of_publisher INT,
    created_at DATE,
    genre_id INT REFERENCES Genre(genre_id) ON DELETE SET NULL
);

CREATE TABLE BorrowedRecord (
    borrow_record_id SERIAL PRIMARY KEY,
    borrow_date DATE,
    due_date DATE,
    return_date DATE,
    status VARCHAR(50),
    user_id INT REFERENCES Users(user_id) ON DELETE SET NULL
);

CREATE TABLE BorrowedItems (
    borrow_item_id SERIAL PRIMARY KEY,
    status VARCHAR(50),
    quantity INT,
    borrow_record_id INT REFERENCES BorrowedRecord(borrow_record_id) ON DELETE SET NULL
);



-- TODO Publisher Table
CREATE TABLE Publishers (
    publisher_id SERIAL PRIMARY KEY,
    publisher_name VARCHAR(100),
    address VARCHAR(255),
    phone_number VARCHAR(15)
);

-- TODO Borrow Table
CREATE TABLE BorrowedBooks (
    borrow_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES Users(user_id) ON DELETE SET NULL,
    book_id INT REFERENCES Books(book_id) ON DELETE SET NULL,
    borrow_date DATE,
    return_date DATE,
    status VARCHAR(50)
);

-- TODO Reservations Table
CREATE TABLE Reservations (
    reservation_id SERIAL PRIMARY KEY,
    reservation_date DATE,
    status VARCHAR(50),
    user_id INT REFERENCES Users(user_id) ON DELETE SET NULL
);

CREATE TABLE ReservationItems (
    reservation_item_id SERIAL PRIMARY KEY,
    status VARCHAR(50),
    quantity INT,
    reservation_id INT REFERENCES Reservations(reservation_id) ON DELETE SET NULL
);


-- TODO Fines Table
CREATE TABLE Fines (
    fine_id SERIAL PRIMARY KEY,
    fine_date DATE,
    amount DECIMAL(10, 2),
    paid_date DATE,
    status VARCHAR(50),
    borrow_item_id INT REFERENCES BorrowedItems(borrow_item_id) ON DELETE SET NULL
);
