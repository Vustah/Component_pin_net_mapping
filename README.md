# Component_pin_net_mapping
A small script that takes a netlist created in Orcad and creates a pin-net mapping for components, connectors and testpoints. 


## How to "install" program
- Clone the repo from GitHub
- Install python through "anaconda Download"
- Create an environment variable called %CONDA_PATH% for the path to where anaconda is installed.
- Create an environment variable called %COMPONENT_MAPPING% for the path to where the downloaded files is located.


## How to run progam
- A netlist needs to be generated prior to running this script.
- - In order to generate the file called "pstxnet.dat"
- The program is ran by running the script called "Component_net_table.bat"
- - A dialog will show up
- - Navigate to the folder where the netlist is located. 
- - - The folder needs to have a file called "pstxnet.dat"
- Then three excel documents is created in the folder chosen.
- - Components.xls
- - Connectors.xls
- - Testpoints.xls.