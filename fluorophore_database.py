import pandas as pd
import pubchempy
import requests
from rdkit import Chem
from rdkit.Chem import Descriptors

main_path = '/Applications/Desktop/nyuResearch/liquid_crystals/Organic_Dyes'
db_file = f'{main_path}/DB for chromophore_Sci_Data_rev02.csv'
fl_db = pd.read_csv(db_file, header=0)
#print(fl_db.iloc[1])

'''SMILES to IUPAC Function'''
# Database of SMILES to IUPAC Name
CACTUS = 'https://cactus.nci.nih.gov/chemical/structure/{0}/{1}'
#Cactus
def smiles_to_iupac(smiles):
    rep = "iupac_name"
    url = CACTUS.format(smiles, rep)
    response = requests.get(url)
    response.raise_for_status()
    return response.text


'''Find Chromophores with Absorption in 400-800 nm Wavelength'''
bandpass = fl_db.loc[(fl_db['Absorption max (nm)'] > 415) & (fl_db['Absorption max (nm)'] < 750), 'Absorption max (nm)']
df_bp = fl_db[fl_db['Absorption max (nm)'].isin(bandpass)]

'''Drop Duplicate References'''
dups = df_bp.drop_duplicates('Reference')
dups.to_csv(f'{main_path}/concat_chromophore_db_no_dups.csv', index=True)

'''Convert SMILES to IUPAC (Takes a WHILE)'''
print('Convert to IUPAC?[y/n]:')
prompt1 = input()

if prompt1 == 'y':
    ''' Convert SMILES to IUPAC Name '''
    print('Converting SMILES to IUPAC')
    print('Take a Coffee Break. This will take a while..')
    iupac_nm = []
    for i in dups['Chromophore']:
        compounds = pubchempy.get_compounds(i, namespace='smiles')
        match = compounds[0]
        print(match.iupac_name)
        iupac_nm.append(match.iupac_name)


dups.to_csv(f'{main_path}/IUPAC_concat_chromophore_db_no_dups.csv', index=True)