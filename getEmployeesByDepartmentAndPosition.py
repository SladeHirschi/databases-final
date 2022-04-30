def get_Employees_By_Department_And_Position(department, position, cur):
    departmentsdata = cur.execute("""
        SELECT
            dept_name
        FROM 
            departments
    """)
    departments = departmentsdata.fetchall()
    departments = [item for t in departments for item in t]
    if department not in departments:
        print("That department does not exist")
        return
    data = cur.execute("""
        SELECT 
            e.*,
            e_d.*
        FROM
            employees e
        JOIN
            employee_details e_d
            ON e_d.employee_id = e.id
        JOIN
            departments d
            ON d.id = e_d.department_id
        JOIN
            positions p
            ON p.id = e_d.position_id
        WHERE d.dept_name = ? AND p.position = ?
        """, [department, position])
    employees = data.fetchall()
    print("\n")
    print("\n")
    print("""
Department: {}
    {}s:
        """.format(department, position))
    for employee in employees:
        if employee is None:
            print("There are none")
            return
        else:
            print(employee[1])
    print("\n")
    print("\n")