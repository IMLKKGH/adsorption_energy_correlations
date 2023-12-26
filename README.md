This script is designed for the extraction of information regarding the coordination number of each adsorption site and their corresponding charges on a surface structure with an adsorbate molecule. This script is designed for binary alloys with an adsorbate molecule containing two atoms. The binary alloy is defined as XY, the molecule is M-M. 
To use this script you need the following files and folders:

1) all_inputs: In this file, you need all the input files for the adsorption energy calculations. The input files are named as ad_site_1.in, ad_site_2.in, ...

2)cell_extended: In order to have the information regarding all the neighbors, in some cases of DFT models, the molecule is near the edge, you need to repeat the cell model to get all the neighbors properly. 
3)cleaned_CuNi_bader.csv: This file contains the Bader charges of the surface.
4)adsorption_energy_calculated.csv: calculated adsorption energy for all the input files. 


Script final_data.py gets the Quantum espresso input files, and prints out following information:
    {'#adsite': adsite_index,
     'min_M1_distance': the minimum distance of one of the M atoms in M2 molecule from its nearest metal atom
     'max_M2_distance': the maximum distance of one of the M atoms in M2 molecule from its nearest metal atom
     'adsite_Cu_CN_dis-upto-3.0': Number of Cu atoms in vicinity of midpoint of M2 molecule with maximum distance of 3 angstrom.
     'adsite_Ni_CN_dis_upto-3.0': Number of Ni atoms in vicinity of midpoint of M2 molecule with maximum distance of 3 angstrom.
     'adsite_Cu_CN_dis_3.0-3.5':  Number of Cu atoms in vicinity of midpoint of M2 molecule with distance of 3 to 3.5  angstrom.
     'adsite_Ni_CN_dis_3.0-3.5':  Number of Ni atoms in vicinity of midpoint of M2 molecule with distance of 3 to 3.5  angstrom.
     'adsite_Cu_CN_dis_3.5-4.0':  Number of Cu atoms in vicinity of midpoint of M2 molecule with distance of 3.5 to 4.0 angstrom.
     'adsite_Ni_CN_dis_3.5-4.0':  Number of Ni atoms in vicinity of midpoint of M2 molecule with distance of 3.5 to 4.0 angstrom.
     'min_CN_distance': minimum distance from the middle point of M2 molecule to the first nearest neighbour,
     'bader_charges_dist_Cu_upto_3.0': bader charges of Cu atoms with up to 3.0 angstrom distance from the middle point of M2 molecule in a form of list.
     'bader_charges_dist_Ni_upto_3.0': bader charges of Ni atoms with up to 3.0 angstrom distance from the middle point of M2 molecule in a form of list.
     'bader_charges_dist_Cu_3.0_3.5':  bader charges of Cu atoms with 3.0-3.5 angstrom distance from the middle point of M2 molecule in a form of list.
     'bader_charges_dist_Ni_3.0_3.5':  bader charges of Ni atoms with 3.0-3.5 angstrom distance from the middle point of M2 molecule in a form of list.
     'bader_charges_dist_Cu_3.5_4.0':  bader charges of Cu atoms with 3.5-4.0 angstrom distance from the middle point of M2 molecule in a form of list.
     'bader_charges_dist_Ni_3.5_4.0':  bader charges of Cu atoms with 3.5-4.0 angstrom distance from the middle point of M2 molecule in a form of list.
     'total_charge_distance_Cu_upto_30':sum over bader charges of bader charges of Cu atoms with up to 3.0 angstrom distance from the middle point of N2 molecule.
     'total_charge_distance_Ni_upto_30':sum over bader charges of Ni atoms with up to 3.0 angstrom distance from the middle point of N2 molecule. 
     'total_charge_distance_Cu_30_35': sum over bader charges of Cu atoms with 3.0-3.5 angstrom distance from the middle point of N2 molecule. 
     'total_charge_distance_Ni_30_35': sum over bader charges of Ni atoms with 3.0-3.5 angstrom distance from the middle point of N2 molecule.
     'total_charge_distance_Cu_35_40': sum over bader charges of Cu atoms with 3.5-4.0 angstrom distance from the middle point of N2 molecule.
     'total_charge_distance_Ni_35_40': sum over bader charges of Cu atoms with 3.5-4.0 angstrom distance from the middle point of N2 molecule. 
     'adsorption_E': adsorption energy of each configuration,


