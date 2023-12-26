#Maincode

import os
import re
import numpy as np
import pandas as pd
import math
pd.set_option('display.max_rows', 200)
pd.options.display.max_colwidth = 500

#Adding bader_charges
bader_file_path = './cleaned_CuNi_bader.csv'
charges_df = pd.read_csv(bader_file_path)
charges_df.bader_charge = charges_df['bader_charge'].round(decimals = 4)
struct_charges_list = list(np.array(charges_df.bader_charge))

charges = list()

CN_Cu_full_list = []
CN_Ni_full_list = []
min_N1_d_full_list = [] 
max_N2_d_full_list = []
CN_distance_full_list = []

total_charges_sum_dis_Cu_25_30 = []
total_charges_sum_dis_Ni_25_30 = []
total_charges_sum_dis_Cu_30_35 = []
total_charges_sum_dis_Ni_30_35 = []
total_charges_sum_dis_Cu_35_40 = [] 
total_charges_sum_dis_Ni_35_40 = [] 



CN_Cu_25_30 = []
CN_Ni_25_30 = []
CN_Cu_30_35 = []
CN_Ni_30_35 = []
CN_Cu_35_40 = []
CN_Ni_35_40 = []
    
charges_distance_Cu_25_30 = []
charges_distance_Ni_25_30 = []
charges_distance_Cu_30_35 = []
charges_distance_Ni_30_35 = []
charges_distance_Cu_35_40 = []
charges_distance_Ni_35_40 = []




