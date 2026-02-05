import os
import json

DIR_PATH = './<subdir>'

'''
Function purpose: 
    Template function for exploring the contents of the current json file

Args: 
    file -> the file that will be manipulated in some way
    

Returns:
    Any or None, depending on function use case
'''
def function_call(file):
    with open(file, 'r') as fp:
        policy = json.load(fp)
        fp.close()


'''
Function purpose: 
    Typical entry point for the program.
    Opens the subdir path and iterates over the json files within it

Args:
    None

Returns:
    None, writes data to a json file indicated by 'output_path'
'''
def main(): 
    output_path = os.path.join(os.path.dirname(__file__), '<filename>.json')

    output_json = {}

    for subdir, dirs, files in os.walk(DIR_PATH):
        for file in files: 
            function_call(os.path.join('<subdir>', file))

    with open(output_path, 'w') as outfile:
	    json.dump(output_json, outfile, indent=2)