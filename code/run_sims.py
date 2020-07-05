import os, sys
import glob 
files_and_folders = os.listdir('.')
crops = [folder for folder in files_and_folders if folder[0] == '_']

for crop in crops :
    os.chdir(crop)
    apsim_files = glob.glob("./*.apsim")
    for file in apsim_files :
        os.system("apsim "+file)
        out_file = glob.glob("./*.out")[0]
        summary_file = glob.glob("./*.sum")[0]
        #print(out_file,'               ',file.split('.')[0])
        #break
        file_prefix = file.split('.')[1][1:]
        
        with open(out_file,'r') as f :
            s = f.read()
            with open(file_prefix+'.out','w') as F :
                F.write(s)
        with open(summary_file,'r') as f :
            s = f.read()
            with open(file_prefix+'.sum','w') as F :
                F.write(s)
    os.chdir('..')
    
