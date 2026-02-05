'''
Function purpose: 
    Recursively search a JSON element until the 'operand' key is no longer found.
    Appends the 'param' value to the list provided in the arguments

Args: 
    element -> the JSON block that is being recursively searched for the 'operand' key
    report -> the list that keeps track of all the 'param' values    

Returns:
    None
'''
def operand_diver(element, report):
    if 'operands' in element.keys():
        for nested_signal in element['operands']:
            try:
                report.append(nested_signal['param'])
            except:
                operand_diver(nested_signal, report)