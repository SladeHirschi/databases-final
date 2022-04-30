def move_Employee(employee, department, cur):
    departmentdata = cur.execute("""
        SELECT
            d.id,
            e.id
        FROM
            departments d
        JOIN 
            employees e
            ON e.employee_name = ?
        JOIN
            employee_details e_d
            ON e_d.employee_id = e.id
        WHERE d.dept_name = ?
    """,[employee, department])
    departments = departmentdata.fetchone()
    #print(departments)
    #print(departments[1])
    if departments is not None:
        cur.execute("""
            UPDATE 
                employee_details
            SET 
                department_id = ?
            WHERE
                employee_id = ?
        """,[departments[0],departments[1]])
    else:
        print("Employee not in the system")

    # departmenttestdata = cur.execute("""
    #     SELECT
    #         e.*
    #     FROM
    #         employee_details e
    #     WHERE e.employee_id = ?
    # """,[departments[1]])
    # testdepartments = departmenttestdata.fetchall()
    # print(testdepartments)