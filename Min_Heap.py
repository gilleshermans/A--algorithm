class heap:
    def __init__(self, list):
        self.list = list

    def heapify(self):
        newList = list
        sortedList = sorted(list, reverse=True)

        for node in sortedList:
            isCorrectlyPlaced = False
            while not isCorrectlyPlaced:
                nodeIndex = newList.index(node)
                try:
                    childL = newList[int(2*nodeIndex+1)]
                    childLIndex = int(2*nodeIndex+1)
                    childR = newList[int(2*nodeIndex+2)]
                    childRIndex = int(2*nodeIndex+2)

                    if node > childL:
                        newList[nodeIndex] = childL
                        newList[childLIndex] = node
                    elif node > childR:
                        newList[nodeIndex] = childR
                        newList[childRIndex] = node
                    else:
                        isCorrectlyPlaced = True
                except:
                    isCorrectlyPlaced = True
    

    def insert(self, node):
        hasBubbled = False
        self.list.append(node)
        while not hasBubbled:
            indexNode = self.list.index(node)
            parent = self.list[int((indexNode - 1)/2)]
            indexParent = self.list.index(parent)
            if parent > node:
                self.list[indexNode] = parent
                self.list[indexParent] = node
            else:
                hasBubbled = True
        
        return self.list


    def delete(self):
        hasBubbledDown = False
        self.list[0] = self.list[-1]
        self.list.remove(self.list[-1])
        indexNode = self.list.index(self.list[0])
        while not hasBubbledDown:
            node = self.list[indexNode]
            childL = self.list[int(2*indexNode) + 1]
            childR = self.list[int(2*indexNode) + 2]

            if self.list[indexNode] > childL:
                self.list[indexNode] = childL
                self.list[self.list.index(childL)] = node
            elif self.list[indexNode] > childR:
                self.list[indexNode] = childR
                self.list[self.list.index(childR)] = node
            else:
                hasBubbledDown = True

            indexNode = self.list.index(node)

        return self.list
