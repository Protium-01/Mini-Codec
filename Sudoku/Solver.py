class Sudoko:
    def __init__(self,problem:list[list[int]]):
        self.grid=problem
        self.missing_count=0
        self.last_update=None
        self.number_count=[0]*9

    def count(self):
        for i in self.grid:
            for j in i:
                if(j==0):
                    self.missing_count+=1
                else:
                    self.number_count[j-1]+=1
    
    def append(self,N,i,j):
        if(self.grid[i][j]==0):
            self.grid[i][j]=N
        else:
            print("Wrong inputs!")

    def convert_into_positionals(self):
        self.a=[[[],[],[]] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if(self.grid[i][j]!=0):
                    self.a[self.grid[i][j]-1][0].append(i)
                    self.a[self.grid[i][j]-1][1].append(j)
                    self.a[self.grid[i][j]-1][2].append((int(j/3)) + (int(i/3))*3) 

    def generate_possibilities(self):
        self.parray=[[]]
        for i in self.a:
            t=[[0,1,2,3,4,5,6,7,8] for p in range(3)]
            for j in i[0]:
                t[0].remove(j)
            for j in i[1]:
                t[1].remove(j)
            for j in i[2]:
                t[2].remove(j)
            arr=[]
            for k in t[2]:
                tem=[]
                a=[i for i in range(3*int(k/3),3*(int(k/3)+1))]
                b=[i for i in range(3*(k%3),3*((k%3)+1))]
                for p in a:
                    for q in b:
                        if(p in t[0] and q in t[1]):
                            tem.append([p,q,k])
                arr.append(tem)
            self.parray.append(arr)
    def display(self):
        for i in range(9):
            if(i%3==0):
                print("-"*25)
            for j in range(9):
                if(j%3==0):
                    print("|",end=" ")
                if(self.grid[i][j]==0):
                    print("_", end=" ")
                else:
                    print(self.grid[i][j],end=" ")
            print("|",end="")
            print()
        print("-"*25)
    
    def solve(self):
        self.count()
        pass 

p1=Sudoko([[0,0,1,0,0,2,0,0,4],[0,0,7,5,0,9,6,0,0],[4,0,0,8,3,0,0,5,7],[9,4,0,0,0,7,0,3,2],[0,0,0,3,9,6,0,0,5],[0,7,3,0,8,0,1,0,0],[7,3,4,0,0,0,0,0,0],[8,0,0,7,0,0,4,2,9],[0,9,2,4,0,5,3,0,0]])
p1.solve()
#print(p1.number_count)
#p1.display()
p1.convert_into_positionals()
"""for i in p1.a:
    print(i,end="\n")"""
p1.generate_possibilities()
for i in p1.parray:
    for j in i:
        print(j,end="\n")
    print()