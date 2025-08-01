import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:admin%40123@localhost:3306/ap',echo = True)

df = pd.read_sql("SELECT * FROM People", con = engine)

print(df)

#insert into tables
# new_data = pd.DataFrame([{'name' : 'Amber', 'age' :22}])

# new_data.to_sql('people', con = engine, if_exists = 'append', index = False)