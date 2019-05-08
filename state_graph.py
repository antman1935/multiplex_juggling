import state_graph_util as util
import matplotlib.pyplot as plt
import networkx as nx
    
class StateGraph:
    def __init__(self, baseState, finalState, capacity, length):
        self.baseState = util.State(baseState, capacity)
        self.finalState = util.State(finalState, capacity)
        self.capacity = capacity
        self.length = length
        self.graph = util.constructStateGraph(self.baseState, self.finalState, self.capacity, self.length)
        self.xGraph = util.convertGraphToNetworkXGraph(self.graph)
        
    def draw(self, name = None):
        plt.subplot(111)
        nx.draw_spring(self.xGraph, with_labels=True)
        
        if name != None:
            plt.savefig(name)

if __name__ == "__main__":
    graph = StateGraph([3, 4, 1], 7)
    graph.draw()