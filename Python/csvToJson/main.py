import json
import csv


def convertir_json(archivoCsv):
    data = []

    with open(archivoCsv, encoding='utf-8') as csvDocument:
        csvreader = csv.DictReader(csvDocument)
        for row in csvreader:
            data.append(row)

    with open('data.json', 'w', encoding='utf-8') as jsonDocument:
        string = json.dumps(data, indent=4)
        jsonDocument.write(string)


csvLocation = r'mortality.csv'

convertir_json(csvLocation)
