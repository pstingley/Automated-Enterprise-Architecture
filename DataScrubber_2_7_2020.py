# DataScrubber_10_21_19.py
# 4_29_18 - Changed to ""ExploreComputers - Just the Apps Ma'am2.csv" after taking out run level 3 - PTS
# 6_26_2019 Added filters to remove the brands ilmntcc2 and ilmntcc from the prefixes to software - PTS
# 8_29_2019 Removed Vs and ()s that followed removing dates and versions from product names - PTS
# 9_21_2019 Reinserted "NV" in HP NV for ...  PTS
# 11_21_2019 Made "Test" stop being deleted because sometimes it shows up in product names.
# 12_3_2019 Deleted []
#

import time;

t1 = time.time()
timeStamp = time.strftime(" %H %M %S %d-%m-%Y")

file2scrub = "ExploreComputers - Just the Apps Ma'am.csv"
#file2scrub = "test_data.csv"
out_f = file2scrub+timeStamp+'.csv'
out_f2 = file2scrub+" with pipes "+timeStamp+'.csv'

print 'Began Scrubbing <'+file2scrub+'> at '+timeStamp
print 'The results will be written to <'+out_f+'>'
print 'And to <'+out_f2+'> for a count'

f = open(file2scrub, 'r')
of = open(out_f, 'w')
pipes = open(out_f2, 'w')
interim_file = open("cleandata.txt", 'w')

Del_Brands = ['NM ','NV ','OR ','UT ','NOC Prod ePlanning',\
'NOC Train ePlanning','CaDev ','CaProd ','CaProd Performance Test',\
'CaTest ','CaMobile ','ct? Test ','ct1 ','ct10vm_','ct13vm_', 'ilmntcc2',\
'ilmntcc','ct2 ','ct3 ','ct7 ','Copy of NOC EGIS Test ','Copy of NOC EGIS ',\
'NOC Prod ePlanning ','NOC Train ePlanning ','NOC Test ePlanning ',\
'NOC EGIS ','NOC GPM ','NOC Dev ePlanning ', ' on 1021',' on 1031','on 1041',\
# ' 1021',' 1031', # These are version numbers, i.e., ArcInfo 10.2.1
' on ct5?', ' on 4?', ' on 41', ' on 42', ' on ct44',\
' on ap32',' on AP35',' on CT0?-0?',' on CT04-01',' on CT04-03',\
' on CT05-01',' on CT05-02',' on CT05-03'' on CT05-04',' on CT14',\
' on CT21',' On CT43',' On CT44',' On ct44',' On CT45',' On CT46',\
' On CT47',' On CT48',' on CT45',' on CT46',' on CT47',' on CT48',\
' On CT53',' On CT54',' On CT55',' On CT56',' On CT4?',' On CT??',\
' on 49',' on 40',' Test82', ' Test83','ES EGIS ','NOC ',\
',<not reported>', '<not reported>,','<not reported>','<none>,',\
'Win2008R2 6.1.7601','Win2012R2 6.3.9600',' (Instance001)', '<none.,',\
' (Instance002)',' ()',' ( )','()',' (TM)', ' v ',' v.', ' V ', '[]']

linesProcessed = 0
unique_products = 0
prev_line = ""

# Delete header line
f.readline()

while True:
   line = f.readline()
   if len( line ) == 0: break

# Substitutions

   if "(C:\fsapps\fsprod\fam\du\)" in line:
      line = line.replace('(C:\fsapps\fsprod\fam\du\)', '')
   if "(C:\Program Files (x86)\DTS\)" in line:
      line = line.replace('(C:\Program Files (x86)\DTS\)', '')
   if "(C:\Program Files (x86)\DTS\) #3" in line:
      line = line.replace('(C:\Program Files (x86)\DTS\) #3', '')
   if "(C:\Program Files (x86)\DTS\) #4" in line:
      line = line.replace('(C:\Program Files (x86)\DTS\) #4', '')
   if "(CI26_qkb1)" in line:
      line = line.replace('(CI26_qkb1)', '')
   if "(CI27_qkb1)" in line:
      line = line.replace('(CI27_qkb1)', '')
   if "(CI28_qkb1)" in line:
      line = line.replace('(CI28_qkb1)', '')
   if "- N/A" in line:
      line = line.replace('- N/A', '')
   if "...6)\Onset Computer Corporation\HOBOware Pro" in line:
      line = line.replace('...6)\Onset Computer Corporation\HOBOware Pro', 'HOBOware Pro')
   if "...iles (x86)\Onset Computer Corporation\HOBOware" in line:
      line = line.replace('...iles (x86)\Onset Computer Corporation\HOBOware', 'HOBOware')
   if "... (x86)\Onset Computer Corporation\HOBOware" in line:
      line = line.replace('... (x86)\Onset Computer Corporation\HOBOware', 'HOBOware')
   if "Command |" in line:
      line = line.replace('Command |', 'Command /')
   if "Dell Data Protection | Access | Drivers | 2.01.018" in line:
      line = "Dell Data Protection / Access / Drivers | 2.01.018"
   if "Dell Data Protection | Access | Middleware | 2.01.010" in line:
      line = "Dell Data Protection / Access / Middleware | 2.01.010"
   if "| Access" in line:  
      line = line.replace('| Access', '/ Access')
   if "???????? ????? " in line:
      line = line.replace('???????? ????? ','')
   if "V.9.6.5" in line:
      line = line.replace('V.9.6.5','')
   if "CPS R" in line:
      line = line.replace('CPS R','CPS')
   if "FRCC Software Application ." in line:
      line = line.replace(' .','')

