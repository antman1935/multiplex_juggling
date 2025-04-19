import state_graph_util as util
import matplotlib.pyplot as plt
import networkx as nx
    
class StateGraph:
    def __init__(self, baseState, finalState, capacity, length):
        self.baseState = util.State(baseState, capacity)
        self.finalState = util.State(finalState, capacity)
        self.capacity = capacity
        self.length = length
        self.graph = None
        self.xGraph = None
        self.sequences = None
        
        
    def draw(self, name = None):
        if (self.graph == None):
            self.graph = util.constructStateGraph(self.baseState, self.finalState, self.capacity, self.length)
            self.xGraph = util.convertGraphToNetworkXGraph(self.graph)
        plt.subplot(111)
        nx.draw_spring(self.xGraph, with_labels=True)
        
        if name != None:
            plt.savefig(name)

    def drawTikz(self, name: str):
        if (self.sequences == None):
            self.sequences = util.getMultiplexJugglingSequencesFromStates(self.baseState, self.finalState, self.length)
        print(len(self.sequences))
        content = "\n\n".join([util.drawJugglingSequence(sequence) for sequence in self.sequences])
        self.write_latex_file(name + ".tex", content)


    def write_latex_file(self, filename: str, custom_content: str):
        preamble = r"""\documentclass{article}
        \usepackage[utf8]{inputenc}
        \usepackage{tikz}
        \usetikzlibrary{arrows.meta, positioning, shapes.geometric}

        \title{My TikZ Document}
        \author{}
        \date{}

        \begin{document}

        \maketitle

        """

        ending = r"""
        \end{document}
        """

        with open(filename, "w") as f:
            f.write(preamble)
            f.write(custom_content)
            f.write(ending)

if __name__ == "__main__":
    graph = StateGraph([3, 4, 1], [1, 1, 6], 8, 3)
    graph.drawTikz("example")