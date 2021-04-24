def main():
    t=int(input())
    for i in range(t):
        x=[int(x) for x in input().split()]
        c=[]
        
        for j in range(x[0],int((x[-1]+x[0])/2)+1):
            g=0
            for h in range(2,int(j/2)+1):
                if((j%h)==0):
                    g=1
                    break
            if(g==0):
                c.append(j)
                break
        for j in range(x[-1],int((x[-1]+x[0])/2),-1):
            g=0
            for h in range(2,int(j/2)+1):
                if((j%h)==0):
                    g=1
                    break
            if(g==0):
                c.append(j)
                break
        if(len(c)==0):
            print("-1")
        elif(len(c)==1):
            print("0")
        else:
            print(max(c)-min(c))

 # Write code here 

main()
