import networkx as nx
import matplotlib.pyplot as plt

def show_wgraph():
    
    node_pos = {'A':(1,2),'B':(2,1),'C':(2,3),'D':(3,3),'E':(4,1),'F':(5,3)}
    plt.figure() 
    
    weight_labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx(G,node_pos,font_color = 'white', node_shape = 's', with_labels = True,)
    output = nx.draw_networkx_edge_labels(G,node_pos,edge_labels=weight_labels)
    
G = nx.DiGraph()

G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')
G.add_node('F')

G.add_edge('A', 'B', weight=3)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'E', weight=3)
G.add_edge('C', 'D', weight=8)
G.add_edge('E', 'F', weight=4)
G.add_edge('D', 'F', weight=2)
G.add_edge('B', 'D', weight=4)
G.add_edge('E', 'D', weight=4)

show_wgraph()