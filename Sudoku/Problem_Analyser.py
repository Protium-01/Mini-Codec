class SudokuAnalyser:
    def __init__(self,sudoku_grid:list[list[int]]):
        self.grid=sudoku_grid
        self.counter=0
        self.pmatrix:list[list[list[list[int]]]]=[[[[0,0,0]for i in range(9)]for i in range(9)]for i in range(9)] #[i][j][value][row,column,box]
        self.pmatrix_list:list[list[list[list[list[int]]]]]=[]
        self.grid_updates:list[list[list[int]]]=[] #[layer_no][list of updates in grid][i,j]
        self.quick_access:list[list[list[int]]]=[[] for i in range(9)] #[number-1][list of locations][i,j]
        self.remaining_count=[9 for i in range(9)]
        self.remaining_numbers=[[i,j]for i in range(9) for j in range(9)]
        
    def initialiser(self):
        tem=[]
        for i in range(9):
            for j in range(9):
                if(self.grid[i][j]!=0):
                    for k in range(9):
                        self.pmatrix[i][k][self.grid[i][j]-1]=[]
                        self.pmatrix[k][j][self.grid[i][j]-1]=[]
                        self.pmatrix[i-(i%3)+int(k/3)][j-(j%3)+(k%3)][self.grid[i][j]-1]=[]
                        self.pmatrix[i][j][k]=[]
                    self.quick_access[self.grid[i][j]-1].append([i,j])
                    self.remaining_count[self.grid[i][j]-1]-=1
                    self.remaining_numbers.remove([i,j])
                    tem.append([i,j])
                    self.counter+=1
        for i in range(9):
            for j in range(9):
                if(self.grid[i][j]==0):
                    for a in range(9):
                        if(len(self.pmatrix[i][j][a])==0):
                            continue
                        for k in range(9):
                            b=0
                            try:
                                self.pmatrix[i][k][a][0]+=1
                                if(j==k):
                                    b+=1
                            except:
                                pass
                            try:
                                self.pmatrix[k][j][a][1]+=1
                                if(k==i):
                                    b+=1
                            except:
                                pass
                            try:
                                self.pmatrix[i-(i%3)+int(k/3)][j-(j%3)+(k%3)][a][2]+=1
                                if(i-(i%3)+int(k/3) == i and j-(j%3)+(k%3) == j):
                                    b+=1
                            except:
                                pass
        self.grid_updates.append(tem)
        self.pmatrix_list.append(self.pmatrix.copy())
        
    def simple_update(self):
        update_counter=0
        tem=[[]for i in range(9)]
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    if(len(self.pmatrix[i][j][k])==0):
                        continue
                    if(min(self.pmatrix[i][j][k])==1):
                        #print(i,j,k+1,":",self.pmatrix[i][j][k])
                        tem[k].append([i,j])
        self.grid_updates.append([])
        self.pmatrix_list.append(self.pmatrix)
        for i in range(9):
            if(tem[i]==[]):
                continue
            for j in tem[i]:
                update_counter+=1
                self.position_updater(i,j[0],j[1])
        if(update_counter==0):
            print("No updates Now!")
        self.counter+=update_counter
     
    def position_updater(self,N,i,j):
        self.grid[i][j]=N+1
        self.grid_updates[-1].append([N+1]+[i+1,j+1])
        for k in range(9):
            self.pmatrix[i][k][N]=[]
            self.pmatrix[k][j][N]=[]
            self.pmatrix[i-(i%3)+int(k/3)][j-(j%3)+(k%3)][N]=[]
            for l in range(9):
                try:
                    self.pmatrix[l][k][N][0]-=1
                except:
                    pass
                try:
                    self.pmatrix[k][l][N][1]-=1
                except:
                    pass
                try:
                    self.pmatrix[i-(i%3)+int(l/3)][j-(j%3)+(l%3)][N][2]-=1
                except:
                    pass
    
    def layer_update(self):
        pass
        
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
                    
p1=SudokuAnalyser([[0,0,1,0,0,2,0,0,4],[0,0,7,5,0,9,6,0,0],[4,0,0,8,3,0,0,5,7],[9,4,0,0,0,7,0,3,2],[0,0,0,3,9,6,0,0,5],[0,7,3,0,8,0,1,0,0],[7,3,4,0,0,0,0,0,0],[8,0,0,7,0,0,4,2,9],[0,9,2,4,0,5,3,0,0]])
p1.initialiser()
print(p1.remaining_numbers)
print(p1.counter)
p1.display()
"""for i in p1.pmatrix:
    for j in i:
        print(j)"""
#print(p1.pmatrix[2][5][0])
p1.simple_update()
#p1.display()
print(p1.grid_updates[-1])
print(p1.counter)
