import heapq
heap = []

testList = [10, 14, 17, 20, 30, 21, 44]

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
    

testList = delete(testList)

print(testList)