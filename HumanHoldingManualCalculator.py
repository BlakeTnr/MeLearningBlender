relsize = 13.812154696132596685082872928177

print("Human holding manual calculator...")
previousxyzinput = input("Input previous XYZ: ")
currentxyzinput = input("Input current XYZ: ")
seperatorcharacter = ","

previousxyzarray = [float(x) for x in previousxyzinput.split(seperatorcharacter)]
currentxyzarray = [float(x) for x in currentxyzinput.split(seperatorcharacter)]

def getNewCord(previousCord, currentCord):
    # (x-x2)*relsize+x
    newCord = (currentCord - previousCord)/relsize+currentCord
    return newCord

def algorithm(previousXYZ, currentXYZ):
    x= getNewCord(previousXYZ[0], currentXYZ[0]);
    y= getNewCord(previousXYZ[1], currentXYZ[1]);
    z= getNewCord(previousXYZ[2], currentXYZ[2]);
    return [x,y,z]

newCords = algorithm(previousxyzarray, currentxyzarray)
print(newCords)