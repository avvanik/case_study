import pandas as pd


class Converter:

    def __init__(self, engine):
        self.engine = engine
        self.csv_names = ['people', 'places']
        self.id_names = ['person', 'city']

    def csv_to_sql(self):
        """Function saves people + person tables in mysql db.
        Schema is modified by adding individual id_keys as primary key"""

        for self.csv_name, self.id_name in zip(self.csv_names, self.id_names):
            df = pd.read_csv(f'/data/{self.csv_name}.csv')
            df[f'{self.id_name}_id'] = range(1, 1 + len(df))
            df[f'{self.id_name}_id'] = f'{self.id_name[0]}' + df[f'{self.id_name}_id'].astype(str)
            df.to_sql(f'{self.csv_name}', con=self.engine, if_exists='replace', index=False)
