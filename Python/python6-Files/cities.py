# Read data from csv file cities.csv
# Calculate and the statistics:
# - mean, variance, stdev for cities with population > 1000000
import csv 
import pprint
import statistics as s

def csv_dictionary(csvfile):
    with open(csvfile,"r", encoding="utf8") as f:
        d = dict(filter(None, csv.reader(f)))
    return d

def matchingcities(cities):
    matches = {}
    for key in cities.keys():
        if len(cities[key].strip()) > 0:
            if int(cities[key]) >= 1000000:
                matches.update({key:cities[key]})
    return matches, len(matches.keys())

def stats(population):
    mean = s.mean(population)
    variance = s.variance(population)
    stdv = s.stdev(population)
    return mean, variance, stdv

def citiesstatistics():
    csvfile = input("CSV File: ")
    cities  = csv_dictionary(csvfile)
    pp = pprint.PrettyPrinter(indent=2,width=40)
    matches, count = matchingcities(cities)
    pp.pprint(matches)
    print(f'Cities with population greater than 1 million: {count}')
    mean, variance, stdv = stats(list(map(int,matches.values())))
    print(f'Mean = {mean:.3f}')
    print(f'Variance = {variance:.3f}')
    print(f'Standard Deviation = {stdv:.3f}')
citiesstatistics()