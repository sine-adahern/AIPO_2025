n = (input())

n_indivdual =[]

for i in n:
    i = int(i)
    n_indivdual.append(i)

k = 0
c = 0
for i in n_indivdual:
    up = i+1
    down = i-1 

    if up == 10:
        c+=0
    else:
        c+=1

    if down == -1 or (down == 0 and k ==0):
        c = c+0
    else:
        c+=1
    
        
    k = k+1
    

print(c)
    
    

        




