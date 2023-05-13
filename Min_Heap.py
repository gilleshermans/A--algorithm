import operator


class heap:
    def __init__(self, list):
        self.list = list


    def insert(self, node):
        hasBubbled = False
        self.list.append(node)

        while not hasBubbled:
            indexNode = self.list.index(node)
            parent = self.list[int((indexNode - 1)/2)]
            indexParent = self.list.index(parent)
            if parent.F > node.F:
                self.list[indexNode] = parent
                self.list[indexParent] = node
            else:
                hasBubbled = True
        
        return self.list


    def delete(self):
        isCorrectlyPlaced = False
        self.list[0] = self.list[-1]
        self.list.pop(len(self.list)-1)
        
        if self.list != []:
            indexNode = self.list.index(self.list[0])
            while not isCorrectlyPlaced:
                node = self.list[indexNode]
                childLIndex = int(2*indexNode) + 1 
                childRIndex = int(2*indexNode) + 2
                if childLIndex < len(self.list) and childRIndex < len(self.list):
                    if self.list[childRIndex].F < self.list[childLIndex].F:
                        childLIndex += 1
                        childRIndex -= 1

                if childLIndex < len(self.list):
                    childL = self.list[childLIndex]
                    if self.list[indexNode].F > childL.F:
                        self.list[indexNode] = childL
                        self.list[childLIndex] = node
                        indexNode = self.list.index(node)
                        continue
                    

                if childRIndex < len(self.list):
                    childR = self.list[childRIndex]
                    if self.list[indexNode].F > childR.F:
                        self.list[indexNode] = childR
                        self.list[childRIndex] = node
                        indexNode = self.list.index(node)
                        continue
                    
                isCorrectlyPlaced = True   
        return self.list

    # def delete(self):
    #     if not self.list:
    #         return []
        
    #     self.list[0], self.list[-1] = self.list[-1], self.list[0]
    #     node = self.list.pop()
    #     indexNode = 0
    #     childLIndex = 1
    #     childRIndex = 2
        
    #     while childLIndex < len(self.list):
    #         childL = self.list[childLIndex]
    #         if childRIndex < len(self.list):
    #             childR = self.list[childRIndex]
    #             if childR.F < childL.F:
    #                 childL, childR = childR, childL
            
    #         if childL.F >= node.F:
    #             break
            
    #         self.list[indexNode], self.list[childLIndex] = childL, node
    #         indexNode = childLIndex
    #         childLIndex = 2 * indexNode + 1
    #         childRIndex = childLIndex + 1
        
    #     return self.list


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
