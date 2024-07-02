"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        target = head
        if target == None:
            return None
        nodeDict = dict()
        nodeList = []
        
        first = None
        prev = None
        while True:
            curr = Node(target.val)  
            nodeDict[id(target)] = curr

            if target.random != None:
                if id(target.random) in nodeDict:
                    curr.random = nodeDict[id(target.random)]
                else:
                    nodeList.append([id(target.random), curr])
            if first == None:
                first = curr
            if prev != None:
                prev.next = curr
            
            target = target.next
            if target == None:
                if prev != None:
                    prev.next = curr
                break
            prev = curr

        for node in nodeList:
            if node[0] in nodeDict:
                node[1].random = nodeDict[node[0]]
        return first
        