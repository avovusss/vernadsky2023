#Переменные типа a_ggn, b_ggn или a_cc являются вспомогательными переменными, использующихся, например, для циклов.
#Необходимо, чтобы количество столбцов (col) было чётным; row — без разницы.
'''
  //10
 (row) 
   50                     
   40                  
   30                    
   20                     
   10                     
      1 2 3 4 5 6 (col) %10
'''

rowIcol_ = int(input()) #Ввести размеры торта в виде результата формулы (10*row + collumn)
rI = rowIcol_//10   #rI: r = row; «I» обозначает количество строк, по нему измеряется "высота" торта (для удобства)
c_ = rowIcol_%10    #c_: c = collumn; «_» обозначает количество столбцов, по нему измеряется длина торта (для удобства)

square = 0      #Проверка на квадратный торт, требуется для фиксации клетки rI+1 (левой верхней),              
if rI == c_:    #которая фиксируется только тогда, когда торт квадратный.
    square = 1


#fixedCells
fixedCells = []
allFixedCells = []
doWeHaveFixedCells = input('Do we have fixed cells? (y/n) ')
if doWeHaveFixedCells == 'y' or doWeHaveFixedCells == 'Y' or doWeHaveFixedCells == 'н' or doWeHaveFixedCells == 'Н':
    fixedCells = input().split(' ') #Ввести фиксированные клетки в виде (pos) (color)
    for a_fc in range(0, len(fixedCells), 2):
        fixedCells[a_fc] = int(fixedCells[a_fc])
        fixedCells[a_fc+1] = int(fixedCells[a_fc+1])
        allFixedCells.append(fixedCells[a_fc])
        allFixedCells.append(fixedCells[a_fc+1])
        allFixedCells.append((rI-fixedCells[a_fc]//10)*10 + c_-fixedCells[a_fc]%10 + 11)
        allFixedCells.append(1-fixedCells[a_fc+1])
        if fixedCells[a_fc]%10 > int(c_/2):
            fixedCells[a_fc] = (rI-fixedCells[a_fc]//10)*10 + c_-fixedCells[a_fc]%10 + 11
            fixedCells[a_fc+1] = 1-fixedCells[a_fc+1]
            

    
def changecake(row, column, color):   #меняет конкретную клетку в торте на заданный цвет color
    cake[rI-row].insert(column, color)
    cake[rI-row].pop(column-1)
    
def printcake(doIPrintCake7):    #выводит торт на экран в удобной для глаза форме
    for a_pc in range(rI):  
        ans = ''
        for b_pc in range(c_):
            if (rI-a_pc)*10+b_pc+1 in allFixedCells and doIPrintCake7 == 'y':
                if cake[a_pc][b_pc] == 0:   #Примечание: на самом первом выводе выводится исходная позиция торта,
                    ans += ' 0'             #где 0 и 1 — фиксированные клетки (0 — светлая клетка, 1 — тёмная).
                elif cake[a_pc][b_pc] == 1:
                    ans += ' 1'
            else:
                if cake[a_pc][b_pc] == 0:
                    ans += '░░'
                elif cake[a_pc][b_pc] == 1:
                    ans += '▓▓'
                else:
                    ans += str(cake[a_pc][b_pc])
        print(ans)

def cakemirrorer():                 #Отражает левую половину торта на правую половину по точке
    for r_cm in range(1, rI+1):     #симметрии в центре торта, цвета при отражении меняются на противоположные.
        for c_cm in range(1, int(c_/2+1)):
            changecake(rI-r_cm+1, c_-c_cm+1, 1-getcolor(r_cm*10+c_cm))



def getcolor(rowAndColumn):   #На вход подаётся позиция клетки в торте, на выход — цвет клетки.
    column = rowAndColumn%10
    row1 = rowAndColumn//10
    rowFromPos = cake[rI-row1]
    numFromColumn = rowFromPos[column-1]
    return numFromColumn


def getneighbours(posn):    #Узнаёт соседей введённой клетки.
    nghbrs = []
    if posn%10 != c_: 
        nghbrs.append(posn+1)
    if posn//10 != rI: 
        nghbrs.append(posn+10)
    if posn%10 != 1: 
        nghbrs.append(posn-1)
    if posn//10 != 1: 
        nghbrs.append(posn-10)
    return(nghbrs)


def getgraphnbhds(graphList):   #Выводит всех клеток-соседей для введённого списка.
    graphNbhds = []
    for a_ggn in graphList:
        pointNbhds = getneighbours(a_ggn)
        for b_ggn in pointNbhds: 
            if b_ggn not in graphList and b_ggn not in graphNbhds:
                graphNbhds.append(b_ggn)        
    return(graphNbhds)
def checkcake(doIPrintGraph7):  #Создаёт граф, состоящий из одноцветных клеток, начало графа всегда в клетке 11.
    graph = [11]                #Затем ищет клетки такого же цвета (0) в ширину по всему торту, заносит их в список.
    halfOfCake = int(rI*c_/2)   #В конце проверяет длину графа: если она равняется половинее торта, то разрезание правильное.
    for i_cc in range(halfOfCake):
        nbhdsToCheck = getgraphnbhds(graph)
        for a_cc in nbhdsToCheck:
            if getcolor(a_cc) == 0 and a_cc not in graph:
                graph.append(a_cc)
    #if doIPrintGraph7 == 'y':          #Убрать комментарии тут и в cycleCakeChanger (ниже), если 
        #print(graph)                   #требуется вывести граф для каждого выведенного торта.
    if len(graph) != halfOfCake:
        return False

        


#trueCake
fc_tc = 1
cake = [[0 for i in range(c_)] for i in range(rI)]
for a_tc in range(0, len(fixedCells), 2):
    changecake(fixedCells[a_tc]//10, fixedCells[a_tc]%10, fixedCells[a_tc+1])
cakemirrorer()

quality = ''
for i in range(c_-1):
    quality += '——'
print(f'\n {quality}\n')
printcake('y')
print(f'\n {quality}\n')



#cakeAssignment (= cA)
eleven = 0
cA = [] 
for a_ca in range(rI):   
    for b_ca in range(int(c_/2)):
        cA.append((rI-a_ca)*10+b_ca+1)
        if cA[-1] == 11 or cA[-1] in fixedCells:
            cA.pop(-1)
            eleven = -1
if square == 1:
    cA.pop(0)
#print(cA)  #Убрать комментарий для вывода конфигурации порядка изменения торта.



#cycleCakeChanger
ans=0
for a_ccc in range(2**(int(rI*c_/2-1-square-len(fixedCells)/2))):
    strCake = bin(a_ccc)[2:]
    #print(strCake)     #Убрать комментарий для бинарной конфигурации каждого выведенного торта.
    for b_ccc in range(len(strCake)): 
        changecake(cA[b_ccc]//10, cA[b_ccc]%10, int(strCake[-1*b_ccc-1]))
    cakemirrorer()
    if checkcake('1') != False:    
        ans+=1
        printcake('1')      #Убрать комментарии в начале строчек, если нужны правильные разрезания торта;
        print()             #Убрать для всех трёх строчек одну табуляцию, чтобы вывести все разрезания.

        #checkcake('y')     #Убрать комментарии тут и в checkcake(), если требуется вывести граф
                            #светлых клеток (красных) для каждого торта;
                                    
print(f'\n[',ans,']')
