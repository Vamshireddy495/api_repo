from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
#1 Establish a connection 
engine = create_engine('mysql+pymysql://root:admin%40123@localhost:3306/ap',echo = True)
#2 Create a MetaData OBject (It stores the schemas of our database, also, it is necessary to define the Table, Column structures)
meta = MetaData()
#3 Define a Table in meta Object
people = Table('people',
               meta,
               Column('id', Integer, primary_key = True),
               Column('name', String, nullable = False),
               Column('age', Integer))
try:
    #4 Create the above table which is defined in the meta object in Database
    meta.create_all(engine)
    print("Connected Successfully")
except Exception as e:
    print(f"{e}")

#functions to insert data

# try:
#     conn = engine.connect()
#     insert_statement = people.insert().values(name = "Mike", age = 30)
#     result = conn.execute(insert_statement)
#     conn.commit()
# except Exception as e:
#     print(f"{e}")


# select statement
# conn = engine.connect()
# select_statement = people.select()#.where(people.c.name == 'Mike')
# #update_statement = people.update().where(people.c.name == 'Mike').values(age = 35)
# result = conn.execute(select_statement)

# # conn.commit()
# for row in result.fetchall():
#     print(row)
# conn.close()

# conn = engine.connect()

#5 Lets Query people table, so define the select_statement query
select_statement = people.select() 
# select_statement = people.select().where(people.c.name == 'Mike')

# # Execute the query
# result = conn.execute(select_statement)

# # Loop through the results and print each row
# for row in result.fetchall():
#     print(row)

# # No need to commit as it's a read-only operation
# conn.close()  # Close the connection after use

#6 Lets execute our select_query (using with statement helps us to close the connection after execution)
with engine.connect() as conn:

    results = conn.execute(select_statement)

    for row in results.fetchall():
        print(row)
