
def check_Is_Admin(admin, cur):
    employeedata = cur.execute("""
        SELECT
            id
        FROM
            employees
        WHERE id = ?
    """,[admin])
    employee = employeedata.fetchall()
    print(employee)
    if employee != []:
        details = cur.execute("""
            SELECT
                e_d.position_id
            FROM
                employee_details e_d
            WHERE e_d.employee_id = ?
        """,[admin])
        adminId = details.fetchone()
        print(adminId[0])
        if adminId[0] == 3:
            print("Reached into the if statement, something is wrong elsewhere.")
            return True
    return False