
def convert(fname, n):
    cities = []
    ofname = fname.split('.')[0] + str(n) + '.csv'
    with open(fname) as f:
        for _ in range(n+1):
            cities.append(f.readline())

    for line in cities:
        print(line)

    for l in cities[-1].split():
        print(l)

    print(ofname)
    with open(ofname, 'w') as f:
        f.write("City,Lat,Long\n") 
        for l in cities[1:]:
            line = l.split()
            f.write("{},{},{}\n".format(line[1],line[3],line[4]))
        
