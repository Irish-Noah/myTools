# jsonFieldEditor.py
# At work we change json 'policies' all the time, having a plan specific editor is really helpful

import json
import os

def data_editor(data, old_source, new_source, signals): 
	flags = ["ignore_E#x","persist-ref"]
	for element in data: 
		try:
			if element['param'] in signals:
				element['flags'] = flags
			#print(element)
		except KeyError:
			pass
			
	return data

def data_editor_source(data, old_source, new_source, signals): 
	for element in data: 
		if element['source'] == old_source:
			if element['param'] in signals:
				element['source'] = new_source
	return data

def filter_editor(filters, old_source, new_source): 
	signals = []
	for element in filters[0]['operands'][2]['operands']:
		if element['source'] == old_source:
			element['source'] = new_source
			if 'BHCAN' not in element['param'] and 'CCAN' not in element['param'] and 'FDCAN8' not in element['param']:
				signals.append(element['param'])
	return filters, signals



def main():
	input_path = os.path.join(os.path.dirname(__file__), 'input.json')
	output_path = os.path.join(os.path.dirname(__file__), 'output.json')

	with open(input_path, 'r') as infile:
		base = json.load(infile)

	plan_to_edit = 4

	signals = ['ENGINE_TEMP_STAT', 'OILPRESSURESTS', 'FUELWATERPRESENTSTS', 'OIL_TEMP_IND_RQ', 'CHKFUELCAP', 'OILLIFELEFT', 'COOLENT_LEVEL_STAT', 'BRAKEFLUIDLEVELSTS', 'EPB_WARN_STAT', 'ELEC_STAB_STAT', 'EPS_STAT', 'ABSFAILSTS', 'AIRBAGFAILSTS', 'AIRBAGLAMP_FAILSTS', 'DAMPING_SYSTEM_STAT', 'TPM_INDLMPONRQ', 'BSS_LT_SRV_RQSTS', 'FCW_SYSTEM_STAT', 'MIL_ONRQ_BPCM', 'TURTLEMODESTS', 'HEV_LMP_RQ', 'HVBATCNTCTRSTAT']

	#base['plans'][plan_to_edit]['filters'], signal_changes = filter_editor(base['plans'][plan_to_edit]['filters'], 'ref', 'persist-ref')
	base['plans'][plan_to_edit]['data'] = data_editor_source(base['plans'][plan_to_edit]['data'], 'ref', 'persist-ref', signals)

	with open(output_path, 'w') as outfile:
		json.dump(base, outfile, indent=2)
	print(f"Output written to {output_path}")

if __name__ == "__main__":
	main()
