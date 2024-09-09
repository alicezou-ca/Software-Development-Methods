#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on May 28 10:04:26 2024
Based on: https://www.kaggle.com/datasets/arbazmohammad/world-airports-and-airlines-datasets
Sample input: --AIRLINES="airlines.yaml" --AIRPORTS="airports.yaml" --ROUTES="routes.yaml" --QUESTION="q1" --GRAPH_TYPE="bar"
"""

import sys
import yaml
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def solve(airlines: pd.DataFrame, airports: pd.DataFrame, routes: pd.DataFrame, question: str, graph_type: str):
    """Using question, figures out which question is being asked for and calls the correct function 
       to solve it

    Parameters
    ----------
    airlines: pd.DataFrame
        Pandas DataFrame containing list of dictionaries from airlines.yaml
    airports: pd.DataFrame
        Pandas DataFrame containing list of dictionaries from airports.yaml
    routes: pd.DataFrame
        Pandas DataFrame containing list of dictionaries from routes.yaml
    question: str
        String that specifies which question from 1-5 is being asked
    graph_type: str
        String that specifies what type of graph should be created
    """
    if question == "q1":
        solve_Q1(
            airlines, 
            airports, 
            routes, 
            graph_type
        )
    elif question == "q2":
        solve_Q2(
            airlines, 
            airports, 
            routes, 
            graph_type
        )
    elif question == "q3":
        solve_Q3(
            airlines, 
            airports, 
            routes, 
            graph_type
        )
    elif question == "q4":
        solve_Q4(
            airlines,
            airports, 
            routes, 
            graph_type
        )
    elif question == "q5":
        solve_Q5(
            airlines, 
            airports, 
            routes, 
            graph_type
        )
    
    
def solve_Q1(airlines: pd.DataFrame, airports: pd.DataFrame, routes: pd.DataFrame, graph_type: str):
    """Generates a csv file containing top 20 airlines that offer the greatest number of routes 
       to Canada, and calls function to generate a graph of the given graph type

    Parameters
    ----------
    airlines: pd.DataFrame
        Pandas DataFrame containing list of dictionaries from airlines.yaml
    airports: pd.DataFrame
        Pandas DataFrame containing list of dictionaries from airports.yaml
    routes: pd.DataFrame
        Pandas DataFrame containing list of dictionaries from routes.yaml
    graph_type: str
        String that specifies what type of graph should be created
    """
    merged_routes_airports = pd.merge(
        routes, 
        airports, 
        left_on='route_to_airport_id', 
        right_on='airport_id'
    )
    merged_routes_airports_airlines = pd.merge(
        merged_routes_airports, 
        airlines, 
        left_on='route_airline_id', 
        right_on='airline_id'
    )
    # Sort merged airline airports for each route by country, and make a df for most frequent airlines
    png_routes = merged_routes_airports_airlines[merged_routes_airports_airlines['airport_country'] == 'Canada']
    top_airlines = png_routes['airline_name'].value_counts().reset_index()
    top_airlines.columns = ['airline_name', 'statistic']

    top_airlines = pd.merge(
        top_airlines, airlines[['airline_name', 'airline_icao_unique_code']]
        , on='airline_name', 
        how='left'
    )

    # Format strings into format specified in test cases
    top_airlines['subject'] = top_airlines.apply(
        lambda x: f"{x['airline_name']} ({x['airline_icao_unique_code']})"
        , axis=1
    )

    # Get top 20 airlines and print to .csv file
    top_20_airlines = top_airlines.sort_values(
        by=['statistic', 'airline_name'], 
        ascending=[False, True]
    ).head(20)
    top_20_airlines[['subject', 'statistic']].to_csv('q1.csv', index=False)

    if(graph_type=='pie'):
        pie_graph(
            top_20_airlines, 
            'q1.pdf', 
            'Top 20 Airlines with Canadian routes'
        )
    elif(graph_type=='bar'):
        bar_graph(
            top_20_airlines, 
            'q1.pdf', 
            'Top 20 Airlines with Canadian routes', 
            'Subject', 
            'Number of Routes'
        )       


def solve_Q2(airlines: pd.DataFrame, airports: pd.DataFrame, routes: pd.DataFrame, graph_type: str):
    """Generates a csv file containing the top 30 countries with least appearances as 
       destination country in routes.yaml, and calls function to generate a graph of 
       the given graph type

    Parameters
    ----------
    airlines: pd.DataFrame
        Pandas DataFrame containing list of dictionaries from airlines.yaml
    airports: pd.DataFrame
        Pandas DataFrame containing list of dictionaries from airports.yaml
    routes: pd.DataFrame
        Pandas DataFrame containing list of dictionaries from routes.yaml
    graph_type: str
        String that specifies what type of graph should be created
    """
    merged_routes_airports = pd.merge(
        routes, 
        airports, 
        left_on='route_to_airport_id', 
        right_on='airport_id'
    )

    # Creat a df out of the airport countries that appear most frequently in routes
    country_counts = merged_routes_airports['airport_country'].value_counts().reset_index()
    country_counts.columns = ['subject', 'statistic']

    least_frequent_countries = country_counts.sort_values(
        by=['statistic', 'subject']
    ).head(30)

    least_frequent_countries.to_csv('q2.csv', index=False)

    if(graph_type=='pie'):
        pie_graph(
            least_frequent_countries, 
            'q2.pdf', 
            '30 Countries with Least Appearances as Destination'
        )
    elif(graph_type=='bar'):
        bar_graph(least_frequent_countries, 
        'q2.pdf', 
        '30 Countries with Least Appearances as Destination', 
        'Subject', 
        'Number of Appearances'
        ) 


def solve_Q3(airlines: pd.DataFrame, airports: pd.DataFrame, routes: pd.DataFrame, graph_type: str):
    """Generates a csv file containing the top 10 destination airports, and calls function to generate
       a graph of the given graph type

    Parameters
    ----------
    airlines: pd.DataFrame
        Pandas DataFrame containing list of dictionaries from airlines.yaml
    airports: pd.DataFrame
        Pandas DataFrame containing list of dictionaries from airports.yaml
    routes: pd.DataFrame
        Pandas DataFrame containing list of dictionaries from routes.yaml
    graph_type: str
        String that specifies what type of graph should be created
    """
    merged_routes_airports = pd.merge(
        routes, 
        airports, 
        left_on='route_to_airport_id', 
        right_on='airport_id'
    )
    destination_airports = merged_routes_airports['airport_name'].value_counts().reset_index()
    destination_airports.columns = ['airport_name', 'statistic']
    final_destination_airports = pd.merge(
        destination_airports, 
        airports[['airport_name','airport_icao_unique_code', 'airport_country', 'airport_city']], 
        on='airport_name', 
        how='left'
    )

    # Creates new df of number of times each destination airport appears in merged list from above
    top_destination_airports = final_destination_airports.sort_values(
        by='statistic', 
        ascending=False
    ).head(10)

    # Format strings into format specified in test cases
    top_destination_airports['subject'] = top_destination_airports.apply(
    lambda x: f"{x['airport_name']} ({x['airport_icao_unique_code']}), {x['airport_city']}, {x['airport_country']}", 
    axis=1
    )
    top_destination_airports[['subject', 'statistic']].to_csv('q3.csv', index=False)

    if(graph_type=='pie'):
        pie_graph(
            top_destination_airports[['subject', 'statistic']], 
            'q3.pdf', 
            'Top 10 Destination Airports'
        )
    elif(graph_type=='bar'):
        bar_graph(
            top_destination_airports[['subject', 'statistic']], 
            'q3.pdf', 
            'Top 10 Destination Airports', 
            'Subject', 
            'Number of Routes'
        ) 


def solve_Q4(airlines: pd.DataFrame, airports: pd.DataFrame, routes: pd.DataFrame, graph_type: str):
    """Generates a csv file containing the top 15 destination cities, and calls function to generate
       a graph of the given graph type

    Parameters
    ----------
    airlines: pd.DataFrame
        Pandas DataFrame containing list of dictionaries from airlines.yaml
    airports: pd.DataFrame
        Pandas DataFrame containing list of dictionaries from airports.yaml
    routes: pd.DataFrame
        Pandas DataFrame containing list of dictionaries from routes.yaml
    graph_type: str
        String that specifies what type of graph should be created
    """
    merged_routes_airports = pd.merge(
        routes, 
        airports, 
        left_on='route_to_airport_id', 
        right_on='airport_id'
    )
    # Df created with a count for each time a city appears in the route airport df
    destination_city = merged_routes_airports[['airport_city', 'airport_country']].value_counts().reset_index(name='statistic')

    # New df with the top 15 cities
    sorted_destination_city = destination_city.sort_values(
        by=['statistic', 'airport_city', 'airport_country'],
        ascending=[False, True, True]
    ).head(15)

    # Format strings into format specified in test cases
    sorted_destination_city['subject'] = sorted_destination_city.apply(
        lambda x: f"{x['airport_city']}, {x['airport_country']}", 
        axis=1
    )

    sorted_destination_city[['subject', 'statistic']].to_csv('q4.csv', index=False)

    if(graph_type=='pie'):
        pie_graph(
            sorted_destination_city[['subject', 'statistic']], 
            'q4.pdf', 
            'Top 15 Destination Cities'
        )
    elif(graph_type=='bar'):
        bar_graph(
            sorted_destination_city[['subject', 'statistic']], 
            'q4.pdf', 
            'Top 15 Destination Cities', 
            'Subject', 
            'Number of Routes'
        ) 


def solve_Q5(airlines: pd.DataFrame, airports: pd.DataFrame, routes: pd.DataFrame, graph_type: str):
    """Generates a csv file containing the unique top 10 Canadian routes with most difference 
       between the destination altitude and the origin altitude, and calls function to generate
       a graph of the given graph type

       Parameters
       ----------
       airlines: pd.DataFrame
           Pandas DataFrame containing list of dictionaries from airlines.yaml
       airports: pd.DataFrame
           Pandas DataFrame containing list of dictionaries from airports.yaml
       routes: pd.DataFrame
           Pandas DataFrame containing list of dictionaries from routes.yaml
       graph_type: str
           String that specifies what type of graph should be created
    """
    to_airports = pd.merge(
        routes, airports, left_on='route_to_airport_id', right_on='airport_id'
    )

    to_airports = to_airports[
        ['route_from_aiport_id', 'airport_country', 'airport_icao_unique_code', 'airport_altitude']
    ].rename(columns={
        'airport_country': 'dest_airport_country',
        'airport_icao_unique_code': 'dest_airport_icao_unique_code',
        'airport_altitude': 'dest_airport_altitude'
    })

    from_airports = pd.merge(
        to_airports, airports, left_on='route_from_aiport_id', right_on='airport_id'
    )

    from_airports = from_airports.rename(columns={
        'airport_country': 'origin_airport_country',
        'airport_icao_unique_code': 'origin_airport_icao_unique_code',
        'airport_altitude': 'origin_airport_altitude'
    })
    # Created a df from_airports that has the origin and destination information for each flight in routes

    # Creates df of routes that are within Canada
    merged_airports = from_airports[
        (from_airports['dest_airport_country'] == 'Canada') & 
        (from_airports['origin_airport_country'] == 'Canada')
    ]

    merged_airports = merged_airports.copy()

    # Turns the origin and destination altitudes from strings to numbers
    merged_airports['origin_airport_altitude'] = pd.to_numeric(
        merged_airports['origin_airport_altitude'], errors='coerce'
    )
    merged_airports['dest_airport_altitude'] = pd.to_numeric(
        merged_airports['dest_airport_altitude'], errors='coerce'
    )

    merged_airports['statistic'] = (
        merged_airports['origin_airport_altitude'] - 
        merged_airports['dest_airport_altitude']
    ).abs()
    # Format strings into format specified in test cases
    merged_airports['subject'] = merged_airports.apply(
        lambda x: f"{x['origin_airport_icao_unique_code']}-{x['dest_airport_icao_unique_code']}", axis=1
    )

    merged_airports = merged_airports.drop_duplicates(subset='subject')
    sorted_merged_airports = merged_airports.sort_values(
        by='statistic', ascending=False
    ).head(10)

    sorted_merged_airports[['subject', 'statistic']].to_csv('q5.csv', index=False)

    if graph_type == 'pie':
        pie_graph(
            sorted_merged_airports[['subject', 'statistic']],
            'q5.pdf',
            'Top 10 Canadian Routes with Biggest Altitude Difference'
        )
    elif graph_type == 'bar':
        bar_graph(
            sorted_merged_airports[['subject', 'statistic']],
            'q5.pdf',
            'Top 10 Canadian Routes with Biggest Altitude Difference',
            'Subject',
            'Altitude Difference'
        )


def pie_graph(data: pd.DataFrame, question_number: str, graph_title: str):
    """Creates a pie chart using the passed in data, and saves it to a pdf

    Parameters
    ----------
    data: pd.DataFrame
        A DataFrame with the columns 'subject' and 'statistic'
    question_number: str
        The current question the bar graph is being generated for
    graph_title: str
    """
    data.set_index('subject')['statistic'].plot.pie(
        autopct='%1.1f%%', 
        startangle=140, 
        legend=False, 
        textprops={'fontsize': 5}
    )
    plt.figsize=(24, 16)

    plt.ylabel('')
    plt.title(graph_title, y=1.05)
    plt.axis('equal')

    plt.savefig(question_number)
    plt.close()


def bar_graph(data: pd.DataFrame, question_number: str, graph_title: str, x_axis: str, y_axis: str):
    """Creates a bar graph using the passed in data, and saves it to a pdf

    Parameters
    ----------
    data: pd.DataFrame
        A DataFrame with the columns 'subject' and 'statistic'
    question_number: str
        The current question the bar graph is being generated for
    graph_title: str
    x_axis: str
        Label for x-axis
    y_axis: str
        Label for y-axis   
    """
    data.set_index('subject', inplace=True)
    ax = data['statistic'].plot.bar(
        legend=False, 
        figsize=(10, 10), 
        color='blue'
    )

    plt.ylabel(y_axis)
    plt.xlabel(x_axis)
    plt.title(graph_title, y=1.05)
    plt.xticks(rotation=90, ha='right', fontsize=8)
    plt.tight_layout()

    plt.savefig(question_number)
    plt.close()


def format_args(input: str) -> str:
    """
    Splits the command line argument by the "=" symbol to isolate the value.

    Parameters
    ----------
    input : str
        The command line argument in the form of --OPTION="value".

    Returns
    -------
    str
        The isolated value from the command line argument, e.g., "value".
    """
    sorted = input.split("=")
    return sorted[1]


def main() -> None:
    """Formats arguments from command line, then loads airline data and calls solve function"""
    for x in range(1, 6):
        sys.argv[x] = format_args(sys.argv[x])

    #load yaml files
    with open(sys.argv[1], 'r') as file:
        yaml_airlines: Any = yaml.safe_load(file)
    with open(sys.argv[2], 'r') as file:
        yaml_airports: Any = yaml.safe_load(file)
    with open(sys.argv[3], 'r') as file:
        yaml_routes: Any = yaml.safe_load(file)

    # Loading individual data for pandas dataframe
    airlines_list = yaml_airlines['airlines']
    airports_list = yaml_airports['airports']
    routes_list = yaml_routes['routes']

    solve(pd.DataFrame(airlines_list), pd.DataFrame(airports_list), pd.DataFrame(routes_list), sys.argv[4], sys.argv[5])


if __name__ == '__main__':
    main()