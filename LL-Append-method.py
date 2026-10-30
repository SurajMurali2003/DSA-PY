class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, val):
        new_node = Node(val)
        self.head =  new_node
        self.tail= new_node
        self.length = 1
    def print_val(self):
        temp =  self.head
        while temp is not None:
            print("valsss", temp.value)
            temp = temp.next

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
         
         self.head = new_node
         self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
    def pop(self):
        #find 2 last el ,  make tail = 2nd last el , tial.next = null retun popoed el
        if self.head is None:
            return "no El in LL"
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail  = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.tail = None
            self.next = None
        return temp.value
            
        
    

linked_list = LinkedList(3)
print("ll", linked_list.head.value)
# linked_list.print_val()
linked_list.append(444)
linked_list.append(555) 
linked_list.append(777)
linked_list.print_val()
print("Lengthh", linked_list.length)

print(linked_list.pop())
print(linked_list.pop())
print(linked_list.pop())
print(linked_list.pop())
print(linked_list.pop())
print(linked_list.pop())
# linked_list.print_val()
print("Lengthh", linked_list.length)