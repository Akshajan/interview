a  = []
n=3
for i in range(1,n+1):
    for j in range(1,n+1):
        if j%i!=0:
            continue
        
        a.append((i,j))
        

            
print(a)
        
        