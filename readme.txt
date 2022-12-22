# IDME
#Finding critical nodes in a complex network from information diffusion and Matthew effect aggregation


The identification of critical nodes is crucial for studying the spread of diseases, vaccination strategies, the robustness of power grids, the placement of advertisements, and the control of rumors and has become a hot topic of immense interest.  Aiming at the needs of propagation scenarios, we propose a new critical node identification approach (IDME) based on information diffusion and Matthew effect aggregation, inspired by real-world information diffusion and the phenomenon of the Matthew effect. 

#requirements
Python== 3.7.3
networkx==2.3
scikit-learn==1.0.2
numpy==1.19.0
matplotlist==3.1.0


# Execution

The algorithm can be used as standalone program as well as integrated in python scripts.

## Standalone

DCDME can be executed as standalone script with the following parameters:

**arguments**
Name  |  Type | Description | Default 
-------------  | ------------- |------------- | -------------
allpath | string| It cotains the file path of Dynamic networks | './data/my_LFR/files.txt'
path_score|string|The scores of DCDME algorithm on each dynamic network| 'result_score_LFR.xlsx'
l | integer |number of snapshot | len(edgefilelist)

#Input
The dynamic networks. We use batch processing, and all dynamic network file path names are placed in the 'files.txt' file. E.g:
birthdeath_u0.1_b0.1_d0.1<br>
birthdeath_u0.2_b0.1_d0.1<br>
birthdeath_u0.3_b0.1_d0.1<br>
birthdeath_u0.4_b0.1_d0.1<br>
birthdeath_u0.5_b0.1_d0.1<br>
birthdeath_u0.6_b0.1_d0.1<br>
birthdeath_u0.7_b0.1_d0.1<br>
birthdeath_u0.8_b0.1_d0.1<br>
switch_u0.1_p0.1k5<br>
switch_u0.1_p0.1k10<br>
switch_u0.1_p0.1k15<br>
switch_u0.1_p0.1k20<br>
switch_u0.1_p0.1k25<br>

# Output
The scores of DCDME algorithm on each dynamic network, which are written to the 'result_score_LFR.xlsx' file. Community information can be obtained from object 'comm_va'.

Instructions for using DCDME code:

1.Install networkx and scikit-learn python libraries before running the script.

2.Place the script inside the dataset folder. The folder should have edge files and community files corresponding to the number of snapshots. 

3.The dateset directory should contain the 'files.txt' file, which contains the directory to execute.

4.Two files, 'edgeslist.txt' and 'commlist.txt', should be included in each directory to be executed, which respectively contain the information of each dynamic network and the corresponding groundtruth community.

5.Run the script like any ususal python script after following steps 1-4.
Unzip datasets.zip to the current directory
