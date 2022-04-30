def get_Members(cur):
    data = cur.execute("""
        SELECT 
            e.*,
            e_d.*
        FROM
            members e
        JOIN
            member_details e_d
            ON e_d.member_id = e.id
        """)
    members = data.fetchall()
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