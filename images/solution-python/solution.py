#!/usr/bin/env python

import json
import sqlalchemy
import pandas as pd

# connect to the database
engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database/codetest")
connection = engine.connect()

# set list for csvs
csv_names = ['people', 'places']
# set names for primary_key
id_names = ['person', 'city']

# load data to db + define schema
for csv_name, id_name in zip(csv_names, id_names):
    df = pd.read_csv(f'/data/{csv_name}.csv')
    df[f'{id_name}_id'] = range(1, 1 + len(df))
    df[f'{id_name}_id'] = f'{id_name[0]}' + df[f'{id_name}_id'].astype(str)
    df.to_sql(f'{csv_name}', con=engine, if_exists='replace', index=False)

# query list of countries + people born in country
query = "SELECT COUNT(*) as people_count, a.country FROM places as a RIGHT JOIN people as p ON p.place_of_birth = " \
        "a.city GROUP BY " \
        "a.country"

output = connection.execute(query)

# safe as json
dictionary = pd.DataFrame(output.fetchall()).set_index('country').to_dict()['people_count']
with open("/data/summary_output.json", "w") as outfile:
    json.dump(dictionary, outfile)
