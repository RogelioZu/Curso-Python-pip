
import charts_app
import csv_reader
import util


file = 'app/data.csv'


def run():

    data = csv_reader.read(file)
    data = list(filter(lambda item: item["Continent"] == "South America", data))
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'],data))


    country = input("Type country => ").title()

    result = util.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        print(country['Country/Territory'])
        keys, values = util.get_population(country)
        charts_app.generate_bar_chart(country['Country/Territory'],keys, values)


    
    charts_app.generate_pie_chart('South America',countries,percentages)

if __name__ == '__main__':
    run()

