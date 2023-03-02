#!/usr/bin/env python

import json
import sqlalchemy
import pandas as pd

# connect to the database
engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database/codetest")
connection = engine.connect()

people_df = pd.read_csv('/data/people.csv')
people_df.to_sql('people', con=engine, if_exists='append', index=True)

places_df = pd.read_csv('/data/places.csv')
places_df.to_sql('places', con=engine, if_exists='append', index=True)

# people_df.to_json(r'/data/sample_output.json')

query = "SELECT COUNT(*), a.country FROM places as a RIGHT JOIN people as p ON p.place_of_birth = " \
        "a.city GROUP BY " \
        "a.country"

output = connection.execute(query)
df = pd.DataFrame(output.fetchall())
#df = df.set_index("country")

dictionary = df.set_index('country').to_dict()['COUNT(*)']

with open("/data/sample_output.json", "w") as outfile:
    json.dump(dictionary, outfile)

#df.to_json(r'/data/sample_output.json')

print("done")