# Getting rid of ES without getting rid of RES  9/28/2018
   if "RES" in line:
      line = line.replace('RES','RZ+Z')
# Similarly fixing AccXES and ZELOTES
   if "AccXES" in line:
      line = line.replace('AccXES','AccXZ+Z')
   if "ZELOTES" in line:
      line = line.replace('ZELOTES','ZELOTZ+Z')
   if "ES " in line:
      line = line.replace('ES ','')
   if "Z+Z" in line:
      line=line.replace('Z+Z', 'ES')
# Getting rid of AK without getting rid of Kodak 
   if "KODAK" in line:
      line = line.replace('KODAK', 'KODAZO')
   if "AK " in line:
      line = line.replace('AK ', '')
   if "KODAZO" in line:
      line = line.replace('KODAZO', 'KODAK')
# Getting rid of CA without getting rid of PCA
   if "PCA" in line:
      line = line.replace('PCA', 'PZ+Z')
# Similarly fixing Citrix ICA Client
   if "ICA Client" in line:
      line = line.replace('ICA', 'IZ+Z')
# Similarly fixing LEICA Geo Office
   if "LEICA Geo" in line:
      line = line.replace('ICA', 'IZ+Z')
   if "CA " in line:
      line = line.replace('CA ', '')
   if "PZ+Z" in line:
      line = line.replace('PZ+Z', 'PCA')
   if "IZ+Z" in line:
      line = line.replace('IZ+Z', 'ICA')
   if "eRedBook" in line:
      line = line.replace('11)', '11')
   if "HP for Controller" in line:
      line = line.replace('HP for ','HP NV for ')
   if "HP for Load" in line:
      line = line.replace('HP for ','HP NV for ')
   if "RICOH_Media_Driver_v " in line:
      line = line.replace('_v','')
   if "RFIDDiscoverV" in line:
      line = line.replace('V','')
   if "(Build ) " in line:
      line = line.replace('(Build ) ','')
# Delete the word Version, but preserve it in a few cases
   if ".NET Version Manager" in line:
      line = line.replace('Version','Z+Z ')
   if "MicroFish 3.0 Demonstration Version" in line:
      line = line.replace('Version','Z+Z ')
   if "Implementing Versioned Workflows" in line:
      line = line.replace('Version','Z+Z ')
   if "PDLCONF User Version" in line:
      line = line.replace('Version','Z+Z ')
   if "Version " in line:
      line = line.replace('Version','')
   if ".NET Z+Z Manager" in line:
      line = line.replace('Z+Z ','Version')

# Some Replacements
   if "Redistributable -" in line:
      line = line.replace('Redistributable -', 'Redistributable ')
   if ' ()' in line:
      line = line.replace(' ()','')
   if "()" in line:
      line = line.replace('()', '')
   if ' []' in line:
      line = line.replace(' []','')
   if line.endswith(" |"):
      line = line.replace(' |', '')
   if "  " in line:
      line = line.replace('  ', ' ')
   if "  " in line:
      line = line.replace('  ', ' ')
   if "  " in line:
      line = line.replace(' .0 ', ' ')


# Patches are removed because they are not products
   if ' Patch' in line: continue
   if '(patch ' in line: continue
   if '(Patch ' in line: continue
# Remove junk
   if line.startswith("|"): continue
   if '" | "' in line: continue
   if '" | ' in line: continue
   if 'CharacterSetResult' in line: continue #Gets rid of lines that blew out because of a non-ASCII Character
# The next three lines removed a really pesky line in the data that was just a double quote and a carriage return.
   if line == '"': continue
   if '"' in line:
      line = line.replace('"', '')
   if len(line) == 1: continue
   if 'Inspector interrupted.' in line: continue
   if 'WindowsCharacterSetResult: Error 111' in line: continue
   if 'Singular expression refers to nonexistent object.' in line: continue
   line = line.strip()
   line = line.lstrip()
   for DelItem in Del_Brands:
      line = line.replace(DelItem, "")
   if "  " in line:
      line = line.replace("  ",  " ")
   if "- |" in line:
      line = line.replace("- |",  "|")
# Eliminate version numbers in application names when version numbers are provided
   s_line = line.split(" | ")
   if len(s_line) > 1:
      if s_line[0] == s_line[1]: 
         line = s_line[0].replace(" "," | ")
         line = line.lstrip()
         line = line.replace("\t","")
         if " 	BehavePlus" in line:
            line = line.replace(" 	BehavePlus", "BehavePlus")
      else:
         if s_line[1] in s_line[0]:
            prodname = s_line[0].replace(s_line[1],"")
            line = prodname.strip() +" | "+s_line[1]


   if " V " in line:
      line = line.replace(' V ', '')
   if " v " in line:
      line = line.replace(' v ', '')
   if " ()" in line:
      line = line.replace(' ()', '')



# Get rid of leading spaces
   line = line.lstrip()

# Output the line with the pipes to be used in the count
   pipes.write( line.rstrip() + '\n' )
   interim_file.write( line.rstrip() + '\n' )

   linesProcessed += 1

# make the line tab-separated
#   line = line.replace('| ','\t')
# Just output one copy of each unique product
   line = s_line[0]
   if line != prev_line:
      of.write( line.rstrip() + '\n' )
      prev_line = line
      unique_products += 1
   
# Output the line to the output file with tabs instead of piping symbols for comparison to FEAF
#   of.write( line.rstrip() + '\n' )



# end of while True: loop.

f.close()
of.close()

t2 = time.time()
t3 = t2 - t1
t4 = t3/60
t5 = t3%60
print('Scrubbed %d lines and identified %d unique products in %d minutes and %d seconds\a\n' % (linesProcessed, unique_products, t4,t5))
