

def main():
    # Get a chemical formula for a molecule from the user.
    chemical_formula = input('\033cEnter the molecular forumla of the sample: ')

    # Get the mass of a chemical sample in grams from the user.
    sample_mass = float(input('Enter the mass in grams of the sample: '))

    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    periodic_table = make_periodic_table()

    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    forumla_list = parse_formula(chemical_formula, periodic_table)

    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    molar_mass = compute_molar_mass(forumla_list, periodic_table)

    # Compute the number of moles in the sample.
    number_of_moles = sample_mass / molar_mass
    
    # call the function to get the name of the molecular formula
    formula_details = get_formula_name(chemical_formula)
    
    print (f'\nGiven Molar Mass of {chemical_formula}:\n' +
            f'{formula_details[0]}, {formula_details[1]}\n')
    
    # Print the molar mass.
    print (f'{molar_mass:.5f} grams/mole')
    
    # Print the number of moles.
    print (f'{number_of_moles:.5f} moles')
    

def make_periodic_table():
    '''Create and return 
    a compound list of the
    Periodic Table of Elements
    With their Atomic Mass
    Parameters: None
    
    Return: A compound list of
        the Periodic Table of Elements
    '''
    # Indexes of list:
    CHEMICAL_SYMBOL = 0
    ELEMENT_NAME = 1
    ATOMIC_MASS = 2
    
    periodic_table_dict = {
        # Symbol: [Element Name, Atomic Mass]
        "Ac": ["Actinium", 227],
        "Ag": ["Silver", 107.8682],
        "Al": ["Aluminum", 26.9815386],
        "Ar": ["Argon", 39.948],
        "As": ["Arsenic", 74.9216],
        "At": ["Astatine", 210],
        "Au": ["Gold", 196.966569],
        "B": ["Boron", 10.811],
        "Ba": ["Barium", 137.327],
        "Be": ["Beryllium", 9.012182],
        "Bi": ["Bismuth", 208.9804],
        "Br": ["Bromine", 79.904],
        "C": ["Carbon", 12.0107],
        "Ca": ["Calcium", 40.078],
        "Cd": ["Cadmium", 112.411],
        "Ce": ["Cerium", 140.116],
        "Cl": ["Chlorine", 35.453],
        "Co": ["Cobalt", 58.933195],
        "Cr": ["Chromium", 51.9961],
        "Cs": ["Cesium", 132.9054519],
        "Cu": ["Copper", 63.546],
        "Dy": ["Dysprosium", 162.5],
        "Er": ["Erbium", 167.259],
        "Eu": ["Europium", 151.964],
        "F": ["Fluorine", 18.9984032],
        "Fe": ["Iron", 55.845],
        "Fr": ["Francium", 223],
        "Ga": ["Gallium", 69.723],
        "Gd": ["Gadolinium", 157.25],
        "Ge": ["Germanium", 72.64],
        "H": ["Hydrogen", 1.00794],
        "He": ["Helium", 4.002602],
        "Hf": ["Hafnium", 178.49],
        "Hg": ["Mercury", 200.59],
        "Ho": ["Holmium", 164.93032],
        "I": ["Iodine", 126.90447],
        "In": ["Indium", 114.818],
        "Ir": ["Iridium", 192.217],
        "K": ["Potassium", 39.0983],
        "Kr": ["Krypton", 83.798],
        "La": ["Lanthanum", 138.90547],
        "Li": ["Lithium", 6.941],
        "Lu": ["Lutetium", 174.9668],
        "Mg": ["Magnesium", 24.305],
        "Mn": ["Manganese", 54.938045],
        "Mo": ["Molybdenum", 95.96],
        "N": ["Nitrogen", 14.0067],
        "Na": ["Sodium", 22.98976928],
        "Nb": ["Niobium", 92.90638],
        "Nd": ["Neodymium", 144.242],
        "Ne": ["Neon",	20.1797],
        "Ni": ["Nickel", 58.6934],
        "Np": ["Neptunium", 237],
        "O": ["Oxygen", 15.9994],
        "Os": ["Osmium", 190.23],
        "P": ["Phosphorus", 30.973762],
        "Pa": ["Protactinium", 231.03588],
        "Pb": ["Lead", 207.2],
        "Pd": ["Palladium", 106.42],
        "Pm": ["Promethium", 145],
        "Po": ["Polonium", 209],
        "Pr": ["Praseodymium", 140.90765],
        "Pt": ["Platinum", 195.084],
        "Pu": ["Plutonium", 244],
        "Ra": ["Radium", 226],
        "Rb": ["Rubidium", 85.4678],
        "Re": ["Rhenium", 186.207],
        "Rh": ["Rhodium", 102.9055],
        "Rn": ["Radon", 222],
        "Ru": ["Ruthenium", 101.07],
        "S": ["Sulfur", 32.065],
        "Sb": ["Antimony", 121.76],
        "Sc": ["Scandium", 44.955912],
        "Se": ["Selenium", 78.96],
        "Si": ["Silicon", 28.0855],
        "Sm": ["Samarium", 150.36],
        "Sn": ["Tin", 118.71],
        "Sr": ["Strontium", 87.62],
        "Ta": ["Tantalum", 180.94788],
        "Tb": ["Terbium", 158.92535],
        "Tc": ["Technetium", 98],
        "Te": ["Tellurium", 127.6],
        "Th": ["Thorium", 232.03806],
        "Ti": ["Titanium", 47.867],
        "Tl": ["Thallium", 204.3833],
        "Tm": ["Thulium", 168.93421],
        "U": ["Uranium", 238.02891],
        "V": ["Vanadium", 50.9415],
        "W": ["Tungsten", 183.84],
        "Xe": ["Xenon", 131.293],
        "Y": ["Yttrium", 88.90585],
        "Yb": ["Ytterbium", 173.054],
        "Zn": ["Zinc", 65.38],
        "Zr": ["Zirconium",	91.224]
    }
    
    return periodic_table_dict

