def get_Members_By_Status(status, cur):
    data = cur.execute("""
        SELECT 
            m.*,
            m_d.*
        FROM
            members m
        JOIN
            member_details m_d
            ON m_d.member_id = m.id
        JOIN
            status s
            ON m_d.status_id = s.id
        WHERE s.status = ?
        """, [status])
    members = data.fetchall()
    print("These are the members from status: ", status)
    print("\n")
    print("\n")
    print("""
    Members:
        """)
    for member in members:
        if member is None:
            print("There are none")
            return
        else:
            print(member[1])
    print("\n")
    print("\n")