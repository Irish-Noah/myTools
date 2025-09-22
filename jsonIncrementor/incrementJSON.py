# incrementJSON.py
# Reads input.json, increments the 'name' field by 1, writes to output.json
import json
import os

def main():
	input_path = os.path.join(os.path.dirname(__file__), 'input.json')
	output_path = os.path.join(os.path.dirname(__file__), 'output.json')

	with open(input_path, 'r') as infile:
		base = json.load(infile)

	master = {
		"data": [base]
	}

	# Increment the 'name' field (assume it's a string representing an int)
	for x in range(0, 109):
		try:
			increment = master['data'][-1].copy()
			increment['param'] = increment['param'].split('-')[0] + '-' + str(int(increment['param'].split('-')[1]) + 1)
			master['data'].append(increment)
			
		except (KeyError, ValueError, TypeError):
			print("Error: 'name' field missing or not convertible to int.")
			return

	with open(output_path, 'w') as outfile:
		json.dump(master, outfile, indent=2)
	print(f"Output written to {output_path}")

if __name__ == "__main__":
	main()
