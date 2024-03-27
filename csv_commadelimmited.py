import csv   
import pandas as pd 
from pandas import DataFrame


with open('freedom_index.csv', 'r') as csv_file:
        csv_reader=csv.reader(csv_file)

        for line in csv_reader:
            print(line)
