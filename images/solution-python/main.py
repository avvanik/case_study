#!/usr/bin/env python

import sqlalchemy
import convert
import output

# connect to db
engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database/codetest")
connection = engine.connect()


def main():
    convert.Converter(engine).csv_to_sql()
    output.Query(connection).output_to_json()


if __name__ == "__main__":
    main()

