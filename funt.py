# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:21:40 2018

@author: hp
"""

l=['pe.FILE_HEADER.NumberOfSections',
'pe.FILE_HEADER.TimeDateStamp',
'pe.FILE_HEADER.PointerToSymbolTable',
'pe.FILE_HEADER.NumberOfSymbols',
#       'pe.FILE_HEADER.Machine',
    'pe.FILE_HEADER.Characteristics',
#     'pe.FILE_HEADER.SizeOfOptionalHeader',
      'pe.OPTIONAL_HEADER.AddressOfEntryPoint',
       'pe.OPTIONAL_HEADER.BaseOfCode',
       'pe.OPTIONAL_HEADER.BaseOfData',
       'pe.OPTIONAL_HEADER.CheckSum',
       'pe.OPTIONAL_HEADER.DllCharacteristics',
       'pe.OPTIONAL_HEADER.FileAlignment',
       'pe.OPTIONAL_HEADER.ImageBase',
#       'pe.OPTIONAL_HEADER.LoaderFlags',
#       'pe.OPTIONAL_HEADER.Magic',
       'pe.OPTIONAL_HEADER.MajorImageVersion',
       'pe.OPTIONAL_HEADER.MajorLinkerVersion',
       'pe.OPTIONAL_HEADER.MajorOperatingSystemVersion',
       'pe.OPTIONAL_HEADER.MajorSubsystemVersion',
       'pe.OPTIONAL_HEADER.MinorImageVersion',
       'pe.OPTIONAL_HEADER.MinorLinkerVersion',
       'pe.OPTIONAL_HEADER.MinorOperatingSystemVersion',
       'pe.OPTIONAL_HEADER.MinorSubsystemVersion',
       'pe.OPTIONAL_HEADER.NumberOfRvaAndSizes',
       'pe.OPTIONAL_HEADER.SectionAlignment',
       'pe.OPTIONAL_HEADER.SizeOfCode',
       'pe.OPTIONAL_HEADER.SizeOfHeaders',
#       'pe.OPTIONAL_HEADER.SizeOfHeapCommit',
       'pe.OPTIONAL_HEADER.SizeOfHeapReserve',
       'pe.OPTIONAL_HEADER.ImageBase',
       'pe.OPTIONAL_HEADER.SizeOfInitializedData',
       'pe.OPTIONAL_HEADER.SizeOfStackCommit',
       'pe.OPTIONAL_HEADER.SizeOfStackReserve',
       'pe.OPTIONAL_HEADER.SizeOfUninitializedData',
       'pe.OPTIONAL_HEADER.Subsystem',
#       'pe.DOS_HEADER.e_magic',
       'pe.DOS_HEADER.e_cparhdr',
       'pe.DOS_HEADER.e_lfarlc',
       'pe.DOS_HEADER.e_oeminfo',
       'pe.DOS_HEADER.e_maxalloc',
       'pe.DOS_HEADER.e_ip',
       'pe.DOS_HEADER.e_lfanew',
       'pe.DOS_HEADER.e_csum',
       'pe.DOS_HEADER.e_ovno',
       'pe.DOS_HEADER.e_minalloc',
       'pe.DOS_HEADER.e_cp',
       'pe.DOS_HEADER.e_cblp',
       'pe.DOS_HEADER.e_sp'
       ]
    

tmp = ['pe.FILE_HEADER.IMAGE_FILE_RELOCS_STRIPPED',\
#            'pe.FILE_HEADER.IMAGE_FILE_EXECUTABLE_IMAGE',\
            'pe.FILE_HEADER.IMAGE_FILE_LINE_NUMS_STRIPPED',\
            'pe.FILE_HEADER.IMAGE_FILE_LOCAL_SYMS_STRIPPED',\
#            'pe.FILE_HEADER.IMAGE_FILE_AGGRESIVE_WS_TRIM',\
#            'pe.FILE_HEADER.IMAGE_FILE_LARGE_ADDRESS_AWARE',\
            'pe.FILE_HEADER.IMAGE_FILE_BYTES_REVERSED_LO',\
#            'pe.FILE_HEADER.IMAGE_FILE_32BIT_MACHINE',\
            'pe.FILE_HEADER.IMAGE_FILE_DEBUG_STRIPPED',\
#            'pe.FILE_HEADER.IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP',\
#            'pe.FILE_HEADER.IMAGE_FILE_NET_RUN_FROM_SWAP',\
#            'pe.FILE_HEADER.IMAGE_FILE_SYSTEM',\
            'pe.FILE_HEADER.IMAGE_FILE_DLL',\
#            'pe.FILE_HEADER.IMAGE_FILE_UP_SYSTEM_ONLY',\
            'pe.FILE_HEADER.IMAGE_FILE_BYTES_REVERSED_HI'
            ]



        
#for x in l:
#    print('try:')
#    print('\tl.append('+x+')')
#    print('except AttributeError:')
#    print("\tl.append('')")
#    
#
#for x in tmp:
#    print('try:')
#    print('\tl.append(int('+x+'))')
#    print('except AttributeError:')
#    print("\tl.append('')")
    
n=['Name']
for c in range(0,len(l)):
    flag=0
    str=''
    for x in l[c]:
        if(x=='.'):
            flag=flag+1
            continue
        if(flag==2):
            str=str+x
    n.append(str)
    
    
for c in range(0,len(tmp)):
    flag=0
    str=''
    for x in tmp[c]:
        if(x=='.'):
            flag=flag+1
            continue
        if(flag==2):
            str=str+x
    n.append(str)

n.append('mal')
#with open('data.csv', 'a', newline='') as myfile:
#        wr = csv.writer(myfile, dialect='excel')
#        wr.writerow(n)


