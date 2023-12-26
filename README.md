This script is designed for extraction of information regarding the coordination number of each adsorption sites and their corresponding charges on a surface structure with an adsorbate molecule.
For using the  script you need the following files and folders:

1) all_inputs: In this file you need all the input files for the adsorption energy calculations. The input files are named as ad_site_1.in, ad_site_2.in, ...

2)dir: cell_extended: In order to have the information regarding all the neighbors, in some cases of DFT models, the molecule is near the edge, you need to repeat the cell model to get all the neighbors properly. 
3)cleaned_CuNi_bader.csv: This file contains the Bader charges of CuNi surface.
4)adsorption_energy_calculated.csv: calculated adsorption energy for all the input files. 


