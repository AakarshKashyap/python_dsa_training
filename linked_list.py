class Node:
    def __init__(self,data):
        self.data = data
        self.next = null
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def length_of_list(self):
        temp = self.head
        count = 0
        while temp is not None:
            count +=1
            temp = temp.next
        return count
    def insert_begin(self, data):
        nn = Node(data)
        if self.head == None:
            self.head = nn
        else:
            nn.next = self.head
            head = nn
    def insert_end(self, data):
        nn = Node(data)
        if self.head is null:
            head = nn
            return
        temp = self.head
        while temp.next is not null:
            temp = temp.next
        temp.next = nn
    def insert_at_pos(self, pos):
        if pos<=0:
            print("Invalid Position")
            return
        if pos == 1:
            insert_begin(data)
            return
        temp = self.head
        i=1
        while(i<pos-1 and temp is not None):
            temp = temp.next
        if temp is None:
            print("Insufficicent Elements")
            return
        nn.next = temp.next
        temp.next = nn
    def insert_at_middle(self, data, pos):
        n= self.length_of_list()
        if n==0:
            self.insert_begin(data)
            return
        pos = n//2
        self.insert_at_pos(data, pos)
    
    def delete_from_begin(self):
        if self.head == None:
            return
        self.head = self.head.next
    def delete_from_pos(self, pos):
        if head.self is None:
            return
        if pos == 1:
            self.head = self.head.next
            temp = self.head
        for i in range(pos - 2):
            temp = temp.next
        temp.next = temp.next.next
    def delete_from_mid(self):
        n = self.length_of_list()
        if n==0:
            return
        pos = n//2
        self.delete_at_pos(pos)
    def delete_from_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        temp = self.head
        while temp.head.next is not None:
            temp = temp.next
        temp.next = None
    def search(self, data):
        temp = self.head
        pos = 1
        while temp is not None:
            if temp.data == data:
                return pos
            temp = temp.next
            pos += 1




        
            
            