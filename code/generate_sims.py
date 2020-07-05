import argparse
import xml.etree.ElementTree as ET
import glob 
import os 


metfiles = glob.glob('.//**//*.met',recursive=True)
simulation_files = glob.glob('*.apsim',recursive=False)



# factorial vars -----------------



# factorial vars -----------------

for sim_file in simulation_files :
    
    with open(sim_file,'r') as S :
        sim_name = os.path.split(sim_file)[-1].split('.')[0]
        try :
            os.mkdir('_'+sim_name)
        except Exception :
            pass
        tree = ET.parse(sim_file)
        print(sim_file)
        root = tree.getroot()
        for metfile in metfiles:
            with open(metfile,'r') as f :
                lines = f.readlines()
                Latitude = float(lines[1].split(' ')[2])
                district = os.path.split(metfile)[-1].split('.')[0]
                for density in range(1,4):
                    sf_name = ('_'+sim_name+'\\'+sim_name+district+'_'+str(density)+'_'+'.apsim').replace(" ", "")
                    of_name = ('_'+sim_name+district+'_'+str(density)+'_''.out').replace(" ", "")
                    root.find(".//metfile")[0].text = '..\\'+metfile[2:] 
                    if root.find(".//Latitude") != None :
                        root.find(".//Latitude").text = str(Latitude) 
                    #root.find(".//outputfile")[0].text = of_name
                    root.find(".//density").text = str(density)

                    tree.write(sf_name)



























