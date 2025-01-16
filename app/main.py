
import charts_app
import csv_reader



data = 'app/data.csv'


def run():

    data2 = csv_reader.read(data)
    data2 = list(filter(lambda item: item["Continent"] == "South America", data2))
    countries = list(map(lambda x: x['Country/Territory'], data2))
    percentages = list(map(lambda x: x['World Population Percentage'],data2))
    
    charts_app.generate_pie_chart(countries,percentages)
    
if __name__ == '__main__':
    run()

