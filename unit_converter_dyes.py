import numpy as np

'''Molecular weight 7OCB'''
mw_7ocb = 293.4

print("Mass 7OCB Desired (in mg): ")
print("(Likely want to use 50.0 mg)")
mass_7ocb = float(input())

print("Enter Molecular Weight of Dye:")
dye_mw_inp = float(input())


def scale_factor():

    mw_dye = dye_mw_inp
    '''Convert MW to mass to get mass scale factor'''
    scale_fact = (mw_7ocb*10000)/(mw_dye*1)

    scale_factors = [scale_fact, scale_fact/10, scale_fact/100, scale_fact/1000]

    return scale_factors, mw_dye


def dye_init():

    '''Volume of Stock Solution (in Liters)'''
    vol_solution = .0050 #volume of solvent in L

    mw_cr = scale_factor()[1] # molecular weight of dye/chromophore
    scale_fac = scale_factor()[0] #scale factor stored as a list

    print("Weighed Mass of Dye/Chromophore (in mg):")
    mass_cr = float(input())
    # convert mg of input to "mol solute / Liter solvent"
    molarity_cr_stock = ((mass_cr/1000)/mw_cr)/vol_solution

    # Molarity of stock solution is listed in milliMolar
    print("Molarity Stock Solution:", molarity_cr_stock*1000, "mM in 5 mL Solvent\n")
    print("\nScale Factors:\n")

    for i in range(len(scale_fac)):
        # Scale factor (highest to lowest
        print(f"Scale Factor: {10**-i*10000}:1")
        print(scale_fac[i],"\n")

    return molarity_cr_stock#, mw_cr

def matrl_dye_ratio():

    scales = scale_factor()[0]

    mass_chromo = [] # store scale factors as a list
    for i in range(len(scales)):
        mass_chromo.append((mass_7ocb/1000)/scales[i])
        print("Mass chromophore: ", mass_chromo[i]*10**6, 'µg')
    # dye ratios 7OCB:chromophore (in grams)
    print('\n')
    return mass_chromo

def dye_diln():

    chromo_stock = dye_init()#[0] #Molarity of stock solution
    mw_chromo = scale_factor()[1] # Molecular weight Chromophore
    mass_chromo = matrl_dye_ratio() #Mass of Chromophores with appropriate scale factor
    mol_chromo = []
    mol_from_stock = []
    #convert mass scale factor to moles
    for i in range(len(mass_chromo)):
        mol_chromo.append(mass_chromo[i]/mw_chromo)
    # Calculate the volume of stock solution to add to "dye" crystal
    for j in range(len(mol_chromo)):
        mol_from_stock.append((mol_chromo[j] * 1000 * 1) / chromo_stock)

    for i in range(len(mol_from_stock)):
        print(f"Dilution {10**-i*10000}:1 –", mol_from_stock[i], f"mL Dye from 5 mL of {chromo_stock*1000} mM stock solution")
        #print(mol_from_stock[i])
        print(f"Moles of Dye added:", mol_chromo[i], "mol\n")

    return




#matrl_dye_ratio()
#test = dye_init()

dilutions = dye_diln()
