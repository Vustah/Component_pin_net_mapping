from tkinter.filedialog import askopenfilename, askdirectory
import sys

nets = {}

def definePath():
    path = askdirectory()
    return path

def ReadFile(path,filename=None):
    if filename == None:
        fileName = askopenfilename(initialdir=path)
    else:
        fileName = path + filename

    try:
        infile = open(fileName,'r')
    except FileNotFoundError:
        print("File Not Found\n", sys.exc_info()[1])
        exit(1)

    infile_content = infile.readlines()
    for idx,line in enumerate(infile_content):
        infile_content[idx] = line.replace("\n","").replace("\t"," ")
    infile.close()
    return infile_content

def WriteFile(content,path,fileName):
    outfile = open(path+"/"+fileName, 'w')
    outfile.write(content)
    outfile.close()

def structure_Nets(nets,path):
    content = ""
    for net_key in nets:
        content += net_key+":\n"
        for comp_key in nets[net_key]:
            for item in nets[net_key][comp_key]:
                pin_name = item["pin_name"]
                pin_number = item["pin_number"]

                content += "\t"+comp_key+"."+pin_number+": "+ pin_name +"\n"
    WriteFile(content,path,"NetList.txt")    

def parse(content):
    net_name_defined = False
    net_name = "h"
    for idx, line in enumerate(content):
        if content[idx] == "NET_NAME":
            net_name = content[idx+1].replace("'","")
            nets[net_name] = {}
            net_name_defined = True
        else:
            #print(net_name)
            if net_name_defined:
                line = line.split(" ")
                if line[0] == "NODE_NAME":
                    pin_name = content[idx+2].replace("'","").replace("\\","").split(":")[0].replace(" ","")
                    #print(pin_name)
                    ref_des = line[1]
                    pin_number = line[2]
                    try: 
                        nets[net_name][ref_des].append({"pin_number":pin_number,
                                                        "pin_name": pin_name})
                    except KeyError:    
                        nets[net_name][ref_des] = [{"pin_number":pin_number,
                                                    "pin_name": pin_name}]

    return nets

def main():
    path = definePath()
    infile_content = ReadFile(path)
    nets = parse(infile_content)
    structure_Nets(nets,path)

if "__main__" == __name__:
    main()
