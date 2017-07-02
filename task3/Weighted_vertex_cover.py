
# coding: utf-8

# In[15]:

print("введите количество вершин и количество ребер")
numberV, numberE = map(int, input().split(' '))

print("введите вес каждой вершины через enter")
sizeV = []
for i in range(numberV):
    sizeV.append(int(input()))
    
print("введите номера концов(через пробел) каждого ребра через enter")
beE = []
for i in range(numberE):
    bE, eE = map(int, input().split(' '))
    beE.append((bE, eE))

dict_sizeV = {}
number = 1
for i in sizeV:
    dict_sizeV[number]=i
    number += 1


dict_sizeVCh = {}
number_ = 1
for i in range(numberV):
    dict_sizeVCh[number_] = 0
    number_ += 1
    
edge_id = 0
valid_edges = 0
while True:
    
    if edge_id == len(beE):
        edge_id = 0
        
        if valid_edges == 0:
            break
            
        valid_edges = 0
        
    edge = beE[edge_id]
    edge_id += 1
        
        
    if ((dict_sizeVCh[edge[0]] < dict_sizeV[edge[0]]) and (dict_sizeVCh[edge[1]] < dict_sizeV[edge[1]])):
        yE = min(dict_sizeV[edge[0]]-dict_sizeVCh[edge[0]], dict_sizeV[edge[1]]-dict_sizeVCh[edge[1]])
        dict_sizeVCh[edge[0]] += yE
        dict_sizeVCh[edge[1]] += yE
        
    
vertexOpt = []    
for i in range(numberV):
    id = i+1
    if dict_sizeV[id] == dict_sizeVCh[id]:
        vertexOpt.append(id)
    
for v in vertexOpt:
    print(v, end=' ')

