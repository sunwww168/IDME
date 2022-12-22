# IDME
#Finding critical nodes in a complex network from information diffusion and Matthew effect aggregation


The identification of critical nodes is crucial for studying the spread of diseases, vaccination strategies, the robustness of power grids, the placement of advertisements, and the control of rumors and has become a hot topic of immense interest.  Aiming at the needs of propagation scenarios, we propose a new critical node identification approach (IDME) based on information diffusion and Matthew effect aggregation, inspired by real-world information diffusion and the phenomenon of the Matthew effect. 

#requirements
Python== 3.7.3
networkx==2.3
matplotlist==3.1.0


# Execution

The algorithm can be used as standalone program as well as integrated in python scripts.

## Standalone

IDME can be executed as standalone script with the following parameters:

**arguments**
Name  |  Type | Description | Default 
-------------  | ------------- |------------- | -------------
allpath | string| It cotains the file path of networks | './datasets/filelist_dataset.txt'
files|string|The rank list of IDME algorithm on each network| './datasets/+pt+/data/+pt+.txt'


#Input
All network file path names are placed in the './datasets/filelist_dataset.txt' file. E.g:<br>
dolphins<br>
CE<br>
euroroad<br>
citeseer<br>
Hamster<br>
powergird<br>
routeview<br>
ca-astroph<br>

# Output
The rank list of IDME algorithm on each network, which are written to the './datasets/+pt+/data/+pt+.txt' file.

Instructions for using DCDME code:

1.Install networkx  python libraries before running the script.

2.Unzip datasets.zip to the current directory. 


3.Run the python file IDME.py.

