# Node Class
class Node:

    # Constructors
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.Addr = hex(id(self))
        # Node generated

# End of Node Class
    





# Doubly Linked List Class
class doublylinkedlist:

    # Initialise head
    def __init__(self):
        self.head = None
        # object initialized

    # Function to print list
    def printList(self):
        ptr = self.head
        if ptr.next != None: print("<head>",end="")
        else: print("Empty List")
        while(ptr):
            if ptr.next == None:  print(ptr.data,end="")
            else: print(ptr.data,"<->",sep="",end="")
            ptr = ptr.next
        print()
        # Printing done ... end function

    # Add nodes to list
    def appendNode(self, data):
        ptr = self.head
        if ptr == None:
            # if no elements in list
            self.head = Node(data)
        elif ptr.data > data:
            # if we need to insert element at start of list
            newNode = Node(ptr.data)
            ptr.data = data
            newNode.next = ptr.next   
            ptr.next = newNode
            newNode.prev = ptr
            newNode.next.prev = newNode
        else:
            # otherwise we find the correct position for element
            newNode = Node(data)
            # Traversal (emulation on a do-while loop)
            while True:
                # until Null reached
                if ptr.next == None: break
                # while data value < next block's data value
                if ptr.next.data > data: break
                # traverse...
                ptr = ptr.next
            # position found, insert node
            newNode.next = ptr.next
            # so we do not get Null Pointer Exception for accessing "Null.prev"
            if ptr.next != None: ptr.next.prev = newNode
            ptr.next = newNode
            newNode.prev = ptr
        # Insertion done ... end function

    # Delete elements from list
    def deleteNode(self, data):
        ptr = self.head
        if ptr == None:
            pass
        else:
            while ptr:
                if ptr.data == data:
                    ptr.prev.next = ptr.next  
                    ptr = None
                    break
                ptr = ptr.next
        # Deletion done ... end function

    # Set Prev Node Link to New Node
    def setPrevNode(self, Node):
        # If Node is somewhere inside list after head
        if Node.prev != None: self.prev = Node.prev
        # If Node is actually head
        else: self.prev = None
        Node.prev = self
        self.next = Node
        # Data Set

    # Set Next Node Link to New Node
    def setNextNode(self, Node):
        Node.next = self
        self.prev = Node
        # Data Set

    # Get Prev Address from Link
    def getPrevLink(self, data):
        ptr = self.head
        if ptr == None:
            return None
        else:
            while ptr:
                if ptr.data == data:
                    return ptr.prev
                ptr = ptr.next     
        # Node Returned

    # Get Next Address from Link
    def getNextLink(self, data):
        ptr = self.head
        if ptr == None:
            return None
        else:
            while ptr:
                if ptr.data == data:
                    return ptr.next 
                ptr = ptr.next
        # Node Returned

    # Print with Addresses
    def fullPrint(self):
        print("_________________________________________________")
        # Printing according to format
        print("  PrevAddr  | Value |  CurrAddr   |    NextAddr")
        print()
        ptr = self.head
        print("    NULL     ",ptr.data,ptr.Addr,ptr.next.Addr,sep="---")
        if ptr.next != None:
            ptr = ptr.next 
            while ptr:
                if ptr.next == None: print(ptr.prev.Addr,ptr.data,ptr.Addr,"     NULL    ",sep="---")
                else: print(ptr.prev.Addr,ptr.data,ptr.Addr,ptr.next.Addr,sep="---")
                ptr = ptr.next
        print()
        print("-------------------END OF LIST-------------------")
        print("_________________________________________________")
        print()
        # Printing Complete ... End Function

# END OF DOUBLY LINKED LIST CLASS






# TEXT EDITIOR CLASS
class texteditor(): 

    # Initialize
    def __init__(self):
        self.head = None
        self.ptr = None

    # Insert Char
    def insertChar(self, data, ptr = None):
        # Check for char length
        if len(data) == 1:
            if ptr == None : ptr = self.head
            newNode = Node(data)
            # Initialise
            if ptr == None:
                self.head = newNode
            else:
                # Append
                while ptr.next != None:
                    ptr = ptr.next  
                ptr.next = newNode
                newNode.prev = ptr
        else:
            print("ERROR : ENTER A CHARACHTER")
            exit(0)

    # Delete Char
    def deleteChar(self, data):
        ptr = self.head
        if ptr == None:
            pass
        else:
            while ptr:
                if ptr.data == data:
                    ptr.prev.next = ptr.next  
                    ptr = None
                    break
                ptr = ptr.next

    # Print String
    def printString(self):
        ptr = self.head
        sen = ""
        # traverse...
        while ptr != None:
            sen += ptr.data
            ptr = ptr.next
        print(sen)

    # GO RIGHT
    def right(self, ptr):
        # IF NONE, RETURN FIRST NODE
        if ptr == None:
            ptr = self.head
            return ptr
        # IF AT END
        elif ptr.next == None:
            return ptr
        else:
            # ELSE RETURN NEXT NODE
            return ptr.next

    #GO LEFT
    def left(self, ptr):
        # IF NONE, RETURN LAST NODE
        if ptr == None:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next  
            return ptr
        # IF AT START
        elif ptr.prev == None:
            return ptr
        else:
            # ELSE RETURN PREV NODE
            return ptr.prev

# END OF TEXT EDITOR CLASS
    





