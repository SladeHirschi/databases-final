CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    employee_name TEXT
);

CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    dept_name TEXT
);

CREATE TABLE positions (
    id INTEGER PRIMARY KEY,
    position TEXT
);

CREATE TABLE status (
    id INTEGER PRIMARY KEY,
    status TEXT
);

CREATE TABLE employee_details (
    id INTEGER PRIMARY KEY,
    employment_start DATE,
    position_id id,
    employee_id INTEGER UNIQUE,
    department_id id,
    FOREIGN KEY (position_id) REFERENCES positions(id),
    FOREIGN KEY (employee_id) REFERENCES employees(id),
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

CREATE TABLE members (
    id INTEGER PRIMARY KEY,
    member_name TEXT
);

CREATE TABLE member_details(
    id INTEGER PRIMARY KEY,
    member_id INT,
    email TEXT,
    member_start DATE,
    status_id INT
);