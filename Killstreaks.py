import os
import time
from subprocess import call
import random
#Execute the fabricator and kit files to gather the information

execute = False
if execute:
    call(['python','KitCode.py'])
    time.sleep(300)
    call(['python', 'FabricatorCode.py'])

fabPrices = []
fabNames = []
kitPrices = []
kitNames = []

KitFile = open(os.getcwd()+"/MarketStuff/KitValues.txt","r")

# grab killstreak information from files
# sort the information by their lists
#
kitValues = []
for i in KitFile:
    #i[i.find('Prof'):i.find('Kit')+3]
    if i == 0:
        continue
    kitValues.append(i[:-1])

KitFile.close()

#break names from values
for i in range(1,len(kitValues)):
    if kitValues[i].find('Professional Killstreak Kit')==-1:
        kitNames.append(kitValues[i][kitValues[i].find('Prof'):kitValues[i].find('Kit')+3])
        kitPrices.append(kitValues[i][kitValues[i].find('$'):])

FabFile = open(os.getcwd()+"/MarketStuff/FabValues.txt","r")
fabValues = []
for i in FabFile:
    if i == 0:
        continue
    fabValues.append(i[:-1])
FabFile.close()

for i in range(1,len(fabValues)):
    fabNames.append(fabValues[i][fabValues[i].find('Prof'):fabValues[i].find('cator') + 5])
    fabPrices.append(fabValues[i][fabValues[i].find('$') :])

#organize fab prices based on the order of kitprices and kitnames
KillstreakFile = open(os.getcwd()+"/MarketStuff/Killstreaks.txt","w")
KillstreakFile.write("%-60s % -15s % -15s % -17s % -15s" % ('Killstreak Kit:', 'Kit Prices:', 'Fab Prices:','Viability:','Potential Profit:') + "\n")
print(len(fabPrices))
print(fabPrices)
print(len(kitNames))
for i in range(len(kitNames)):
    kitFabPrice = ""
    viability = 'UNVIABLE'
    for j in range(len(fabPrices)):
        if fabNames[j].find(kitNames[i])!=-1:

            kitFabPrice = fabPrices[j]
            break
    x1 = float(kitPrices[i][kitPrices[i].find('$')+1:])
    x2 = 1
    if len(kitFabPrice[kitFabPrice.find('$')+1:])>2:
        x2 = float(kitFabPrice[kitFabPrice.find('$')+1:])

    if x1*.85-5 >x2:
        viability = 'VIABLE'
    PotProfit = ""
    if x1*.85 - (x2+5)>0:
        PotProfit = '$'+str(round((x1*.85 - (x2+5)),2))
        if len(PotProfit)==4:
            PotProfit = PotProfit+'0'


    KillstreakFile.write("%-60s % -15s % -15s % -17s % -6s" % (kitNames[i], kitPrices[i], kitFabPrice,viability,PotProfit ) + "\n")
KillstreakFile.close()
