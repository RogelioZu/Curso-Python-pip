import pandas as pd
import charts_app
import csv_reader
import util





def run():

   
    """
    
    data = list(filter(lambda item: item["Continent"] == "South America", data))
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'],data))

    """

    df = pd.read_csv('data.csv')
    df = df [df['Continent'] == 'Africa']
    countries = df ['Country/Territory'].values
    percentages = df['World Population Percentage'].values

    charts_app.generate_pie_chart('Africa',countries,percentages)
  

    country = input("Type country => ").title()
    
    data = csv_reader.read('data.csv')

    result = util.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        print(country['Country/Territory'])
        keys, values = util.get_population(country)
        charts_app.generate_bar_chart(country['Country/Territory'],keys, values)

        


    
    

if __name__ == '__main__':

        
    run()

