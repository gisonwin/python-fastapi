from db_init import engine, person_table

with engine.connect() as conn:
    query = person_table.select()
    rs = conn.execute(query)
    # for row in rs:
    #     print(row[0], row.name)

    # all_persons = rs.fetchall()
    # print(all_persons)

    one_person = rs.fetchone()
    print(one_person)

    conn.close()
