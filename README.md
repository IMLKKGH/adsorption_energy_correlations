This script is designed for the extraction of information regarding the coordination number of each adsorption site and their corresponding charges on a surface structure with an adsorbate molecule. This script is designed for binary alloys with an adsorbate molecule containing two atoms. The binary alloy is defined as XY, the molecule is M-M. 
To use this script you need the following files and folders:

1) all_inputs: In this file, you need all the input files for the adsorption energy calculations. The input files are named as ad_site_1.in, ad_site_2.in, ...

2)cell_extended: In order to have the information regarding all the neighbors, in some cases of DFT models, the molecule is near the edge, you need to repeat the cell model to get all the neighbors properly. 
3)cleaned_CuNi_bader.csv: This file contains the Bader charges of the surface.
4)adsorption_energy_calculated.csv: calculated adsorption energy for all the input files. 



