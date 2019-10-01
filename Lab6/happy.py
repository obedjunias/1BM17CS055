with open("./happy.txt","r") as h:
    fh = h.read()
    h_l = fh.split(" ")
with open("./prime.txt","r") as p:
    ph = p.read()
    p_l = ph.split(" ")

for each1 in h_l:
    if each1 in p_l:
        print(each1,end = " ")
