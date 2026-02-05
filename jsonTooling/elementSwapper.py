'''
Function purpose:
    Iterate over a list of json objects and replace the 'source' value with a new 'source' value

Args:
    data -> list of json objects
	old_source -> target keyword to be replaced
	new_source -> new value for the target to be replaced with

Returns:
    data -> list of edited json objects
'''
def data_editor_source(data, old_source, new_source): 
	for element in data: 
		if element['source'] == old_source:
			element['source'] = new_source
	return data