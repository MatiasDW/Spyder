import csv
#precision 2
with open('mpg.csv') as csvfile:
    mpg= list(csv.DictReader(csvfile))
mpg[:3]


mpg[0].keys()

sum(float(d['cty']) for d in mpg)/ len(mpg)
sum(float(d['hwy']) for d in mpg)/ len(mpg)

"""cylinders= = set(d['cyl'] dor d in mpg)
cylinders

ctympgbycyl = []
for c in cylinders:
    summpg = 0
    cyltypecount = 0
    for d in mpg:
        if d['cyl'] == c:
            summpg += float(d['cty'])
            cyltypecount += 1
    ctympgbycyl.sort(key=lambda x: x[0])
    ctympgbycyl
    
    
vehicleclass = set(d['class'] for d in mpg)
vehicleclass


hwympgbyclass = []

for t in vehicleclass:  #iterateover all the vehicle class
    summpg = 0
    vclasscount = 0
    for d in mpg:
        if d['class']== t:
            summpg += float(d['hwy'])
            vclasscount += 1 #increase the count
    hwympgbyclass.append((t, summpg/vclasscount)) #append the tuple ('class', ' avg mpg')
hwympgbyclass.sort(key=lambda x: x[1])
hwympgbyclass"""



















