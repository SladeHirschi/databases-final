def get_Employee_Details(employee, cur):
    data = cur.execute("""
        SELECT 
            e.employee_name,
            e_d.employment_start,
            p.position,
            d.dept_name
        FROM
            employees e
        JOIN
            employee_details e_d
            ON e_d.employee_id = e.id
        JOIN
            positions p
            ON p.id = e_d.position_id
        JOIN
            departments d
            ON d.id = e_d.department_id
        WHERE e.employee_name = ?
        """, [employee])
    employee = data.fetchone()
    if employee is None:
        print("There is no employee by that name")
        return
    list(employee)
    print("\n")
    print("""
    Employee: 
        Name: {} 
        Start Date: {} 
        Position: {} 
        Department: {}
    """.format(employee[0], employee[1], employee[2], employee[3]))
    print("\n")

def get_Member_Details(member, cur):
    data = cur.execute("""
        SELECT 
            m.member_name,
            m_d.email,
            m_d.member_start,
            s.status
        FROM
            members m
        JOIN
            member_details m_d
            ON m_d.member_id = m.id
        JOIN
            status s
            ON m_d.status_id = s.id
        WHERE m.member_name = ?
        """, [member])
    member = data.fetchone()
    if member is None:
        print("There is no member by that name")
        return
    list(member)
    print("\n")
    print("""
    Member: 
        Name: {} 
        Email: {} 
        Member Start Date: {} 
        Status: {}
    """.format(member[0], member[1], member[2], member[3]))
    print("\n")