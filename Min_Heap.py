import operator


class heap:
    def __init__(self, list):
        self.list = list


    def insert(self, node):
        isCorrectlyPlaced = False
        self.list.append(node)

        while not isCorrectlyPlaced:
            indexNode = self.list.index(node)
            indexParent = int((indexNode - 1)/2)
            parent = self.list[indexParent]
            
            if parent.F > node.F:
                self.list[indexNode], self.list[indexParent] = parent, node
            else:
                isCorrectlyPlaced = True
        
        return self.list



    def delete(self):
        isCorrectlyPlaced = False
        self.list[0] = self.list[-1]
        self.list.pop(len(self.list)-1)

        if self.list == []:
            return
        
        indexNode = self.list.index(self.list[0])

        while not isCorrectlyPlaced:
            node = self.list[indexNode]
            childLIndex = 2*indexNode + 1 
            childRIndex = childLIndex + 1

            if childLIndex < len(self.list):
                try:
                    if self.list[childRIndex].F < self.list[childLIndex].F:
                        childLIndex, childRIndex = childRIndex, childLIndex
                except:
                    pass

                childL = self.list[childLIndex]
                if self.list[indexNode].F > childL.F:
                    self.list[indexNode], self.list[childLIndex] = childL, node
                    indexNode = childLIndex
                    continue

            isCorrectlyPlaced = True   

        return self.list



    def heapify(self):
        newList = self.list
        sortedList = sorted(self.list, key=operator.attrgetter("F"), reverse=True)
        #sortedList = sorted(self.list, reverse=True)

        for node in sortedList:
            isCorrectlyPlaced = False
            while not isCorrectlyPlaced:
                nodeIndex = self.list.index(node)
                childLIndex = int(2*nodeIndex+1)
                childRIndex = int(2*nodeIndex+2)

                if childLIndex < len(self.list):
                    childL = self.list[childLIndex]
                    if node.R > childL.R:
                        newList[nodeIndex] = childL
                        newList[childLIndex] = node
                        continue
                if childRIndex < len(self.list):
                    childR = self.list[childRIndex]
                    if node.R > childR.R:
                        newList[nodeIndex] = childR
                        newList[childRIndex] = node
                    else:
                        isCorrectlyPlaced = True

                else:
                    isCorrectlyPlaced = True
        return newList
   

if __name__ == '__main__':
    testList = heap([6.5, 5.2, 4.6, 5.6, 5.4])
    testList = testList.delete()
    print(testList)
