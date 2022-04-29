def get_Employees(cur):
    data = cur.execute("""
        SELECT 
            e.*,
            e_d.*
        FROM
            employees e
        JOIN
            employee_details e_d
            ON e_d.employee_id = e.id
        """)
    employees = data.fetchall()
    print("\n")
    print("\n")
    print("""
    Employees:
        """)
    for employee in employees:
        if employee is None:
            print("There are none")
            return
        else:
            print(employee[1])
    print("\n")
    print("\n")