from ntpath import join
from typing import Dict
from node import VariableNode
from queue import Queue
import utils
import numpy as np
import networkx as nx
import time

def sumProduct(graph : nx.DiGraph):
    rootNode = utils.getRootFrom(graph)
    leavesNodes = utils.getLeavesFrom(graph)

    passingMessage(leavesNodes, graph, False)
    passingMessage(rootNode, graph, True)

    return

def getMarginals(graph : nx.DiGraph) -> Dict:
    marginals = {}
    
    for n in graph.nodes:
        if (isinstance(n, VariableNode)):
            currentMarginal = 1
            for neighbor in graph.predecessors(n):
                currentMarginal = currentMarginal * neighbor.getMessage()
            for neighbor in graph.successors(n):
                currentMarginal = currentMarginal * neighbor.getMessage()
            marginals[n.name] = currentMarginal
    return marginals

def brutalForce(cardinality):
    marginals = dict()

    jointMatrix = np.random.randint(0, cardinality, size = (cardinality, cardinality, cardinality, cardinality, cardinality))
    for i in range(cardinality):
        marginals[i] = np.sum(jointMatrix)
    return marginals


def passingMessage(startingNodes, graph : nx.DiGraph, backwards = False):

    pendingNodes = Queue()
    pendingNodesSet = set()
    visitedNodes = set()

    # Add leaves to the queue
    for n in startingNodes:
        pendingNodes.put(n)
        pendingNodesSet.add(n)

    while (not pendingNodes.empty()):
        n = pendingNodes.get()
        pendingNodesSet.remove(n)

        if (not n.passingMessage(utils.getNodes(n, graph, backwards, True))):
            pendingNodes.put(n)
            pendingNodesSet.add(n)
        else:
            visitedNodes.add(n)
        
        for neighbor in utils.getNodes(n, graph, backwards, False):
            if (not visitedNodes.__contains__(neighbor) and not pendingNodesSet.__contains__(neighbor)):
                pendingNodes.put(neighbor)
                pendingNodesSet.add(neighbor)
    return

if __name__ == "__main__":
    cardinality = 50
    
    st = time.time()

    graph = utils.mkFactorGraph(cardinality)
    sumProduct(graph)
    marginals = getMarginals(graph)

    et = time.time()

    # get the execution time
    elapsed_time = (et - st) / 1000

    print("The sum-product algorithm is finished and needs {} ms".format(elapsed_time))

    st = time.time()

    marginals = brutalForce(cardinality)

    et = time.time()

    # get the execution time
    elapsed_time = (et - st) / 1000

    print("The brutal force algorithm is finished and needs {} ms".format(elapsed_time))
