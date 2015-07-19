from urllib import request
import pandas as pd

# Retrieve the webpage as a string

def get_dataset_as_csv(url):
	response = request.urlopen(url)
	csv = response.read()
	return csv

def get_dataframe(url):
	csv = get_dataset_as_csv(url)
	return pd.DataFrame.from_csv(csv, sep=",", parse_dates=False)


def test_get_dataset_as_csv():
	url = 'http://vincentarelbundock.github.io/Rdatasets/csv/datasets/AirPassengers.csv'	
	csv = get_dataset_as_csv(url)
	print(csv)