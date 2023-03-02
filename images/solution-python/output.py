import pandas as pd
import json


class Query:

    def __init__(self, connection):
        self.connection = connection

    def output_to_json(self):
        """ Function queries list of countries + people born in country. Output is saved as json """

        query = "SELECT COUNT(*) as people_count, a.country FROM places as a RIGHT JOIN people as p ON " \
                "p.place_of_birth = " \
                "a.city GROUP BY " \
                "a.country"

        output = self.connection.execute(query)

        dictionary = pd.DataFrame(output.fetchall()).set_index('country').to_dict()['people_count']
        with open("/data/summary_output.json", "w") as outfile:
            json.dump(dictionary, outfile)
