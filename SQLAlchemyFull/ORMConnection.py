from sqlalchemy import create_engine , Column, Integer , String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

#1 create engine
engine = create_engine("mysql+pymysql://root:admin%40123@localhost:3306/ap",echo = True)

#2 create a sessionmaker [not connection]      

# with engine.connection as conn:
     #conn.execute(statement)

Session = sessionmaker(engine)

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
    description = Column(String(150), nullable = False)
    value = Column(Integer)
    owner = Column(Integer, ForeignKey('people.id'))

    person = relationship('Person', back_populates = 'things')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)         #Create session
session = Session()                         #Create Instance of Session

# new_person = Person(name= 'Chaitanya', age = 41)
# session.add(new_person)                             #execute the query

session.commit()

session.close()


