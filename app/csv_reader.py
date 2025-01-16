import csv

population_data = {}

def read_and_get(path):
    with open(path, mode='r', encoding='utf-8')as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            country = row['Country/Territory']
            percentage = float(row['World Population Percentage'])
            population_data[country] = percentage

        keys = population_data.keys()
        values = population_data.values()

        return keys,values

def read(path):
    with open(path, mode='r', encoding='utf-8') as file:
        csv_reader = list(csv.DictReader(file))

        return csv_reader