class FormulaError(ValueError):
    """FormulaError is the type of error that
    parse_formula will raise if a formula is invalid.
    """

def parse_formula(formula, periodic_table_dict):
    """Convert a chemical formula for a molecule into a compound list
    that stores the quantity of atoms of each element in the molecule.
    For example, this function will convert "H2O" to [["H", 2], ["O", 1]]
    and "PO4H2(CH2)12CH3" to [["P", 1], ["O", 4], ["H", 29], ["C", 13]]

    Parameters
        formula: a string that contains a chemical formula
        periodic_table_dict: the compound dictionary returned
            from make_periodic_table
    Return: a compound list that contains chemical symbols and
        quantities like this [["Fe", 2], ["O", 3]]
    """
    assert isinstance(formula, str), \
        "wrong data type for parameter formula; " \
        f"formula is a {type(formula)} but must be a string"
    assert isinstance(periodic_table_dict, dict), \
        "wrong data type for parameter periodic_table_dict; " \
        f"periodic_table_dict is a {type(periodic_table_dict)} " \
        "but must be a dictionary"

    def parse_quant(formula, index):
        quant = 1
        if index < len(formula) and formula[index].isdecimal():
            start = index
            index += 1
            while index < len(formula) and formula[index].isdecimal():
                index += 1
            quant = int(formula[start:index])
        return quant, index

    def get_quant(elems, symbol):
        return 0 if symbol not in elems else elems[symbol]

    def parse_r(formula, index, level):
        start_index = index
        start_level = level
        elem_dict = {}
        while index < len(formula):
            ch = formula[index]
            if ch == "(":
                group_dict, index = parse_r(formula, index+1, level+1)
                quant, index = parse_quant(formula, index)
                for symbol in group_dict:
                    prev = get_quant(elem_dict, symbol)
                    elem_dict[symbol] = prev + group_dict[symbol] * quant
            elif ch.isalpha():
                symbol = formula[index:index+2]
                if symbol in periodic_table_dict:
                    index += 2
                else:
                    symbol = formula[index:index+1]
                    if symbol in periodic_table_dict:
                        index += 1
                    else:
                        raise FormulaError(
                            "invalid formula, unknown element symbol:",
                            formula, index)
                quant, index = parse_quant(formula, index)
                prev = get_quant(elem_dict, symbol)
                elem_dict[symbol] = prev + quant
            elif ch == ")":
                if level == 0:
                    raise FormulaError(
                        "invalid formula, unmatched close parenthesis:",
                        formula, index)
                level -= 1
                index += 1
                break
            else:
                if ch.isdecimal():
                    # Decimal digit not preceded by an
                    # element symbol or close parenthesis
                    message = "invalid formula:"
                else:
                    # Illegal character: [^()0-9a-zA-Z]
                    message = "invalid formula, illegal character:"
                raise FormulaError(message, formula, index)
        if level > 0 and level >= start_level:
            raise FormulaError(
                "invalid formula, unmatched open parenthesis:",
                formula, start_index - 1)
        return elem_dict, index

    # Return the compound list of element symbols and
    # quantities. Each element in the compound list
    # will be a list in this form: ["symbol", quantity]
    elem_dict, _ = parse_r(formula, 0, 0)
    return list(elem_dict.items())


# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary returned
            from make_periodic_table.
        Return: the total molar mass of all the elements in
            symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # For each list in the compound symbol_quantity_list:
    # Separate the list into symbol and quantity.
    
    molar_mass = 0
    
    for symbol, quantity in symbol_quantity_list:
    
        if symbol in periodic_table_dict:
            
            # Get the atomic mass for the symbol from the dictionary.
            # atomic_detail = periodic_table_dict[symbol]
            # atomic_mass = atomic_detail[ATOMIC_MASS_INDEX]
            
            atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
            
            # Multiply the atomic mass by the quantity.
            product = atomic_mass * quantity
            
            # Add the product into the total molar mass.
            molar_mass += product
            
        
        else:
            print ('No such value')
        
    # Return the total molar mass.
    return molar_mass

def get_formula_name(formula):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".
    """

    known_molecules_dict = {
        # "Molecular formula":["Compound name","Molecular weight"]
        "CH3COOH":["Acetic acid","60.052 g/mol"],
        "HCl":["Hydrochloric acid","36.458 g/mol"],
        "H2SO4":["Sulfuric acid","98.072 g/mol"],
        "NH3":["Ammonia","17.031 g/mol"],
        "HNO3":["Nitric acid","63.012 g/mol"],
        "H3PO4":["Phosphoric acid","97.994 g/mol"],
        "Na3PO4":["Sodium phosphate","119.976 g/mol"],
        "CaCO3":["Calcium carbonate","100.086 g/mol"],
        "(NH4)2SO4":["Ammonium sulfate","132.134 g/mol"],
        "H2CO3":["Carbonic acid","62.024 g/mol"],
        "NaHCO3":["Sodium bicarbonate","84.0066 g/mol"],
        "NaOH":["Sodium hydroxide","39.997 g/mol"],
        "Ca(OH)2":["Calcium hydroxide","74.092 g/mol"],
        "C2H5OH":["Ethanol","46.069 g/mol"],
        "HBr":["Hydrobromic acid","80.912 g/mol"],
        "HNO2":["Nitrous acid","47.013 g/mol"],
        "KOH":["Potassium hydroxide","56.11 g/mol"],
        "AgNO3":["Silver nitrate","169.872 g/mol"],
        "Na2CO3":["Sodium carbonate","105.988 g/mol"],
        "NaCl":["Sodium chloride","58.44 g/mol"],
        "(C6H10O5)n":["Cellulose","162.1406 g/mol"],
        "Mg(OH)2":["Magnesium hydroxide","58.319 g/mol"],
        "CH4":["Methane","16.043 g/mol"],
        "NO2":["Nitrogen dioxide","30.006 g/mol"],
        "NaNO3":["Sodium nitrate","84.994 g/mol"],
        "H2SO3":["Sulfurous acid","82.073 g/mol"],
        "Al2(SO4)3":["Aluminium sulfate","342.15 g/mol"],
        "Al2O3":["Aluminum oxide","101.96 g/mol"],
        "NH4NO3":["Ammonium nitrate","80.043 g/mol"],
        "(NH4)3PO4":["Ammonium phosphate","132.056 g/mol"],
        "Ba(OH)2":["Barium hydroxide","171.341 g/mol"],
        "CCl4":["Carbon tetrachloride","153.811 g/mol"],
        "C6H8O7":["Citric acid","192.123 g/mol"],
        "HCN":["Hydrocyanic acid","27.026 g/mol"],
        "C7H6O3":["Salicylic Acid","138.121 g/mol"],
        "HI":["Hydroiodic acid","127.91 g/mol"],
        "HClO":["Hypochlorous acid","52.457 g/mol"],
        "Fe2O3":["Iron iii oxide","159.687 g/mol"],
        "Mg3(PO4)2":["Magnesium phosphate","262.855 g/mol"],
        "C2H3NaO2":["Sodium acetate","82.0343 g/mol"],
        "Na2SO4":["Sodium sulfate","142.036 g/mol"],
        "C12H22O11":["Sucrose","342.2965 g/mol"],
        "KNO3":["Potassium nitrate","101.102 g/mol"],
        "NH4HCO3":["Ammonium bicarbonate","96.086 g/mol"],
        "NH4Cl":["Ammonium chloride","53.489 g/mol"],
        "NH4OH":["Ammonium hydroxide","35.046 g/mol"],
        "Ca(NO3)2":["Calcium nitrate","164.088 g/mol"],
        "CaO":["Calcium oxide","56.0774 g/mol"],
        "CO":["Carbon monoxide","28.01 g/mol"],
        "Cl2":["Chlorine gas","70.9 g/mol"],
        "C6H6O":["Phenol","94.11 g/mol"],
        "H2O2":["Hydrogen peroxide","34.0147 g/mol"],
        "MgCl2":["Magnesium chloride","95.211 g/mol"],
        "KCl":["Potassium chloride","74.5513 g/mol"],
        "KI":["Potassium iodide","166.0028 g/mol"],
        "SO2":["Sulfur dioxide","64.066 g/mol"],
        "C3H8O3":["Glycerin","92.09 g/mol"],
        "Ba(NO3)2":["Barium nitrate","261.337 g/mol"],
        "C4H6O4Ca":["Calcium acetate","158.17 g/mol"],
        "Fe2O3":["Iron oxide","159.69 g/mol"],
        "K2CO3":["Potassium carbonate","138.205 g/mol"],
        "AgCl":["Silver chloride","143.318 g/mol"],
        "NaI":["Sodium iodide","149.894 g/mol"],
        "Na2O":["Sodium oxide","61.9789 g/mol"],
        "Na2S":["Sodium sulfide","78.0452 g/mol"],
        "Zn(NO3)2":["Zinc nitrate","189.388 g/mol"],
        "C20H14O4":["Phenolphthalein","318.32 g/mol"],
        "Mg(NO3)2":["Magnesium nitrate","148.313 g/mol"],
        "SiO2":["Silicon dioxide","60.083 g/mol"],
        "C3H6O":["Acetone","58.08 g/mol"],
        "C6H6O2":["Hydroquinone","110.11 g/mol"],
        "C5H5N":["Pyridine","79.1 g/mol"],
        "C2H3O2NH4":["Ammonium acetate","77.083 g/mol"],
        "C8H10":["Xylene","106.16 g/mol"],
        "BaSO4":["Barium sulfate","233.38 g/mol"],
        "C6H6":["Benzene","78.11 g/mol"],
        "CrO42-":["Chromate","15.992 g/mol"],
        "C4H8O":["Methyl Ethyl Ketone","72.107 g/mol"],
        "C2HCl3O2":["Trichloroacetic acid","163.38 g/mol"],
        "MgSO4":["Magnesium sulfate","120.361 g/mol"],
        "CH3OH":["Methanol","32.04 g/mol"],
        "O":["Oxygen","Atomic mass 15.999 g/mol"],
        "C16H18ClN3S":["Methylene blue","319.85 g/mol"],
        "Na2SO3":["Sodium sulfite","126.043 g/mol"],
        "SO3":["Sulfur trioxide","80.057 g/mol"],
        "AlPO4":["Aluminum phosphate","121.951 g/mol"],
        "C18H36O2":["Stearic acid","284.484 g/mol"],
        "N2O":["Dinitrogen monoxide","44.013 g/mol"],
        "TiO2":["Titanium dioxide","233.38 g/mol"],
        "C2H3N":["Acetonitrile","41.053 g/mol"],
        "H2C2O4":["Oxalic acid","90.03 g/mol"],
        "K2Cr2O7":["Potassium dichromate","294.185 g/mol"],
        "NaBr":["Sodium bromide","102.894 g/mol"],
        "NaClO":["Sodium hypochlorite","74.439 g/mol"],
        "Zn(CH3COO)2(H2O)2":["Zinc acetate","183.48 g/mol"],
        "ZnCl2":["Zinc chloride","136.286 g/mol"],
        "Zn(OH)2":["Zinc hydroxide","99.424 g/mol"],
        "MgCO3":["Magnesium carbonate","84.313 g/mol"],
        "KClO3":["Potassium chlorate","122.545 g/mol"],
        "N2H4":["Hydrazine","32.0452 g/mol"],
        "C6H8O6":["Ascorbic acid","176.12 g/mol"],
        "C7H6O2":["Benzoic acid","122.12 g/mol"],
        "C6H6O2":["Resorcinol","110.1 g/mol"],
        "Cl2":["Chlorine","70.9 g/mol"],
        "C4H4O4":["Maleic acid","116.072 g/mol"],
        "Na2S2O5":["Sodium metabisulfite","190.107 g/mol"],
        "C2H5NO":["Acetamide","59.068 g/mol"],
        "(Na2O)x·SiO2":["Sodium silicate","122.062 g/mol"],
        "PO43-":["Phosphate","94.9714 g/mol"],
        "CH2Cl2":["Dichloromethane","84.93 g/mol"],
        "CS2":["Carbon Disulfide","76.13 g/mol"],
        "CrK2O4":["Potassium chromate","194.189 g/mol"],
        "ZnSO4":["Zinc sulfate","161.436 g/mol"],
        "I":["Iodine","Atomic mass 126.90 g/mol"],
        "C76H52O46":["Tannic acid","1701.19 g/mol"],
        "Al":["Aluminum","26.982 g/mol"],
        "HClO4":["Perchloric acid","100.46 g/mol"],
        "KBr":["Potassium Bromide","119.002 g/mol"],
        "H2CrO4":["Chromic acid","118.01 g/mol"],
        "OH2":["Dihydrogen monoxide","18.01528 g/mol"],
        "C3H6O2":["Methyl acetate","74.079 g/mol"],
        "C2H6OS":["Dimethyl sulfoxide","78.13 g/mol"],
        "C6H14":["Hexane","86.18 g/mol"],
        "C10H12O2":["Eugenol","164.2 g/mol"],
        "MnO2":["Manganese dioxide","86.9368 g/mol"],
        "C3H6O3":["Lactic acid","90.078 g/mol"],
        "C4H4O6KNa·4H2O":["Sodium potassium tartrate","282.1 g/mol"],
        "C6H12N4":["Hexamine","140.186 g/mol"],
        "LiOH":["Lithium hydroxide","23.95 g/mol"],
        "PCl5":["Phosphorus pentachloride","208.24 g/mol"],
        "K2O":["Potassium oxide","94.2 g/mol"],
        "KH2PO4":["Monopotassium phosphate","136.084 g/mol"],
        "AgC2H3O2":["Silver acetate","166.91 g/mol"],
        "Na3C6H5O7":["Sodium citrate","258.06 g/mol"],
        "NaF":["Sodium fluoride","41.98817 g/mol"],
        "NaNO2":["Sodium nitrite","68.9953 g/mol"],
        "SO4":["Sulfate ion","96.06 g/mol"],
        "BaCO3":["Barium carbonate","197.34 g/mol"],
        "CaI2":["Calcium iodide","293.887 g/mol"],
        "Li2O":["Lithium oxide","29.88 g/mol"],
        "C4H8N2O2":["Dimethylglyoxime","116.12 g/mol"],
        "KMnO4":["Potassium Permanganate","158.034 g/mol"],
        "Ag3PO4":["Silver phosphate","418.58 g/mol"],
        "NH4Br":["Ammonium bromide","97.943 g/mol"],
        "Ca3(PO4)2":["Calcium phosphate","310.18 g/mol"],
        "K2Cr2O7":["Dichromate","294.185 g/mol"],
        "Al2S3":["Aluminum sulfide","150.158 g/mol"],
        "(NH4)2CO3":["Ammonium carbonate","96.086 g/mol"],
        "BaCl2":["Barium chloride","208.23 g/mol"],
        "NO":["Nitrogen monoxide","30.006 g/mol"],
        "C6H12O6":["Fructose","180.16 g/mol"],
        "MgI2":["Magnesium iodide","278.1139 g/mol"],
        "MgS":["Magnesium sulfide","56.38 g/mol"],
        "O3":["Ozone","48 g/mol"],
        "KCN":["Potassium cyanide","65.12 g/mol"],
        "Ag2O":["Silver oxide","231.735 g/mol"],
        "Na2CrO4":["Sodium chromate","161.97 g/mol"],
        "Na2O2":["Sodium peroxide","77.98 g/mol"],
        "C7H8":["Toluene","92.14 g/mol"],
        "ZnCO3":["Zinc carbonate","125.388 g/mol"],
        "Zn3(PO4)2":["Zinc phosphate","386.11 g/mol"],
        "ZnS":["Zinc sulfide","97.474 g/mol"],
        "C6H4Cl2":["Para dichlorobenzene","147.01 g/mol"],
        "H3BO3":["Boric acid","61.83 g/mol"],
        "KHCO3":["Potassium bicarbonate","100.114 g/mol"],
        "KClO":["Potassium hypochlorite","90.55 g/mol"],
        "KNO2":["Potassium nitrite","85.103 g/mol"],
        "C27H28Br2O5S":["Bromothymol Blue","624.384 g/mol"],
        "NH4I":["Ammonium iodide","144.94 g/mol"],
        "NH4NO2":["Ammonium nitrite","64.06 g/mol"],
        "(NH4)2O":["Ammonium oxide","52.0763 g/mol"],
        "Ar":["Argon gas","39.948 g/mol"],
        "BaBr2":["Barium bromide","297.14 g/mol"],
        "BaI2":["Barium iodide","391.136 g/mol"],
        "BrO3":["Bromate","127.901 g/mol"],
        "N2O3":["Dinitrogen trioxide","76.01 g/mol"],
        "C2H6O2":["Ethylene glycol","62.07 g/mol"],
        "NiSO4":["Nickel sulfate","154.75 g/mol"],
        "Pb(C2H3O2)2":["Lead ii acetate","325.29 g/mol"],
        "LiCl":["Lithium chloride","42.394 g/mol"],
        "PO43-":["Phosphate ion","94.9714 g/mol"],
        "KF":["Potassium fluoride","58.0967 g/mol"],
        "K2SO3":["Potassium sulfite","158.26 g/mol"],
        "Ag2CO3":["Silver carbonate","275.7453 g/mol"],
        "NaCN":["Sodium cyanide","49.0072 g/mol"],
        "Na3N":["Sodium nitride","82.976 g/mol"],
        "SrCl2":["Strontium chloride","158.52 g/mol"],
        "Sr(NO3)2":["Strontium nitrate","211.628 g/mol"],
        "CH4N2O":["Urea","60.056 g/mol"],
        "NaClO":["Bleach","74.439 g/mol"],
        "LiBr":["Lithium bromide","86.844 g/mol"],
        "AlF3":["Aluminum fluoride","83.9767 g/mol"],
        "BaF2":["Barium fluoride","175.34 g/mol"],
        "C4H8O2":["Butanoic acid","88.11 g/mol"],
        "CaH2":["Calcium hydride","42.094 g/mol"],
        "CuCO3":["Copper ii carbonate","123.55 g/mol"],
        "Li3PO4":["Lithium phosphate","115.79 g/mol"],
        "C3H8O3":["Glycerol","92.09382 g/mol"],
        "HBrO":["Hypobromous acid","96.911 g/mol"],
        "HIO":["Hypoiodous acid","143.89 g/mol"],
        "PbI2":["Lead iodide","461.01 g/mol"],
        "LiI":["Lithium iodide","133.844 g/mol"],
        "MgO":["Magnesium oxide","40.3044 g/mol"],
        "C3H7NO2":["Urethane","89.09 g/mol"],
        "Ni(NO3)2":["Nickel nitrate","182.703 g/mol"],
        "Na2Cr2O7":["Sodium dichromate","261.97 g/mol"],
        "C4H6O6":["Tartaric acid","150.087 g/mol"],
        "ZnI2":["Zinc iodide","319.22 g/mol"],
        "Br":["Bromine","54.9380 g/mol"],
        "AlBr3":["Aluminum bromide","266.69 g/mol"],
        "C2H6Na4O12":["Sodium Percarbonate","157.01 g/mol"],
        "C4H6O4Ni":["Nickel acetate","178.797 g/mol"],
        "Na2S2O3":["Sodium Thiosulfate","158.11 g/mol"],
        "C2H4O":["Acetaldehyde","44.05 g/mol"],
        "CuSO4":["Copper sulfate","159.609 g/mol"],
        "C6H14O6":["Mannitol","182.172 g/mol"],
        "CaCl2":["Calcium Chloride","110.98 g/mol"],
        "C5H8NO4Na":["Monosodium Glutamate","169.111 g/mol"],
        "(C8H8)n":["Polystyrene","104.1 g/mol"],
        "CaC2":["Calcium Carbide","64.099 g/mol"],
        "C2Cl4":["Tetrachloroethylene","165.83 g/mol"],
        "NaClO3":["Sodium Chlorate","106.44 g/mol"],
        "KIO3":["Potassium Iodate","214.001 g/mol"],
        "Pb(C2H3O2)2":["Lead Acetate","325.29 g/mol"],
        "KSCN":["Potassium Thiocyanate","97.181 g/mol"],
        "C4H10":["Butane","58.12 g/mol"],
        "C12H22O11":["Maltose","342.3 g/mol"],
        "C27H36N2O10":["Polyurethane Foam","548.589 g/mol"],
        "CH2O":["Formaldehyde","30.031 g/mol"],
        "HCOOH":["Formic Acid","46.03 g/mol"],
        "SF6":["Sulfur Hexafluoride","146.06 g/mol"],
        "PCl3":["Phosphorus Trichloride","137.33 g/mol"],
        "C2H6":["Ethane","30.07 g/mol"],
        "N2O5":["Dinitrogen Pentoxide","30.07 g/mol"],
        "H3PO3":["Phosphorous Acid","82 g/mol"],
        "K4Fe(CN)6":["Potassium Ferrocyanide","368.35 g/mol"],
        "XeF2":["Xenon Difluoride","169.29 g/mol"],
        "Br2":["Diatomic Bromine","159.808 g/mol"],
        "C6H5":["Phenyl","77.106 g/mol"],
        "PI3":["Phosphorus Triiodide","411.6872 g/mol"],
        "H2S2O8":["Peroxydisulfuric Acid","194.14 g/mol"],
        "K2HPO4":["Dipotassium Phosphate","174.2 g/mol"],
        "Al(OH)3":["Aluminium hydroxide","78.00 g/mol"],
        "(NH4)2S2O8":["Ammonium persulfate","228.18 g/mol"],
        "Na2[B4O5(OH)4]·8H2O":["Sodium borate","201.22 g/mol"],
        "C2H3O2Cl":["Chloroacetic acid","94.49 g/mol"],
        "CH3CO2K":["Potassium acetate","98.142 g/mol"],
        "BaO":["Barium oxide","153.326 g/mol"],
        "Cu2O":["Copper(I) Oxide","143.09 g/mol"],
        "Cu(OH)2":["Copper Hydroxide","97.561 g/mol"],
        "SnO2":["Tin Oxide","97.561 g/mol"],
        "ClF3":["Chlorine Trifluoride","92.448 g/mol"],
        "C2H4":["Ethylene","28.054 g/mol"],
        "C2H2":["Acetylene","26.038 g/mol"],
        "Cr2O3":["Chromic Oxide","151.9904 g/mol"],
        "NaHSO4":["Sodium bisulfate","120.06 g/mol"],
        "CuCl2":["Copper (II) chloride","134.45 g/mol"],
        "HgCl2":["Mercuric chloride","271.52 g/mol"],
        "SnCl2":["Tin (II) chloride","189.60 g/mol"],
        "C3H8":["Propane","44.097 g/mol"],
        "PbO2":["Lead (IV) oxide","239.1988 g/mol"]
    }
    
    '''
    1.Check if formula exists in dictionary
        return formula object
    else:
        null and void    
    '''
    if formula in known_molecules_dict:
        return known_molecules_dict[formula]
    
    else:
        return ['Unknown Formula', '?? g/mol']

# Call the main function
if __name__ == '__main__':
    main()