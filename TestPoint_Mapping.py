import NetParsing as NP


def sort_TestPoints(nets,path):
    Test_points = {}
    TP_found = False
    for net_key in nets:
        for comp_key in nets[net_key]:
            if comp_key.find("TP") != -1:
                Test_points[comp_key] = net_key
                TP_found = True
    if not TP_found:
        return None
    Test_points_xls = [["Test Point","Net Name"]]
    for key in Test_points:
        #Test_points_csv += key + "\t" + Test_points[key]+"\n"
        Test_points_xls.append([key, Test_points[key]])
    
    return Test_points_xls

    #NP.WriteFile(Test_points_csv,path,"TestPoints.csv")


def main():
    path = NP.definePath()
    infile_content = NP.ReadFile(path)
    nets = NP.parse(infile_content)
    NP.structure_Nets(nets,path)
    sort_TestPoints(nets,path)

if "__main__" == __name__:
    main()

