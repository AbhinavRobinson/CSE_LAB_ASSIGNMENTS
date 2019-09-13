class LinkedList {

  // Head Node
  Node head;

  // Our Node Maker
  static class Node
  {
    Node next;
    int data;

    Node()
    {
      this.data = 0;
      this.next = null;
    }

    Node(int d)
    {
      this.data = d;
      this.next = null;
    }

    Node(int d,Node next)
    {
      this.data = d;
      this.next = next;
    }
  }

  // INSERTS ELEMENTS IN LINKED LIST
  public static LinkedList insert(LinkedList list, int data)
  {
    // Create a new node with given data 
    Node new_node = new Node(data); 
    new_node.next = null; 

    // If the Linked List is empty, 
    // then make the new node as head 
    if (list.head == null) { 
        list.head = new_node; 
    } 
    else { 
        // Else traverse till the last node 
        // and insert the new_node there 
        Node last = list.head; 
        while (last.next != null) { 
            last = last.next; 
        } 

        // Insert the new_node at last node 
        last.next = new_node; 
    } 

    // Return the list by head 
    return list; 
  }

  public static void printList(LinkedList list)
  {
    // Gets the head and assigns to pointer
    Node pointer = list.head;
    // traverses the list
    while(pointer != null)
    {
      // just a fancy print command
      if (pointer.next == null)
      {
        System.out.print(pointer.data+"\n");
        break;
      }
      System.out.print(pointer.data+" -> ");
      // skips a element
      pointer = pointer.next;
    }
  }


  // QUESTION ONE
  public static void printAlternate(LinkedList list)
  {
    // Gets the head and assigns to pointer
    Node pointer = list.head;
    // traverses the list
    while(pointer != null)
    {
      // just a fancy print command
      if (pointer.next == null || (pointer.next).next == null)
      {
        System.out.print(pointer.data+"\n");
        break;
      }
      System.out.print(pointer.data+" -> ");
      // skips a element
      pointer = (pointer.next).next;
    }
  }

  // Get length of list
  public static int getListLength(LinkedList list)
  {
    // List Length is 1-indexed
    int len = 1;
    // Create a head pointer
    Node pointer = list.head; 
    while(pointer.next != null)
    {
      len++;
      pointer = pointer.next;
    }
    return len;
  }




  // QUESTION TWO
  public static int getLastNth(LinkedList list, int len, int index){
    Node pointer = list.head;
    // Nth from last = Length - Nth
    index = len - index;
    while(pointer.next != null)
    {
      // Cover Edge Case, index > len
      if(index < 0) break;
      // Reach the correct Node
      if(index == 0)
      {
        return pointer.data;
      }
      pointer = pointer.next;
      index--;
    }
    // Cover Edge Case, no data in list
    return -1;
  }

  // Removes a Node
  public static void removeNode(LinkedList list, int index){
    // Gets Head and creates a Previous Node
    Node pointer = list.head;
    Node pre_pointer = null;
    while(pointer.next != null){
      // Moves Along The list
      pre_pointer = pointer;
      pointer = pointer.next;
      if(index == 0){
        // Removal From List
        pre_pointer.next = pointer.next;
        pointer.next = null;
        break;
      }
      index--;
    }
  }


  // QUESTION THREE
  public static LinkedList removeDupUnsorted(LinkedList list)
  {
    Node pointer = list.head;
    int index = 0;

    while(pointer != null){
      int chk_num = pointer.data;
      Node chk_pointer = pointer.next;
      index = 0;
      while(chk_pointer != null){
        if(chk_pointer.data == chk_num){
          removeNode(list, index);
        }
        index++;
        chk_pointer = chk_pointer.next;
      }
      pointer = pointer.next;
    }
    return list;
  }


  // Question FOUR
  public static LinkedList Join(LinkedList list1, LinkedList list2){
    Node rear = list1.head;
    while(rear.next != null){
      rear = rear.next;
    }

    rear.next = list2.head;      

    return list1;
  }
  // END OF LINKEDLIST CLASS
}

class Main{
  public static void main(String[] args) 
  {
    // QUESTION ONE
    // Create List
    LinkedList list = new LinkedList();
    // Insert Elements into list
    list = LinkedList.insert(list, 1);
    list = LinkedList.insert(list, 2);
    list = LinkedList.insert(list, 3);
    list = LinkedList.insert(list, 4);
    list = LinkedList.insert(list, 5);
    list = LinkedList.insert(list, 6);
    list = LinkedList.insert(list, 7);
    list = LinkedList.insert(list, 8);
    // Printing Alternate
    System.out.println("**** QUESTION 1 ****");
    LinkedList.printAlternate(list);

    // QUESTION TWO
    System.out.println("**** QUESTION 2 ****");
    System.out.println("Nth from Last Node Data : "+LinkedList.getLastNth(list,LinkedList.getListLength(list),3));
    // QUESTION THREE
    LinkedList list2 = new LinkedList();
    list2 = LinkedList.insert(list2, 2);
    list2 = LinkedList.insert(list2, 1);
    list2 = LinkedList.insert(list2, 2);
    list2 = LinkedList.insert(list2, 1);
    list2 = LinkedList.insert(list2, 5);
    list2 = LinkedList.insert(list2, 3);
    list2 = LinkedList.insert(list2, 7);
    list2 = LinkedList.insert(list2, 3);

    System.out.println("**** QUESTION 3 ****");
    System.out.println("Original List");
    LinkedList.printList(list2);
    LinkedList.removeDupUnsorted(list2);
    System.out.println("Removing Duplicates from List");
    LinkedList.printList(list2);

    System.out.println("**** QUESTION 4 ****");
    System.out.println("List 1 + List 2 = ");
    LinkedList.printList(LinkedList.Join(list,list2));
  }
  // END OF MAIN 
}