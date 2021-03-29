# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:03:27 2018

@author: lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:34:08 2018

@author: hp
"""
import csv
import pefile
import os
import pandas as pd
csvname='rough.csv'
global path
path = 'pe/'



#for x in pe_files:   
#       
#    name=path+x
#    try:
#        pe =  pefile.PE(name, fast_load=True)
#    except:
#        print(x)
#

  

def create(x,pe):
    mal=0
    l=[x]
    try:
            l.append(pe.FILE_HEADER.NumberOfSections)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.FILE_HEADER.TimeDateStamp)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.FILE_HEADER.PointerToSymbolTable)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.FILE_HEADER.NumberOfSymbols)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.FILE_HEADER.Characteristics)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.AddressOfEntryPoint)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.BaseOfCode)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.BaseOfData)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.CheckSum)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.DllCharacteristics)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.FileAlignment)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.ImageBase)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.MajorImageVersion)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.MajorLinkerVersion)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.MajorOperatingSystemVersion)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.MajorSubsystemVersion)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.MinorImageVersion)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.MinorLinkerVersion)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.MinorOperatingSystemVersion)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.MinorSubsystemVersion)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.NumberOfRvaAndSizes)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.SectionAlignment)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.SizeOfCode)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.SizeOfHeaders)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.SizeOfHeapReserve)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.ImageBase)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.SizeOfInitializedData)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.SizeOfStackCommit)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.SizeOfStackReserve)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.SizeOfUninitializedData)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.OPTIONAL_HEADER.Subsystem)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.DOS_HEADER.e_cparhdr)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.DOS_HEADER.e_lfarlc)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.DOS_HEADER.e_oeminfo)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.DOS_HEADER.e_maxalloc)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.DOS_HEADER.e_ip)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.DOS_HEADER.e_lfanew)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.DOS_HEADER.e_csum)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.DOS_HEADER.e_ovno)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.DOS_HEADER.e_minalloc)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.DOS_HEADER.e_cp)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.DOS_HEADER.e_cblp)
    except AttributeError:
            l.append('')
    try:
            l.append(pe.DOS_HEADER.e_sp)
    except AttributeError:
            l.append('')
    
    #bolean values for header
    try:
            l.append(int(pe.FILE_HEADER.IMAGE_FILE_RELOCS_STRIPPED))
    except AttributeError:
            l.append('')
    try:
            l.append(int(pe.FILE_HEADER.IMAGE_FILE_LINE_NUMS_STRIPPED))
    except AttributeError:
            l.append('')
    try:
            l.append(int(pe.FILE_HEADER.IMAGE_FILE_LOCAL_SYMS_STRIPPED))
    except AttributeError:
            l.append('')
    try:
            l.append(int(pe.FILE_HEADER.IMAGE_FILE_BYTES_REVERSED_LO))
    except AttributeError:
            l.append('')
    try:
            l.append(int(pe.FILE_HEADER.IMAGE_FILE_DEBUG_STRIPPED))
    except AttributeError:
            l.append('')
    try:
            l.append(int(pe.FILE_HEADER.IMAGE_FILE_DLL))
    except AttributeError:
            l.append('')
    try:
            l.append(int(pe.FILE_HEADER.IMAGE_FILE_BYTES_REVERSED_HI))
    except AttributeError:
            l.append('')
            
    l.append('')
#    l1=list(map(list, zip(*l)))
    del pe
#    pe.__data__.close()

    return l
            
#    with open(csvname, 'a', newline='') as myfile:
#        wr = csv.writer(myfile, dialect='excel')
#        wr.writerow(l)
        
        

def create_df(col,pe_files,name):
#    
#    pe_files = [f for f in os.listdir(path)]
    df=pd.DataFrame(columns=col)
#    pe_files=[]
#    name=[]
#    name.append("7z")
#    pe_files.append("E:/gui/pe/7z.exe")
    for x in range(0,len(pe_files)):      
        try:
#            pe_files = ['E:/guifinal/pe/hh.exe']
            with open(pe_files[x], "rb") as file_content:
                pe= pefile.PE(data=file_content.read(), fast_load=True)
            
#            pe =  pefile.PE(pe_files[x], fast_load=True)
            if(pe.FILE_HEADER.IMAGE_FILE_32BIT_MACHINE):
                l=create(name[x],pe)
                str=name[x]
                print(str+' features extracted succesfully')
                print(*l, sep = ", ") 
                df1=pd.DataFrame([l],columns=col)
                df=df.append(df1)
            
            else:
                    print(str+' is not 32 bit')
                    continue
        except:
#            str1=pe_files[x]
            print(" could not extract features")
    #pe=pefile.PE('e:/xp/hh.exe',fast_load=True)
    return df            






#
#def create_df(col):
#    
#    pe_files = [f for f in os.listdir(path)]
#    df=pd.DataFrame(columns=col)
#    for x in pe_files:      
#        name=path+x
#        try:
#            pe =  pefile.PE(name, fast_load=True)
#            if(pe.FILE_HEADER.IMAGE_FILE_32BIT_MACHINE):
#                l=create(x,pe)
#                
#                print(x+' features extracted succesfully')
#                print(*l, sep = ", ") 
#                df1=pd.DataFrame([l],columns=col)
#                df=df.append(df1)
#                
#            else:
#                    print(x+' is not 32 bit')
#                    continue
#        except:
#            print(x+" could not extract features")
#    return df     
    
#create_df()
          
        
    




