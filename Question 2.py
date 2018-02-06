
class Node:
    """ base class """
    def __init__(self, name, cost, utility):
        """

        :param name:
        :param cost:
        :param utility:

        """

        self.name = name
        self.cost = cost
        self.utlity = utility


    def get_expected_cost(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_expected_utility(self):
        """ abstract method to be overridden in derived classes
        :returns expected utility of this node """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

class ChanceNode(Node):

    def __init__(self, name, cost, utility, future_nodes, probs):
        """

        :param name:
        :param cost:
        :param utility:
        :param future_nodes:
        :param probs:
        """

        Node.__init__(self, name, cost, utility)
        self.futureNodes = future_nodes
        self.probs = probs
        self.utlity = utility

    def get_expected_cost(self):
        """
        :return: expected cost of this chance node
        """
        exp_cost = self.cost  # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1
        return exp_cost

    def get_expected_utility(self):
        """
        :return: expected utility of this chance node
        """
        exp_utility = self.utlity
        i = 0
        for node in self.futureNodes:
            exp_utility += self.probs[i] * node.get_expected_utility()
            i += 1
        return exp_utility


class TerminalNode(Node):

    def __init__(self, name, cost, utility):
        Node.__init__(self, name, cost, utility)

    def get_expected_cost(self):
        """
        :return: cost of this chance node
        """
        return self.cost

    def get_expected_utility(self):
        """
        :return: utility of this chance node
        """
        return self.utlity


class DecisionNode(Node):

    def __init__(self, name, cost, utility, future_nodes):
        Node.__init__(self, name, cost, utility)
        self.futureNode = future_nodes

    def get_expected_costs(self):
        """ returns the expected costs of future nodes"""
        outcomes = dict() # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            outcomes[node.name] = node.get_expected_cost()

        return outcomes

    def get_expected_utility(self):
        """ returns the expected costs of future nodes"""
        outcomestwo = dict()  # dictionary to store the expected utility of future nodes along with their names as keys
        for node in self.futureNode:
            outcomestwo[node.name] = node.get_expected_utility()

        return outcomestwo


#Terminal Nodes (include: name, cost, utility)
T1 = TerminalNode('T1', 10, 0.9)
T2 = TerminalNode('T2', 20, 0.8)
T3 = TerminalNode('T3', 30, 0.7)
T4 = TerminalNode('T4', 40, 0.6)
T5 = TerminalNode('T5', 50, 0.5)

#Chance Nodes (include: name, cost, utility, future nodes, probs)
C2 = ChanceNode('C2', 35, 0, [T1, T2], [0.7, 0.3])
C1 = ChanceNode('C1', 25, 0, [C2, T3], [0.2, 0.8])
C3 = ChanceNode('C3', 45, 0, [T4, T5], [0.1, 0.9])

#Decision/D1 (include: name, cost, utility, future nodes)
D1 = DecisionNode('D1', 0, 0, [C1, C3])

# print the expect cost of C1
print(D1.get_expected_costs(), D1.get_expected_utility())
