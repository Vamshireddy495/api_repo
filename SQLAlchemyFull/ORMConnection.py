from sqlalchemy import create_engine , Column, Integer , String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

#1 create engine
engine = create_engine("mysql+pymysql://root:admin%40123@localhost:3306/ap",echo = True)

#2 create a sessionmaker [not connection]      

# with engine.connection as conn:
     #conn.execute(statement)

# Create a Base class
Base = declarative_base()

#declare class, Defines a Table
class Person(Base):                 #Singular 
    __tablename__ = 'people'        #Plural

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    age = Column(Integer)
#declare relationship
    things = relationship('Thing', back_populates = 'person')
    
    
class Thing(Base):
    __tablename__ = 'things'

    id = Column(Integer, primary_key = True)
    description = Column(String(150), nullable = False, unique = True)
    value = Column(Integer)
    owner = Column(Integer, ForeignKey('people.id'))

    person = relationship('Person', back_populates = 'things')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)         #Create session
session = Session()                         #Create Instance of Session

# new_person = Person(name= 'Chaitanya', age = 41)
# session.add(new_person)                             #execute the query

# insert_query = session.query(Person).filter_by(name = 'Julien').first()
# if insert_query:
#     item = Thing(description='Charger', value = 30)
#     insert_query.things.append(item)
#     session.commit()

session.close()

with session:
    
    update_person = session.query(Person).filter_by(name='Amber').first()
    if update_person:
        update_person.name = "Julien"
        session.commit()
    else:
        print("Not found")

with session:

    select_query = session.query(Person).all()
    if select_query:
        print([p.name for p in select_query])


with session:

    select_statement = session.query(Person.name, Person.age)

    for name, age in select_statement:
        print(f"name:{name}, age:{age}")

# with session:
#     delete_query = session.query(Person).filter_by(name = 'Julien').first()
#     if delete_query:
#         session.delete(delete_query)
#         session.commit()
#     else:
#         print('not found')

with session:
    x = session.query(Thing).filter(Thing.owner == 5)
    for row in x:
        print(row.owner, row.description, row.value)