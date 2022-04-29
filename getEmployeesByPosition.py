def get_Employees_By_Position(position, cur):
    positionsData = cur.execute("""
        SELECT
            position
        FROM 
            positions
    """)
    positions = positionsData.fetchall()
    positions = [item for t in positions for item in t]
    if position not in positions:
        print("That position does not exist")
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
            positions p
            ON p.id = e_d.position_id
        WHERE p.position = ?
        """, [position])
    employees = data.fetchall()
    print("\n")
    print("\n")
    print("""
Position: {}
    Employees:
        """.format(position))
    for employee in employees:
        if employee is None:
            print("There are none")
            return
        else:
            print(employee[1])
    print("\n")
    print("\n")