from data_structures import Stack, Queue

class Node:
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent
        self.successors = []
        if parent:
            parent.add_successor(self)

    def add_successor(self, successor):
        self.successors.append(successor)

    def remove_successor(self, index):
        try:
            del(self.successors[index])
        except IndexError:
            print("No such node")

    def walk(self, func = None):
        if func:
            func(self.value)
        else:
            print(self.value)
        for node in self.successors:
            node.walk(func)


def depth_first_search(goal, 
root = Node("Root!")
main_left_branch = Node("Main left branch", root)
main_middle_branch = Node("Main middle branch", root)
main_right_branch = Node("Main right branch", root)
left_sub_branch_1 = Node("Left sub branch 1", main_left_branch)
left_sub_branch_2 = Node("Left sub branch 2", main_left_branch)
right_sub_branch = Node("Right sub branch", main_right_branch)
root.walk()
nodes = []
root.walk(lambda node: nodes.append(node))
print(nodes)
