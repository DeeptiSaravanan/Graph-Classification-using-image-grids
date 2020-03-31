with open("out.txt","r") as f:
	c=f.read()
	c1 = c.replace("'","")
	c2 = c1.replace(",","")
	c3 = c2.replace("(","")
	c4 = c3.replace(")","")

with open("out.txt","w") as of:
	of.write(c4)

extensions = open("/home/N1801734D/gspannew/out.txt","r")
C = []

class Graph():
    """
        Implementation of a Graph
    """
    edges, vertices = [], []
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.vertices = []
    def add_vertex(self, vertex):
        self.vertices.append(vertex)
    def add_edge(self, edge):
        self.edges.append(edge)
    #def get_graph_id(self)    
    def get_vertex(self, id):
        for v in self.vertices:
            if v.id == id:
                return v
        raise KeyError('No vertex with the id was found in graph')

class Vertex():
	visited = False
	dfs_id=0	
	def __init__(self, id, label):
		self.id = id
		self.label = label

class Edge():
	def __init__(self, label, from_vertex, to_vertex):
		self.label = label
		self.from_vertex = from_vertex
		self.to_vertex = to_vertex

	def connected_to(self,vertex):
		return verte.id == self.from_vertex.id or vertex.id == self.to_vertex.id


		#for u,v,L_u,L_v,L_uv in enumerate(C):
		#print(C)
		#u = C[0]
		#v = C[1]
		#L_u = C[2]
		#L_v = C[3]\
		#L_uv = C[4]
 		#print(u,v,L_u,L_v,L_uv)

def dfs2g(C):
	G=Graph(id=-1)
	vertices = []
	u = []
   	v = []
	p = []
	L_u = []
	L_v = []
	L_uv = []
	i=0
	n=0
	k=0
	q=0
	#for u,v,L_u,L_v,L_uv in C:		
	while i < len(C):
		
		if(C[i] <> '\n'):
			#u,v,L_u,L_v,L_uv += [e for e in C[i]]
			a,b,c,d,e = C[i].split()
			u.append(a)
			v.append(b)
			#print(u,v)
			L_u.append(c)
			L_v.append(d)
			#L_uv.append(d[4])
			#j = j+1
			#print u
			#print v
			#print L_u
			#print L_v
			
		else:
			j=n;
			#print k
			with open('/home/N1801734D/gspannew/textout/node/node' + str(k) + '.txt','w') as outfile:
				#output = "t" + " " + "id" + " " + "label" + "\n"
				#outfile.write(output)
				while j < len(u):
					if u[j] not in p: 
						output = u[j] + " " + L_u[j] + "\n"
						p.append(u[j])
						outfile.write(output)
					if v[j] not in p:
						output = v[j] + " " + L_v[j] + "\n"
						p.append(v[j])
						outfile.write(output)

			
					j=j+1
				p = []
			with open('/home/N1801734D/gspannew/textout/edge/edge' + str(k) + '.txt', 'w') as outfile:			
				#output = "t" + " " + "start_id" + " " + "end_id" + "\n"
				#outfile.write(output)

				while q < len(u):
					output = u[q] + " " + v[q] + " " + "\n"
					q = q+1
					outfile.write(output)
			n=j
			q=n
			k=k+1	
		i = i+1
	#print u
	#for vertex, label in [(u, L_u), (v,L_v)]:
	#	if not (vertex,label) in vertices:
	#		vertices.append((vertex,label))

	#for v_id, v_label in vertices:
	#Create and add vertex
    	#	v = Vertex(id=v_id, label=v_label)
    	#	G.add_vertex(vertex=v)
     #Add edges
	#for t in C:
	#	print(t)
     #Expand tuple
    	#	u, v, L_u, L_v, L_uv = t
     #Get vertices
    	#	_u, _v = G.get_vertex(id=u), G.get_vertex(id=v)
    # Add edge
    	#	e = Edge(label=L_uv, from_vertex=_u, to_vertex=_v)
    	#	G.add_edge(edge=e)
	return G


for i,ext in enumerate(extensions):
	#print(C[1])
#	for _c in ext:
	C.append(ext)	

#while i < 5:
	#if(C[i] != "\n"):
		#print "t" + j 
   		#print C[i]
		#j = j+1	

dfs2g(C)
#print C[5][8]
	#while i3 < len(C):
		#temp.append(C[i])
	#print len(temp)
	#print temp[0]
		#print(C[i])
		#i = i+1
		#op = dfs2g(temp)
                #print(op)  
