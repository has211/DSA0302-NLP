import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

nodes = ["John","Mary","He","a ball","She","it","him","they all","dog"]
G.add_nodes_from(nodes)

accepted = [
    ("John","He"),
    ("Mary","She"),
    ("a ball","it"),
    ("John","him"),
    ("John","they all"),
    ("Mary","they all"),
    ("a ball","they all"),
    ("dog","they all")
]

rejected = [
    ("Mary","He"),
    ("John","She"),
    ("John","it"),
    ("Mary","it"),
    ("Mary","him"),
    ("a ball","He"),
    ("a ball","She"),
    ("dog","He"),
    ("dog","She")
]

pos = {
    "John":(0,2),"Mary":(2,2),"He":(0,1),
    "a ball":(4,2),"She":(2,1),"it":(4,1),
    "him":(0,0),"they all":(3,0),"dog":(5,0)
}

nx.draw_networkx_nodes(G,pos,node_color="lightblue",node_size=2200)
nx.draw_networkx_labels(G,pos,font_size=10,font_weight="bold")
nx.draw_networkx_edges(G,pos,edgelist=accepted,edge_color="green",width=2,arrows=True)
nx.draw_networkx_edges(G,pos,edgelist=rejected,edge_color="red",style="dashed",width=1.5,arrows=True)

plt.title("Q1 Constraint Graph - Coreference Resolution")
plt.axis("off")
plt.tight_layout()
plt.show()
