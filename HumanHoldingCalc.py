p0 = 0.04393
p1 = 0
relsize = 13.812154696132596685082872928177
rs = relsize

p2 = (p1-p0)*relsize+p1
print("p2: " + str(p2))

p3correct = (p2-p1)*relsize+p2
p3 = ((p1-p0)*relsize)*(relsize+1)+p1
print("p3 (correct): " + str(p3correct))
print("p3 (possible): " + str(p3))

p4correct = (p3-p2)*relsize+p3
p4 = (p2-p1)*rs**2+p3
print("p4 (correct): " + str(p4correct))
print("p4 (possible): " + str(p4))

p5correct = (p4correct-p3correct)*relsize+p3correct
p5 = p1*((rs+1)**3-(rs+1)*rs)-(p0*rs)*((rs+1)**2-rs)-(p1*rs)*(rs+1)
print("p5 (correct): " + str(p5correct))
print("p5 (possible): " + str(p5))