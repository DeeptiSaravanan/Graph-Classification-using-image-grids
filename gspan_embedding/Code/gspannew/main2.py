from algorithms import g_span as gSpan
from algorithms import load_graphs
from algorithms import compute_support
import numpy as np
import random

train_test_split = 0.7
path_to_graph_dataset = "data/trial.txt"

def get_subgraphs_for_each_graph(graphs, graphs_list):
    
    n = len(graphs)
    subgraphs = {}
    
    for i in range(n):
        subgraphs[i] = []

    for i, graph in enumerate(graphs_list):
        for j in graph:
            subgraphs[j].append(i)
            
    return subgraphs


def get_graphs_for_each_subgraph(extensions, graphs):
    
    graphs_list = []
    support = []
    for i, ext in enumerate(extensions):
    #print('Pattern %d' % (i+1))
        #for _c in ext:
        #    print(_c)
        # print('')
        graph = []
        sup = compute_support(ext, graphs, graph)
        support.append(sup)
        graphs_list.append(graph)
        
    return graphs_list, support

def gspan(train_test_split, path_to_graph_dataset, min_sup):
    graphs=[]
    graph = load_graphs(path_to_graph_dataset)
    n = len(graph)
  
    idxs = np.arange(0,n,1)
   
    random.shuffle(idxs)
    #graphs = graph[idxs.tolist()]
   # print idxs
    for e in idxs:
    	graphs.append(graph[e])
	#print e
    #print graphs
    

    with open("/home/N1801734D/grid/graph_2D_CNN/datasets/classes/test/test_classes.txt", 'r') as f:
        y = f.read().splitlines()
        y = [int(elt) for elt in y]
    for e in y:
    	ys = y[e]
   # print("number of graphs: ", n)
    
    np.save("shuffled_graph_idxs", idxs)

    train_graphs = graphs[:(int)(train_test_split*n)]
    test_graphs = graphs[(int)(train_test_split*n):]
    
    #print("number of graphs for train: ", len(train_graphs), " for test: ", len(test_graphs))

    extensions = []
    gSpan([], train_graphs, min_sup=30, extensions=extensions)

    #with open("out.txt","w") as f:
    for i, ext in enumerate(extensions):
    #print('Pattern %d' % (i+1))
    	for _c in ext:
      		print(_c)
    			#f.write(_c)
    	print('')
    		#f.write('')
    
    
    #print("Compute subgraphs list in train graphs: ")
    support, train_graphs_list = get_graphs_for_each_subgraph(extensions=extensions, graphs=train_graphs)
    train_subgraphs_list = get_subgraphs_for_each_graph(graphs=train_graphs, graphs_list=train_graphs_list)
    
    for i in range(len(train_graphs)):
        np.save("id/train_np/g_" + str(i), np.array(train_subgraphs_list[i]))
        with open("id/train/g_" + str(i) + ".txt","w") as f:
        	f.writelines(["%s " % item for item in train_subgraphs_list[i]])
        #print(train_subgraphs_list[i])
    
    #print("Compute subgraphs list in test graphs: ")
    _, test_graphs_list = get_graphs_for_each_subgraph(extensions=extensions, graphs=test_graphs)
    test_subgraphs_list = get_subgraphs_for_each_graph(graphs=test_graphs, graphs_list=test_graphs_list)
    
    for i in range(len(test_graphs)):
        np.save("id/test_np/g_" + str(i), np.array(test_subgraphs_list[i]))
        with open("id/test/g_" + str(i) + ".txt","w") as fo:
        	fo.writelines(["%s " % item for item in test_subgraphs_list[i]])
        #print(test_subgraphs_list[i])

    np.save("extensions", extensions)
    np.save("support", support)


gspan(train_test_split=train_test_split, path_to_graph_dataset=path_to_graph_dataset, min_sup=1)
#for i, ext in enumerate(extensions):
    #print('Pattern %d' % (i+1))
 #   for _c in ext:
  #     print(_c)
   # print('')
    
