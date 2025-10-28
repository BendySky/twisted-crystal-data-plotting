'''Molecular weight 7OCB'''
mw_7ocb = 293.4

print("Mass 7OCB Desired (in mg): ")
print("(Likely want to use 50.0 mg)")
mass_7ocb = float(input())

print("Enter Molecular Weight of Dye:")
mw_dye = float(input())

print("Enter Weighed Mass of Chromophore:")
mass_cr = float(input())

print("Use Custom Scale Factors? (Y/n)")
cust_scale = input()

'''
if custom scale factor needed, change in scale_factor function
-- scale_fac_custom --
'''


def scale_factor(custom='n'):

    '''Convert MW to mass to get mass scale factor'''
    '''1:10000 Compound: Dye is Standard ratio'''
    scale_fact = (mw_7ocb*10000)/(mw_dye*1)
    if custom == 'n':
        scale_factors = [scale_fact, scale_fact/10, scale_fact/100, scale_fact/1000]
    elif custom == 'y':
        ## THESE VALUES CAN BE CHANGED AS NEEDED ##
        scale_fac_custom = [(scale_fact/100)/1, (scale_fact/100)/2, (scale_fact/100)/3, (scale_fact/100)/4]
        scale_factors = scale_fac_custom
    return scale_factors


def dye_init():

    '''Volume of Stock Solution (in Liters)'''
    vol_solution = .0050  # volume of solvent in L
    scale_fac = scale_factor(custom=cust_scale)  # scale factor stored as a list

    # convert mg of input to "mol solute / Liter solvent"
    molarity_cr_stock = ((mass_cr / 1000) / mw_dye) / vol_solution

    # Molarity of stock solution is listed in milliMolar
    print("Molarity Stock Solution:", molarity_cr_stock * 1000, "mM in 5 mL Solvent\n")
    print("\nScale Factors:\n")

    for i in range(len(scale_fac)):
        if cust_scale == 'n':
            # Scale factor (highest to lowest
            print(f"Scale Factor: {10 ** -i * 10000}:1")
            print(scale_fac[i], "\n")
        elif cust_scale == 'y':
            ### Scale Factor 100 ###
            print(f'Scale Factor: 100:{i+1}')
            print(scale_fac[i])

    if cust_scale == 'y':
        print("\nCUSTOM SCALE FACTORS USED")
    else:
        print("\nStandard Scale Factors Used")
    return molarity_cr_stock


def matrl_dye_ratio():

    scales = scale_factor(custom=cust_scale)

    mass_chromo = [] # store scale factors as a list
    for i in range(len(scales)):
        mass_chromo.append((mass_7ocb/1000)/scales[i])
        print("Mass chromophore: ", mass_chromo[i]*10**6, 'µg in',mass_7ocb,'mg 7OCB')
    # dye ratios 7OCB:chromophore (in grams)
    print('\n')
    return mass_chromo


def dye_diln():

    chromo_stock = dye_init()#[0] #Molarity of stock solution
    mass_chromo = matrl_dye_ratio() #Mass of Chromophores with appropriate scale factor
    mol_chromo = []
    mol_from_stock = []
    #convert mass scale factor to moles
    for i in range(len(mass_chromo)):
        mol_chromo.append(mass_chromo[i]/mw_dye)
    # Calculate the volume of stock solution to add to "dye" crystal
    for j in range(len(mol_chromo)):
        mol_from_stock.append((mol_chromo[j] * 1000 * 1) / chromo_stock)

    for i in range(len(mol_from_stock)):
        print(f"Dilution {10**-i*10000}:1 –", mol_from_stock[i], f"mL Dye from 5 mL of {chromo_stock*1000} mM stock solution")
        #print(mol_from_stock[i])
        print(f"Moles of Dye added:", mol_chromo[i], "mol\n")

    return mol_chromo


dilutions = dye_diln()
