import numpy as np
import matplotlib as plt
import importlib
from First_Class import Mancala

class Node:
    def __init__(self, current_state):
        super(Node, self).__init__()
        self.future_states = [] 
        self.mancala = current_state

class Tree:
    
    def createNode(self, state = None , Next_turn = None):
        
        mancala_state = Mancala(Initial_State = state, turn = Next_turn)
        return Node(mancala_state)

    def createTree(self,root,depth):

        if depth == 0:
            return root
        Valid_moves = range(0,6) if root.mancala.turn == 'min' else range(7,13)
        
        for move in Valid_moves:
            Next = root.mancala.move(move)
            child_Node = self.createNode(Next.state,Next.turn) 
            root.future_states.append(self.createTree(child_Node,depth - 1))
        return root

    def search(self, node, data):
        """
        Search function will search a node into tree.
        """
        return


    def deleteNode(self,node,data):
        """
        Delete function will delete a node into tree.
        """
        return


    def traverseInorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        for move in root.future_states:
            if move is not None:
                move.mancala.print()
                self.traverseInorder(move)


if __name__ == "__main__":
    T = Tree()
    m = Mancala()
    N = T.createNode(m.state,m.turn)
    r = T.createTree(N,2)
    T.traverseInorder(N)