adsite_index = []
folder_path = './all_inputs/'
for n in range(1,128):
    file_name = f'ad_site_{n}.in'
    f = open(folder_path + 'cell_extended/' + file_name,'r')
    all_lines = f.readlines()

    cell_array_small = np.array([[10.2247 ,  0.     ,  0.     ],
           [-5.11235,  8.85485,  0.     ],
           [ 0.     ,  0.     , 23.3484 ]])

    cell_array_dupl = np.array([[ 20.4494,   0.    ,   0.    ],
           [-10.2247,  17.7097,   0.    ],
           [  0.    ,   0.    ,  23.3484]])


    atm_pos = []
    cell_parameters = []
    for line in all_lines:
        line = line.strip()
        #print(line)
        #Taking out number of atoms
        if 'nat' in line:
            nat = re.findall('[0-9]+',line)
            nat = int(nat[0])
        #Make a list out of all the atm_pos
        coordinate_line = re.findall('[A-Za-z]+\s+[-]*[0-9]+[.][0-9]+[d0]*\s+[-]*[0-9]+[.][0-9]+[d0]*\s+[-]*[0-9]+[.][0-9]+[d0]*',line)
        if coordinate_line: 
            coordinate = coordinate_line[0].split()
            for i in range(1,len(coordinate)):
                if 'd' in coordinate[i]:
                    coordinate[i] = coordinate[i].replace('d','0')
                coordinate[i] = float(coordinate[i])
            atm_pos.append(coordinate)
        
        
    #Making an array out of atomic positions by multiplying the cell parameters*atomic_coordiantes
    if nat > 66:
        for i in range(len(atm_pos)):
            atm_pos[i] = [atm_pos[i][0],np.dot(cell_array_dupl,np.array(atm_pos[i][1:]))]
    else:
        for i in range(len(atm_pos)):
            atm_pos[i] = [atm_pos[i][0],np.dot(cell_array_small,np.array(atm_pos[i][1:]))]


    #Adding number to atoms names
    count = 0
    for atom in atm_pos:
        count = count + 1
        atom[0] = atom[0] + f'{count}'
    
    #Finding the middle position of N2
    N_positions = []
    for atom in atm_pos:
        if re.findall('^N[0-9]+',atom[0]):
            N_positions.append(atom)
        
    for i in N_positions:
        atm_pos.remove(i)

    mid_bond_N2  = (N_positions[0][1] + N_positions[1][1])/2

    #Finding the adsorption site coordinate, it has the (XN1 + XN2/2, YN1+YN2/2, max(Z of all coordinates)
    all_z = []
    for atom in atm_pos:
        all_z.append(atom[1][2])
    max_z = max(all_z)
    ad_site_coordinate = np.array([mid_bond_N2[0],mid_bond_N2[1],max_z])

    #N_distances
    N1_distances = {}
    for atom in atm_pos:
        squared_distance = np.square(N_positions[0][1] - atom[1])
        distance = math.sqrt(sum(squared_distance))
        N1_distances[f'{N_positions[0][0]}-{atom[0]}'] = distance 

    
    min_dN1 = min(N1_distances.values())
    N1_distances = {k: v for k, v in sorted(N1_distances.items(), key=lambda item: item[1])}

    N2_distances = {}
    for atom in atm_pos:
        squared_distance = np.square(N_positions[1][1] - atom[1])
        distance = math.sqrt(sum(squared_distance))
        N2_distances[f'{N_positions[1][0]}-{atom[0]}'] = distance 

    min_dN2 = min(N2_distances.values())
    N2_distances = {k: v for k, v in sorted(N2_distances.items(), key=lambda item: item[1])}

    #Coordination numbers
    mid_N2_CN = {}
    for atom in atm_pos:
        squared_distance = np.square(mid_bond_N2 - atom[1])
        distance = math.sqrt(sum(squared_distance))
        mid_N2_CN[f'midnitmol-{atom[0]}'] = distance
    mid_N2_CN = {k: v for k, v in sorted(mid_N2_CN.items(), key=lambda item: item[1])}


    adsite_CN = {}
    for atom in atm_pos:
        squared_distance = np.square(ad_site_coordinate - atom[1])
        distance = math.sqrt(sum(squared_distance))
        adsite_CN[f'adsite-{atom[0]}'] = distance
    adsite_CN = {k: v for k, v in sorted(adsite_CN.items(), key=lambda item: item[1])}

    count_Cu_25_30 = 0
    count_Ni_25_30 = 0
    count_Cu_30_35 = 0
    count_Ni_30_35 = 0
    count_Cu_35_40 = 0
    count_Ni_35_40 = 0
    keys_ = []
    values_ = []
    charge_each_Cu_25_30 = []
    charge_each_Ni_25_30 = [] #
    charge_each_Cu_30_35 = []
    charge_each_Ni_30_35 = []
    charge_each_Cu_35_40 = []
    charge_each_Ni_35_40 = []
    
    for k,v in mid_N2_CN.items():
        values_.append(v)
        if v < 3.0000:
                atom_number = int(re.findall('[0-9]+',k)[0]) 
                bader_charge_atom_index = math.ceil(atom_number/4)
                bader_charge = struct_charges_list[bader_charge_atom_index-1]
                
                if 'Cu' in k:
                    count_Cu_25_30 = count_Cu_25_30 + 1
                    charge_each_Cu_25_30.append(bader_charge)
                if 'Ni' in k:
                    count_Ni_25_30 = count_Ni_25_30 + 1
                    charge_each_Ni_25_30.append(bader_charge)
                    
        if v < 3.5000 and v > 3.0000 or v == 3.0000:
                atom_number = int(re.findall('[0-9]+',k)[0]) 
                bader_charge_atom_index = math.ceil(atom_number/4)
                bader_charge = struct_charges_list[bader_charge_atom_index-1]
                
                if 'Cu' in k:
                    count_Cu_30_35 = count_Cu_30_35 + 1
                    charge_each_Cu_30_35.append(bader_charge)
                if 'Ni' in k:
                    count_Ni_30_35 = count_Ni_30_35 + 1
                    charge_each_Ni_30_35.append(bader_charge)
                    
                    
        if v < 4.0000 and v > 3.5000 or v == 3.5000:
                atom_number = int(re.findall('[0-9]+',k)[0]) 
                bader_charge_atom_index = math.ceil(atom_number/4)
                bader_charge = struct_charges_list[bader_charge_atom_index-1]
        
                if 'Cu' in k:
                    count_Cu_35_40 = count_Cu_35_40 + 1
                    charge_each_Cu_35_40.append(bader_charge)
                if 'Ni' in k:
                    count_Ni_35_40 = count_Ni_35_40 + 1
                    charge_each_Ni_35_40.append(bader_charge)
                    

                    
                    

    values_ = sorted(values_)
    #if min(values_) < 0.8:
        #CN_distance = min(values_[1:])
    #if min(values_)> 0.8:
    CN_distance = min(values_)
    

    
    min_N1 = min(N1_distances.values())
    max_N2 = max(N2_distances.values())

    
    
    CN_Cu_25_30.append(count_Cu_25_30)
    CN_Ni_25_30.append(count_Ni_25_30)
    CN_Cu_30_35.append(count_Cu_30_35)
    CN_Ni_30_35.append(count_Ni_30_35)
    CN_Cu_35_40.append(count_Cu_35_40)
    CN_Ni_35_40.append(count_Ni_35_40)
    
    charges_distance_Cu_25_30.append(charge_each_Cu_25_30)
    charges_distance_Ni_25_30.append(charge_each_Ni_25_30)
    charges_distance_Cu_30_35.append(charge_each_Cu_30_35)
    charges_distance_Ni_30_35.append(charge_each_Ni_30_35)
    charges_distance_Cu_35_40.append(charge_each_Cu_35_40)
    charges_distance_Ni_35_40.append(charge_each_Ni_35_40)
    total_charges_sum_dis_Cu_25_30.append(sum(charge_each_Cu_25_30))
    total_charges_sum_dis_Ni_25_30.append(sum(charge_each_Ni_25_30))
    total_charges_sum_dis_Cu_30_35.append(sum(charge_each_Cu_30_35))
    total_charges_sum_dis_Ni_30_35.append(sum(charge_each_Ni_30_35))
    total_charges_sum_dis_Cu_35_40.append(sum(charge_each_Cu_35_40))
    total_charges_sum_dis_Ni_35_40.append(sum(charge_each_Ni_35_40))
    min_N1_d_full_list.append(min_N1)
    min_N2_d_full_list.append(min_N2)
    CN_distance_full_list.append(CN_distance)
    adsite_index.append(file_name)
    
