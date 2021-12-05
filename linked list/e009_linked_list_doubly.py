# web solution
class Node(object):
    # Doubly linked node
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
	
class doubly_linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_item(self, data):
        # Append an item 
        new_item = Node(data, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item

        self.count += 1

    def print_forward(self):
        for node in self.iter():
            print(node)

    def print_backward(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev
            
    def iter(self):
        # Iterate the list
        current = self.head
        while current:
            item_val = current.data
            current = current.next
            yield item_val

    def reverse(self):
        """ Reverse linked list. """
        current = self.head
        while current:
            #temp, current.next, current.prev = current.next, current.prev, temp
            temp = current.next
            current.next = current.prev
            current.prev = temp

            current = current.prev

        #temp, self.head, self.tail = self.head, self.tail, temp
        temp = self.head
        self.head = self.tail
        self.tail = temp

    def insert_first(self, data):
        new_item = Node(data, self.head, None)
        self.head.prev = new_item
        self.head = new_item
        self.count += 1

    def find(self, data):
        for val in self.iter():
            if val == data:
                return True
        return False

    def delete_item(self, data):
        # Delete an item from the list
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    (self.head.next).prev = None
                    self.head = self.head.next
                elif current == self.tail:
                    (self.tail.prev).next = None
                    self.tail = self.tail.prev
                else:
                    (current.prev).next = current.next
                    (current.next).prev = current.prev
                del current
                self.count -= 1
                return
            current = current.next

items = doubly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')
items.append_item('SQL')

print("Print items in the Doubly linked, backwards:")
items.print_backward()
print("Print items in the Doubly linked, forwards:")
items.print_forward()
print("print reversed items:")
items.reverse()
items.print_forward()
print("insert new item at top, print forwards:")
items.insert_first('Pascal')
items.print_forward()
print("print backwards:")
items.print_backward()

# recherche par valeur
while True:
    data = input("Entrez la valeur à chercher (vide pour quitter): ")
    if not data:
        break

    _find = items.find(data)
    print("dans la liste: ", _find)

# delete items
print("delete 2 items:")
items.delete_item('C#')
items.delete_item('PHP')
print("print forwards:")
items.print_forward()
print("print backwards:")
items.print_backward()
