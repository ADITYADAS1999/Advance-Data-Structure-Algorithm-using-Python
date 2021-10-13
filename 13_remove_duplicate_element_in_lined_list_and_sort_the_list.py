    #Represent a node of the singly linked list  
class Node:
    def __init__(self,data):  
    self.data = data
    self.next = None  
              
class RemoveDuplicate:  
#Represent the head and tail of the singly linked list  
    def __init__(self):
        self.head = None;  
        self.tail = None;  
#addNode() will add a new node to the list  
    def addNode(self, data):  
#Create a new node  
        newNode = Node(data);  
              
            #Checks if the list is empty  
            if(self.head == None):  
                #If list is empty, both head and tail will point to new node  
                self.head = newNode;  
                self.tail = newNode;  
            else:  
                #newNode will be added after tail such that tail's next will point to newNode  
                self.tail.next = newNode;  
                #newNode will become new tail of the list  
                self.tail = newNode;  
                  
        #removeDuplicate() will remove duplicate nodes from the list  
        def removeDuplicate(self):  
            #Node current will point to head  
            current = self.head;  
            index = None;  
            temp = None;  
              
            if(self.head == None):  
                return;  
            else:  
                while(current != None):  
                    #Node temp will point to previous node to index.  
                    temp = current;  
                    #Index will point to node next to current  
                    index = current.next;  
                      
                    while(index != None):  
                        #If current node's data is equal to index node's data  
                        if(current.data == index.data):  
                            #Here, index node is pointing to the node which is duplicate of current node  
                            #Skips the duplicate node by pointing to next node  
                            temp.next = index.next;  
                        else:  
                            #Temp will point to previous node of index.  
                            temp = index;  
                        index = index.next;  
                    current = current.next;  
                      
        #display() will display all the nodes present in the list  
        def display(self):  
            #Node current will point to head  
            current = self.head;  
            if(self.head == None):  
                print("List is empty");  
                return;  
            while(current != None):  
                #Prints each node by incrementing pointer  
                print(current.data);  
                current = current.next;  
              
       
    sList = RemoveDuplicate();  
              
    #Adds data to the list  
    sList.addNode(1);  
    sList.addNode(2);  
    sList.addNode(3);  
    sList.addNode(2);  
    sList.addNode(2);  
    sList.addNode(4);  
    sList.addNode(1);  
       
    print("Originals list: ");  
    sList.display();  
       
    #Removes duplicate nodes  
    sList.removeDuplicate();  
       
    print("List after removing duplicates: ");  
    sList.display();  
