import os
import json
from pathlib import Path

DIR_PATH = './x250'

def collect_signals(file):
    report = []
    with open(file, 'r') as fp:
        policy = json.load(fp)
        for plan in policy['plans']: 
            for signal in plan['data']:
                try:
                    report.append(signal['param'])
                except:
                    operand_diver(signal, report)
                
    return report
    

# recursive diver for nested operands 
def operand_diver(element, report):
    if 'operands' in element.keys():
        for nested_signal in element['operands']:
            try:
                report.append(nested_signal['param'])
            except:
                operand_diver(nested_signal, report)



def check_singals_exist(file, signals):
    report = []
    fp = open(file, 'r')
    for signal in signals:
        fp.seek(0)
        for line in fp:
            if signal in line:
                report.append(f'{signal} found in {file}')
    report.append(f'overlap in signals: {len(report)/47}')
    return report

def main(): 
    output_path = os.path.join(os.path.dirname(__file__), 'x250result.json')

    master_collection = {}

    found_signals = {}
    # J4U_signals = ["ETAT_AAS_AR", "ETAT_AAS_AV","ETAT_FONCT_LVV_RVV", "DMD_ALLUMAGE_FA","DMD_ALLUM_AFIL", "ESPACT","REGUL_ABR", "FRPK","FONCT_ACT_LVV_RVV", "LKA_LEFT_LINE_INFO","LKA_RIGHT_LINE_INFO","ETAT_SAM","VIT_A_AFFICHER_ILV","ALLUM_FLECHE", "COUPLE_REEL","REGIME_MOTEUR","MODE_BVA_BVMP","RAP_BV_ENGAGE_MECA","VOLONTE_COND","VITV", "VITESSE_LACET","ACCEL_LAT","ACCEL_LONGI_ROUES","ANGLE_VOLANT","PRESSION_MAITRE_CYL","CONTACT_FREIN1","ETAT_GMP_HYB","PEM_SPEED_HD","FEUX_ABAR","FEUX_ABAV","CONSO_INSTANTANEE","CLIGNO_D","CLIGNO_G","P_TEM_SBR_STATE_COND","P_TEM_SBR_STATE_PASS_AV","ETAT_GMP","RAP_ENGAGE_CALCULE","INFO_CMDM_MODE_VHL","ETAT_PRINCIP_SEV","ETAT_JOUR_NUIT","ETAT_ESSUYAGE","U_BATT_BECB","HV_BATT_INSULATION_RESISTANCE"]
    for subdir, dirs, files in os.walk(DIR_PATH):
        for file in files: 
            master_collection[file.replace('.json', '')] = collect_signals(os.path.join('x250', file))

    # for each signal in each policy, compare to all other signals and store in an object like {'signal_name': [policy_id, policy_id, ...]}
    for policy in master_collection: 
        for signal in master_collection[policy]:
            for policy_duped in master_collection:
                for signal_duped in master_collection[policy_duped]:
                    if signal == signal_duped:
                        if signal in found_signals.keys():
                            if policy_duped not in found_signals[signal]:
                                found_signals[signal].append(policy_duped)
                        else:
                            found_signals[signal] = [policy_duped]



    

    # j4u code
    '''for subdir, dirs, files in os.walk(DIR_PATH):
        for file in files: 
            try:
                if int(file.replace('.json', '')):
                    found_signals[file] = check_singals_exist(file, signals)
            except:
                continue    '''
    with open(output_path, 'w') as outfile:
	    json.dump(found_signals, outfile, indent=2)


if __name__ == "__main__":
    main()