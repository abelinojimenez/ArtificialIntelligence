"""
        ###################################################
        ####       CRITICAL PATH SOURCE                ####
        ####        Artificial Inteligence             ####
        ####   coding by Carlos Abelino Jimenez Garcia ####
        ###################################################
"""
from collections import deque   # import dequeue librery from collections for use eficient queue pop() function
class Activity:
    def __init__(self):
        self.INF=10e9
        self.ES=-(self.INF)
        self.EF=0
        self.LS=0
        self.LF=self.INF
        self.value=0
        self.name=""
        self.visit=0 # this flag change when BFS(realy djikstral for the relaxation function ) is apply
class Critical_Path:
    def __init__(self):
        self.start=Activity()
        self.target=Activity()
        self.listname=["inicio"]
        self.nodes=[]
        self.nodes.append(self.start)
        self.adj=[]  # adyacent for travel left to right
        self.Iadj=[] # inverter adyacent for travel right to left
        self.index=1
        self.numberActivity=2
        # template values when us create node
        self.tmpval=0
        self.tmpname=""
        self.listPadj=[]
        # list of the path critical
        self.listcritical=[]
    def getdata(self):
        self.numberActivity=int(input("ingresa la cantidad de actividades a llenar: "))
        self.numberActivity+=2
        # start adjacent list with N lists in lists
        for x in range(self.numberActivity):
            self.adj.append([])
            self.Iadj.append([])
        self.tmpNumActivity=self.numberActivity
            # get data to the N activity    
        while (self.tmpNumActivity-2)>0:
            self.tmpname=input("ingresa el nombre de la actividad: ")
            self.tmpval=int(input("ingresa el valor de la actividad: "))
            
            self.listPadj= (input("ingrese predecesores formato:   A   o  A,B,C: ")).split(",")
            if self.listPadj==['']: # repair if split fail
                    self.listPadj=[]
            # register node
            self.listname.append(self.tmpname)
            newnode=Activity()
            newnode.name=self.tmpname
            newnode.value=self.tmpval
            self.nodes.append(newnode)
            #add adjacent node with predecesor
            if len(self.listPadj)==0:
                self.adj[0].append(len(self.listname)-1)
                self.Iadj[len(self.listname)-1].append(0)
            else:
                for nod in range(0,len(self.listPadj)):
                    # first us identificate in listname the index ,for we'll do it, fist search in the list previo node(activitys) and get name ,second this number add adjacen with actual activity  
                    self.adj[self.listname.index(self.listPadj[nod])].append(len(self.listname)-1)
                    self.Iadj[len(self.listname)-1].append(self.listname.index(self.listPadj[nod]))

            print("----------------------------------------------------------------------")
            self.tmpNumActivity-=1
        
        self.listname.append("final"); #add final name node 
        self.nodes.append(self.target) #add real final data node to the list
        self.tmpNumActivity=self.numberActivity
        # connected node without predecesor
        for nod in range(0,len(self.listname)-1):
            if len(self.adj[nod])==0 :
                self.adj[nod].append(len(self.listname)-1)
                self.Iadj[len(self.listname)-1].append(nod)
    def prinadj(self):
        print(self.adj)
        print(self.Iadj)
        for n in self.nodes:
            print(n.EF,n.LF)
    def travelPath(self):
        #first part we trasvel left to right(start to target) do relaxation MAX value in one by one node conection.
        q=deque()
        q.append(0)
        while len(q)!=0:
            node=q.popleft()
            for adyacent in self.adj[node]:
                # update weight relaxation node
                if self.nodes[adyacent].ES<self.nodes[node].EF:
                    self.nodes[adyacent].ES=self.nodes[node].EF
                    self.nodes[adyacent].EF=self.nodes[adyacent].ES+self.nodes[adyacent].value
                if self.nodes[adyacent].visit==0:
                    q.append(adyacent)
                self.nodes[adyacent].visit=1
        self.nodes[len(self.listname)-1].LF=self.nodes[len(self.listname)-1].EF
        self.nodes[len(self.listname)-1].LS=self.nodes[len(self.listname)-1].LF-self.nodes[len(self.listname)-1].value
        #second step is part to the target to the start do relaxation MIN value in one by one node conection.
        q.append(len(self.listname)-1)
        while len(q)!=0:
            node=q.popleft()
            for adyacent in self.Iadj[node]:
                # update weight relaxation node
                if self.nodes[adyacent].LF>self.nodes[node].LS:
                    self.nodes[adyacent].LF=self.nodes[node].LS
                    self.nodes[adyacent].LS=self.nodes[adyacent].LF-self.nodes[adyacent].value
                if self.nodes[adyacent].visit==1:
                    q.append(adyacent)
                self.nodes[adyacent].visit=0
        # getCriticalPath is a method do DFS algorithm modification by get Only EF-LF=0
    def dfs(self,source,onePath,target):
        if source==target:
            self.listcritical.append(list(onePath))
            return
        for nod in self.adj[source]:
            if self.nodes[nod].EF==self.nodes[nod].LF:
                onePath.append(nod)
                self.dfs(nod,onePath,target)
                onePath.pop()
    def getCriticalPath(self):
        onePath=[0]
        self.dfs(0,onePath,len(self.listname)-1)
        return self.listcritical
    def nameCritical(self):
        for lis in self.listcritical:
            sumpath=0
            for nod in lis:
                print(self.listname[nod],"-->"),
                sumpath+=self.nodes[nod].value
            print("la suma de tareas es = ",sumpath)
            print("\n")

    
            
                
                    
        
            
path=Critical_Path()
path.getdata()
path.travelPath()
#path.prinadj()
path.getCriticalPath()
path.nameCritical()
