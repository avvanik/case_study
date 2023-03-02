#!/usr/bin/env python

import sqlalchemy
from convert import Converter
from output import Query

# connect to db
engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database/codetest")
connection = engine.connect()


def main():
    Converter(engine).csv_to_sql()
    Query(connection).output_to_json()


if __name__ == "__main__":
    main()

