import os
import json
from pathlib import Path

DIR_PATH = './'

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
    output_path = os.path.join(os.path.dirname(__file__), 'result2.json')
    found_signals = {}
    signals = ["ETAT_AAS_AR", "ETAT_AAS_AV","ETAT_FONCT_LVV_RVV", "DMD_ALLUMAGE_FA","DMD_ALLUM_AFIL", "ESPACT","REGUL_ABR", "FRPK","FONCT_ACT_LVV_RVV", "LKA_LEFT_LINE_INFO","LKA_RIGHT_LINE_INFO","ETAT_SAM","VIT_A_AFFICHER_ILV","ALLUM_FLECHE", "COUPLE_REEL","REGIME_MOTEUR","MODE_BVA_BVMP","RAP_BV_ENGAGE_MECA","VOLONTE_COND","VITV", "VITESSE_LACET","ACCEL_LAT","ACCEL_LONGI_ROUES","ANGLE_VOLANT","PRESSION_MAITRE_CYL","CONTACT_FREIN1","ETAT_GMP_HYB","PEM_SPEED_HD","FEUX_ABAR","FEUX_ABAV","CONSO_INSTANTANEE","CLIGNO_D","CLIGNO_G","P_TEM_SBR_STATE_COND","P_TEM_SBR_STATE_PASS_AV","ETAT_GMP","RAP_ENGAGE_CALCULE","INFO_CMDM_MODE_VHL","ETAT_PRINCIP_SEV","ETAT_JOUR_NUIT","ETAT_ESSUYAGE","U_BATT_BECB","HV_BATT_INSULATION_RESISTANCE"]
    for subdir, dirs, files in os.walk(DIR_PATH):
        for file in files: 
            try:
                if int(file.replace('.json', '')):
                    found_signals[file] = check_singals_exist(file, signals)
            except:
                continue    
    with open(output_path, 'w') as outfile:
	    json.dump(found_signals, outfile, indent=2)


if __name__ == "__main__":
    main()