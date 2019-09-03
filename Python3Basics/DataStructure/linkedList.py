class Node:
    def __init__(self,value):
        self.next = None
        self.value = value

class singleLinkedList(Node):
    def __init__(self):
        self.head = None
        self.length = 0

    def insertHeadNode(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def insertTailNode(self,data):
        currentNode = self.head
        while(currentNode.next != None):
            currentNode = currentNode.next
        newNode = Node(data)
        currentNode.next = newNode
        newNode.next = None
        self.length += 1

    def prependNode(self,data):
        if(self.length == 0):
                return self.insertHeadNode(data)
        else:
                return self.insertTailNode(data)

    def insertAtPos(self,pos,data):
        if (pos == 0):
            return self.insertHeadNode(data)
        elif (pos == self.length):
            return self.insertTailNode(data)
        else:
            newNode = Node(data)
            currentNode = self.head
            counter = 0
            while(counter != pos-1):
                currentNode = currentNode.next
                counter += 1
            leadNode = currentNode
            newNextNode = leadNode.next
            leadNode.next = newNode
            newNode.next = newNextNode



    def displayList(self):
        currentNode = self.head
        while(currentNode != None):
            print(currentNode.value,"-> ",end = "")
            currentNode = currentNode.next

    def reverseList(self):
        previousNode = None
        currentNode = self.head
        while(currentNode != None):
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        self.head = previousNode


list = singleLinkedList()
list.prependNode(10)
list.prependNode(20)
list.prependNode(30)
list.prependNode(40)
print(list.length)
print(list.displayList())
list.insertAtPos(3,50)
print(list.length)
print(list.displayList())
list.reverseList()
print(list.displayList())
