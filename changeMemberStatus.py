def change_Member_Status(member, status, cur, con):
    memberData = cur.execute("""
        SELECT
            m.id,
            s.id
        FROM 
            members m
        JOIN
            status s
            ON s.status = ?
        WHERE m.member_name = ?
    """,[status, member])
    member = memberData.fetchone()
    print(member[1],member[0] )
    if member is not None:
        cur.execute("""
            UPDATE 
                member_details
            SET 
                email = ?
            WHERE
                member_id = ?
        """,[member[1],member[0]])
        con.commit()
    else:
        print("Employee not in the system")