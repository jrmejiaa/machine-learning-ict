import networkx as nx
from numpy import var
from node import *
    
def mkFactorGraph(cardinality : int) -> nx.DiGraph:
    graph = nx.DiGraph()
    # Add all variable nodes
    variableNodes = []
    for i in range(5):
        name = "X" + str(i + 1)
        node = VariableNode(name, hash(name))
        variableNodes.append(node)
        graph.add_node(node)

    # Add all Factors nodes
    factorNodes = []
    for i in range(5):
        name = "F" + str(i + 1)
        # Get the right size for the matrix depending on the function factor
        if (i == 0 or i == 3):
            size = (cardinality, cardinality)
        elif (i == 1):
            size = (cardinality, cardinality, cardinality)
        else:
            size = (cardinality)
        # Create matrix with random numbers
        matrix = np.random.randint(0, cardinality, size = size)
        node = FactorNode(matrix, name, hash(name))
        factorNodes.append(node)
        graph.add_node(node)
    
    # Add edges between the nodes
    graph.add_edge(variableNodes[0] , factorNodes[0])   # x1 to f1
    graph.add_edge(factorNodes[0]   , variableNodes[1]) # f1 to x2
    graph.add_edge(variableNodes[1] , factorNodes[1])   # x2 to f2
    graph.add_edge(factorNodes[1]   , variableNodes[2]) # f2 to x3
    graph.add_edge(factorNodes[1]   , variableNodes[3]) # f2 to x4
    graph.add_edge(variableNodes[2] , factorNodes[2])   # x3 to f3
    graph.add_edge(variableNodes[3] , factorNodes[3])   # x4 to f4
    graph.add_edge(variableNodes[3] , factorNodes[4])   # x4 to f5
    graph.add_edge(factorNodes[3]   , variableNodes[4]) # f4 to x5
    return graph

def getRootFrom(graph : nx.DiGraph):
    # Check the nodes without incoming edges
    root = [n for n,d in graph.in_degree() if d==0]
    if (len(root) != 1):
        raise Exception("There are more than one root ")
    return root

def getLeavesFrom(graph : nx.DiGraph):
    # Check the nodes without outgoing edges
    leaves = [n for n,d in graph.out_degree() if d==0]
    if (len(leaves) < 1):
        raise Exception("There are no leaves in the graph")
    return leaves

def getNodes(n : Node, graph : nx.DiGraph, backwards = False, nodesWithMessage = True):
    if (backwards == True):
        if (nodesWithMessage == True):
            return graph.predecessors(n)
        else:
            return graph.successors(n)
    else:
        if (nodesWithMessage == True):
            return graph.successors(n)
        else:
            return graph.predecessors(n)



