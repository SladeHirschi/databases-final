CREATE TABLE employee (
    id INTEGER PRIMARY KEY,
    employee_name TEXT
);

CREATE TABLE department (
    id INTEGER PRIMARY KEY,
    dept_name TEXT
);

CREATE TABLE position (
    id INTEGER PRIMARY KEY,
    position TEXT
);

CREATE TABLE employeeDetails (
    id INTEGER PRIMARY KEY,
    employee_start DATE,
    position TEXT,
    employee_id INTEGER UNIQUE,
    department TEXT
    FOREIGN KEY (position) REFERENCES position(position)
    FOREIGN KEY (employee_id) REFERENCES employee(id)
    FOREIGN KEY (department) REFERENCES department(dept_name)
);

CREATE TABLE members (
    id INTEGER PRIMARY KEY,
    member_name TEXT
)

CREATE TABLE memberDetails(
    id INTEGER PRIMARY KEY,
    email TEXT,
    member_start DATE,
    member_status TEXT
);