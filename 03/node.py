from abc import abstractmethod
import numpy as np
import networkx as nx

class Node(object):
    def __init__(self, name : str, id : int) -> None:
        self.name = name
        self.id = id
        self.message = None
    
    @abstractmethod
    def passingMessage(self, incomingNodes) -> bool:
        pass

    def getMessage(self) -> float:
        return self.message

class VariableNode(Node):
    """ Variable node in factor graph
    """
    def __init__(self, name : str, id : int):
        super(VariableNode, self).__init__(name, id)
        return

    def passingMessage(self, neighbors) -> bool:
        """ Multiplies together incoming messages to make new outgoing
        """
        mulIncoming = 1
        for node in neighbors:
            if (node.getMessage() is None):
                return False
            mulIncoming = node.getMessage() * mulIncoming
        self.message = mulIncoming
        return True


class FactorNode(Node):
    """ Factor node in factor graph
    """
    def __init__(self, functionFactor : np.ndarray, name : str, id : int) -> None:
        super(FactorNode, self).__init__(name, id)
        self.functionFactor = functionFactor
        return

    def passingMessage(self, neighbors) -> bool:
        """ Multiplies incoming messages with functionFactor to make new outgoing
        """
        mulIncoming = 1
        for node in neighbors:
            if (node.getMessage() is None):
                return False
            mulIncoming = node.getMessage() * mulIncoming

        self.message = np.sum(np.multiply(self.functionFactor, mulIncoming))
        return True