def move_Employee_Position(employee, position, cur):
    positiondata = cur.execute("""
        SELECT
            p.id,
            e.id
        FROM
            positions p
        JOIN
            employees e
            ON e.employee_name = ?
        WHERE p.position = ?
    """,[employee, position])
    positions = positiondata.fetchone()
    if positions is not None:
        cur.execute("""
            UPDATE
                employee_details
            SET
                position_id = ?
            WHERE
                employee_id = ?
        """,[positions[0],positions[1]])
    else:
        print("Employee not in the system")