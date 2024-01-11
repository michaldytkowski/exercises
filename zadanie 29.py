import json
import csv

def json_to_csv():
    with open('users.json', 'r') as f:
        json_data = json.loads(f.read())
    with open('users.csv', 'w') as f:
        headers = json_data[0].keys()
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in json_data:
            writer.writerow(row)


        



json_to_csv()