def get_Supervisors_By_Department(department, cur):
    departmentsdata = cur.execute("""
        SELECT
            dept_name
        FROM 
            departments
    """)
    departments = departmentsdata.fetchall()
    departments = [item for t in departments for item in t]
    if department not in departments:
        print("\n")
        print("\n")
        print("That department does not exist")
        print("\n")
        print("\n")
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
        WHERE d.dept_name = ? AND p.position = 'supervisor'
        """, [department])
    supervisors = data.fetchall()
    print("\n")
    print("\n")
    print("""
Department: {}
    Supervisors:
        """.format(department))
    for supervisor in supervisors:
        if supervisor is None:
            print("There are none")
            return
        else:
            print(supervisor[1])
    print("\n")
    print("\n")