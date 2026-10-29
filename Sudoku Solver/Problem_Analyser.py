class SudokuAnalyser:
    def __init__(self,sudoku_grid:list[list[int]]):
        self.grid=sudoku_grid
        self.p_layer:list[list[list[float]]]=[[[None for i in range(9)]for i in range(9)]for i in range(9)]
        self.counter=0
        self.p_layer_list:list[list[list[list[float]]]]=[]
        self.grid_updates:list[list[list[int]]]=[] #[layer_no][list of updates in grid][i,j]
        self.quick_access:list[list[list[int]]]=[[] for i in range(9)] #[number-1][list of locations][i,j]
        self.remaining_number=[9 for i in range(9)]
        
    def initial_cleaner(self):
        for i in range(9):
            for j in range(9):
                if(self.grid[i][j]!=0):
                    for k in range(9):
                        self.p_layer[i][k][self.grid[i][j]-1]=0
                        self.p_layer[k][j][self.grid[i][j]-1]=0
                        self.p_layer[i][j][k]=0
                    for k in range(3):
                        self.p_layer[i][j-(j%3)+k][self.grid[i][j]-1]=0
                        self.p_layer[i-(i%3)+k][j][self.grid[i][j]-1]=0
                    self.counter+=1
                    self.quick_access[self.grid[i][j]-1].append([i,j])
                    self.remaining_number[self.grid[i][j]-1]-=1
        self.grid_updates.append(self.quick_access)
        for i in range(9):
            if len(self.quick_access[i])!=0:
                for j in self.quick_access[i]:
                    self.p_layer[j[0]][j[1]]=[i+1]
    
    def layer_probability(self):
        
        pass
    
    def layer_update(self):
        tem:list[list[int]]=[]
        for i in range(9):
            for j in range(9):
                if(len(self.p_layer[i][j])!=1):
                    for k in self.p_layer[i][j]:
                        if(k==1):
                            tem.append([i,j])
                            self.grid[i][j]=self.p_layer[i][j].index(1)+1
                            self.quick_access[self.grid[i][j]-1].append([i,j])
    
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
p1.initial_cleaner()
print(p1.remaining_number)

