import numpy as np
import csv
import os
from sklearn.decomposition import PCA

d = '/home/N1801734D/example/graph2vec_tf/embeddings/'
e = '/home/N1801734D/gspannew/id/test/'
out = '/home/N1801734D/grid/graph_2D_CNN/datasets/ten/test/'
filenames=[]
i=0
length = 0
res=[]

for filename in os.listdir(e):
	length = length+1

while i < length:
	print "loading subgraph files"
	with open(e+"g_" + str(i) + ".txt", "r") as f:
		contents = csv.reader(f, delimiter=" ")
		#print contents
		for t in contents:
			for j in t:
				if j <> "" and j <> "\n":
					filenames.append(d+str(j)+".gexf.g2v3")
	#print filenames
	k=0
	print "Getting contents"
	while k < len(filenames):
		f1 = filenames[k]
		#print "opening " + f1
		with open(f1,"r") as f:
			c1 = f.read()
			c11 = c1.replace(","," ")
			res.append(c11)
	
		k=k+1

#f1 = filenames[0]
#f2 = filenames[1]

#with open(f1,"r") as f:
#	c1 = f.read()
#	c11 = c1.replace(","," ")
	#print c1
	#print "####################################################################################"

#with open(f2,"r") as f:
#	c2 = f.read()
#	c22 = c2.replace(","," ")
	#print c2

#res = []
#res.append(c11)
#res.append(c22)
	print "Saving as .emb file"

	with open("lol/test/lol_"+str(i)+".emb","w") as f:
		for item in res:
			f.write("%s\n" % item)

	with open("lol/test/lol_"+str(i)+".emb","r") as f:
        	con = f.read()
        	con1 = con.replace("["," ")
        	con2 = con1.replace("]"," ")
	
	with open("lol/test/lol_"+str(i)+".emb","w") as f:
		f.write(con2)
	print "Loading .emb file"

	emb = np.loadtxt("lol/test/lol_"+str(i)+".emb")
#emb=emb[emb[:,0],1:]
	print "Saving as numpy array"
	#emb = emb.reshape(-1,1)
	#emb = emb[emb[:,0].argsort(),1:]
	#my_pca = PCA(n_components=10)
	#pca_output = my_pca.fit_transform(emb)

	np.save(out+str(i),emb,allow_pickle=True)
	filenames=[]
	res=[]
	#print "This iteraion ends here"
	i=i+1		
			
				
