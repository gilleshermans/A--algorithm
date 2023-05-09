import heapq
heap = []

testList = [10, 14, 17, 20, 30, 21, 44]
testList2 = [20, 17, 30, 2, 5, 19, 8]

def heapify(list : list):
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
   

def insert(heap : list, node):
    hasBubbled = False
    heap.append(node)
    while not hasBubbled:
        indexNode = heap.index(node)
        parent = heap[int((indexNode - 1)/2)]
        indexParent = heap.index(parent)
        if parent > node:
            heap[indexNode] = parent
            heap[indexParent] = node
        else:
            hasBubbled = True
    
    return heap


def delete(heap : list):
    hasBubbledDown = False
    heap[0] = heap[-1]
    heap.remove(heap[-1])
    indexNode = heap.index(heap[0])
    while not hasBubbledDown:
        node = heap[indexNode]
        childL = heap[int(2*indexNode) + 1]
        childR = heap[int(2*indexNode) + 2]

        if heap[indexNode] > childL:
            heap[indexNode] = childL
            heap[heap.index(childL)] = node
        elif heap[indexNode] > childR:
            heap[indexNode] = childR
            heap[heap.index(childR)] = node
        else:
            hasBubbledDown = True

        indexNode = heap.index(node)

    return heap
    

heapify(testList2)