import re

__get_response_string_regex = re.compile('.*Rs=(.*)\|')

def get_response_string(response_column):
	response = ''
	match = __get_response_string_regex.match(response_column)
	if (match):
		response = match.group(1)
	return response

def get_column(row):
	get_response_string(row['_raw'])