# QUESTION THREE
class polynomial:

    # INITIALISE POLYNOMIAL
    def __init__(self):
        self.head = None

    # ADD VARIABLE TO LIST
    def addVariable(self,constant,power):
        data = [constant, power]
        ptr = self.head
        if ptr == None:
            # if no elements in list
            self.head = Node(data)
        elif ptr.data[1] == data[1]:
            ptr.data = [ptr.data[0]+data[0],ptr.data[1]]
        elif ptr.data[1] < data[1]:
            # if we need to insert element at start of list
            newNode = Node(ptr.data)
            ptr.data = data
            newNode.next = ptr.next   
            ptr.next = newNode
            newNode.prev = ptr
            if newNode.next != None: newNode.next.prev = newNode
        else:
            # otherwise we find the correct position for element
            newNode = Node(data)
            # Traversal (emulation on a do-while loop)
            while True:
                flag = False   
                # until Null reached
                if ptr.next == None: break
                # If power is same 
                if ptr.next.data[1] == data[1]:                 
                    flag = True
                    break   
                # while data value > next block's data value
                if ptr.next.data[1] <= data[1]: break
                # traverse...
                ptr = ptr.next
            # If Differrent Power
            if not flag:
                # position found, insert node
                newNode.next = ptr.next
                # so we do not get Null Pointer Exception for accessing "Null.prev"
                if ptr.next != None: ptr.next.prev = newNode
                ptr.next = newNode
                newNode.prev = ptr
            # IF same power
            else:
                ptr.next.data[0] += data[0] 
    # END OF ADDTION OF VARIABLE TO LIST

    # DELETE A VARIABLE
    def deleteVariable(self, constant, power):
        data = [constant, power]
        ptr = self.head
        if ptr == None:
            pass
        else:
            while ptr:
                if ptr.data == data:
                    ptr.prev.next = ptr.next  
                    ptr = None
                    break
                ptr = ptr.next
        # Deletion done ... end function
    # END OF DELETION OF VARIABLE

    # PRINT POLYNOMIAL
    def printPolynomial(self):
        ptr = self.head
        if ptr.next != None: print("<head> -> ",end="")
        else: print("Empty List")
        while(ptr):
            if ptr.next == None:  
                if ptr.data[1] == 0:
                    print(ptr.data[0],end="")
                else:
                    print(ptr.data[0],'x^',ptr.data[1],end="")
            else: 
                if ptr.data[1] == 0:
                    print(ptr.data[0]," + ",sep="",end="")
                else:
                    print(ptr.data[0],'x^',ptr.data[1]," + ",sep="",end="")
            ptr = ptr.next
        print()
        # Printing done ... end function

    #  Multiply TWO POLYNOMIALS
    def multiply(self, y):
        a,b = self.hasMoreCoff(y)
        A = a.head
        Z = polynomial()
        while A:
            # FIRST VARIABLE OF X
            x_coff = A.data[0]
            x_pow = A.data[1]
            B = b.head
            while B:
                # FIRST VARIABLE OF Y
                y_coff = B.data[0]
                y_pow = B.data[1]
                # MULTIPLY
                z_coff = x_coff*y_coff
                z_pow = x_pow+y_pow
                # ADD TO POLYNOMIAL
                Z.addVariable(z_coff,z_pow)
                B = B.next  
            A = A.next
        return Z   
    # END OF MULTIPLY

    # HELPER FUNCTIONS
    # COUNT
    def countCoff(self):
        ptr = self.head
        count = 0
        while ptr:
            count+=1
            ptr = ptr.next
        return count
    # FIND LARGER LIST
    def hasMoreCoff(self,Y):
        if self.countCoff()>Y.countCoff():
            return self,Y
        return Y,self
  
# END OF POLYNOMIAL CLASS






# Main Class // Driver Class
if __name__ == '__main__':
    # QUESTION ONE
    # Create a empty list
    print("Initializing list...")
    Llist = doublylinkedlist()
    # Add elements to list
    print("Inserting elements into list...")
    Llist.appendNode(3)
    Llist.appendNode(4)
    Llist.appendNode(1)
    Llist.appendNode(5)
    Llist.appendNode(2)
    # print list
    Llist.printList()
    # now lets delete 3
    print("Deleting 3 from list...")
    Llist.deleteNode(3)
    # print list
    Llist.printList()
    # lets print according to required format
    print("Printing in Full Format...")
    Llist.fullPrint()

    # QUESTION TWO
    print("---------QUESTION 2--------")
    slist = texteditor()
    slist.insertChar("a")
    slist.insertChar("b")
    slist.insertChar("h")
    slist.insertChar("i")
    slist.insertChar("n")
    slist.insertChar("a")
    slist.insertChar("v") 
    slist.printString()
    slist.deleteChar("v")
    slist.printString()
    ptr = slist.left(None)
    ptr = slist.left(ptr)
    print(ptr.data)
    ptr = slist.right(ptr)
    print(ptr.data)

    # QUESTION THREE
    print("---------QUESTION 3--------")
    # GIVEN TEST CASE
    print("-------GIVEN TEST CASE-------")
    A = polynomial()
    B = polynomial()
    A.addVariable(3,2)
    A.addVariable(5,1)
    A.addVariable(6,0)
    B.addVariable(6,1)
    B.addVariable(8,0)
    print("A = ",end="")
    A.printPolynomial()
    print("B = ",end="")
    B.printPolynomial()
    C = A.multiply(B)
    print("A * B = C")
    print("C = ",end="")
    C.printPolynomial()

# END OF MAIN/DRIVER METHOD