ad_energy_df = pd.read_csv('./adsorption_energy_calculated.csv')
ads_energy = ad_energy_df.adsorption_energy

cn_df = pd.DataFrame(
    {'#adsite': adsite_index,
     'min_N1_distance': min_N1_d_full_list,
     'max_N2_distance': min_N2_d_full_list,
     'adsite_Cu_CN_dis2.5-3.0': CN_Cu_25_30,
     'adsite_Ni_CN_dis2.5-3.0': CN_Ni_25_30,
     'adsite_Cu_CN_dis3.0-3.5': CN_Cu_30_35,
     'adsite_Ni_CN_dis3.0-3.5': CN_Ni_30_35,
     'adsite_Cu_CN_dis3.5-4.0': CN_Cu_35_40,
     'adsite_Ni_CN_dis3.5-4.0': CN_Ni_35_40,
     'min_CN_distance': CN_distance_full_list,
     'bader_charges_dist_Cu_2.5_3.0': charges_distance_Cu_25_30,
     'bader_charges_dist_Ni_2.5_3.0': charges_distance_Ni_25_30,
     'bader_charges_dist_Cu_3.0_3.5': charges_distance_Cu_30_35,
     'bader_charges_dist_Ni_3.0_3.5': charges_distance_Ni_30_35,
     'bader_charges_dist_Cu_3.5_4.0': charges_distance_Cu_35_40,
     'bader_charges_dist_Ni_3.5_4.0': charges_distance_Ni_35_40,
     'total_charge_distance_Cu_25_30':total_charges_sum_dis_Cu_25_30,
     'total_charge_distance_Ni_25_30':total_charges_sum_dis_Ni_25_30,
     'total_charge_distance_Cu_30_35':total_charges_sum_dis_Cu_30_35,
     'total_charge_distance_Ni_30_35':total_charges_sum_dis_Ni_30_35,
     'total_charge_distance_Cu_35_40':total_charges_sum_dis_Cu_35_40,
     'total_charge_distance_Ni_35_40':total_charges_sum_dis_Ni_35_40,
     'adsorption_E': ads_energy,
    })

cn_df.index = cn_df.index + 1

cn_df.to_csv(folder_path+'final_data.csv', index=False)
