import NetParsing as NP
import xlwt
import TestPoint_Mapping as TP


def writeExcel(filename,sheetname,content,wb):
    sheet = wb.add_sheet(sheetname)
    for idx,row in enumerate(content):
        for jdx,cell in enumerate(row):
            sheet.write(int(idx),jdx,cell)
    
def component_table(nets, path, component):
    component_dict = {}
    component_exist = False
    for net_key in nets:
        for comp_key in nets[net_key]:
            if comp_key.find(component) != -1:
                Pin_key = nets[net_key][comp_key]
                for pin in Pin_key:
                    pin_name = pin["pin_name"]
                    pin_number = pin["pin_number"]
                    try:
                        component_dict[net_key].append({"pin_name":pin_name,
                                                "pin_number":pin_number})
                    except KeyError:
                        component_dict[net_key] = [{"pin_name":pin_name,
                                                "pin_number":pin_number}]
                component_exist = True
    return component_dict, component_exist

def parse_component_dict(path, component_dict, comp_name,filename,wb):
    #Component_csv = "Pin number \tPin Name \tNet Name\n"
    Component = [["Pin number","Pin Name" ,"Net Name", "Description", "Notes"]]
    for net_key in component_dict:
        for net in component_dict[net_key]:
            pin_name = net["pin_name"]
            pin_number = net["pin_number"]
            
            #Component_csv += pin_number + "\t" + pin_name + "\t" + net_key + "\n"
            Component.append([pin_number,pin_name,net_key])
    writeExcel(filename,comp_name,Component,wb)
    #NP.WriteFile(Component_csv, path, comp_name+".xls")

def find_all_IC(nets, componet_group_to_find = "U"):
    IC_list = []
    for net_key in nets:
        for comp_key in nets[net_key]:
            if comp_key.find(componet_group_to_find) != -1:
                if not comp_key in IC_list:
                    IC_list.append(comp_key)
    IC_list.sort(key=lambda x: int("".join([i for i in x if i.isdigit()])))
    return IC_list

def find_and_write_components(nets,path,componet_group_to_find,filename):
    wb = xlwt.Workbook()
    filename = path+"\\"+filename
    IC_list = find_all_IC(nets,componet_group_to_find)
    if IC_list:
        for comp_name in IC_list:
            component_dict, component_exist = component_table(nets, path, comp_name)
            if component_exist:
                parse_component_dict(path, component_dict,comp_name,filename,wb)
        try:
            wb.save(filename)
        except PermissionError: 
            print("This file is already open somewhere. \nYou need to close it and try again.")
            exit(1)
        

def write_testPoints(path, filename,content):
    filename = path+ "\\" + filename
    wb = xlwt.Workbook()
    writeExcel(filename,"TestPoints",content, wb)
    wb.save(filename)


def main():
    path = NP.definePath()
    filename = "/pstxnet.dat"
    infile_content = NP.ReadFile(path,filename)
    nets = NP.parse(infile_content)
    NP.structure_Nets(nets,path)
    find_and_write_components(nets,path,"U","Components.xls")
    find_and_write_components(nets,path,"J","Connectors.xls")
    testpointContent = TP.sort_TestPoints(nets,path)
    write_testPoints(path,"TestPoints.xls",testpointContent)
    
    print("Success")

if "__main__" == __name__:
    main()