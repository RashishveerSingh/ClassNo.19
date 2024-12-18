tuplulupepelele = (1,1,0,0,1,0,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,)

sunny = 0
rainy = 0

for i in range (0,len(tuplulupepelele)):
    if tuplulupepelele[i] == 1:
        sunny =+ 1
    else:
        rain =+ 1
if sunny>rain:
    print("good weather")
else:
    print("bad weather")