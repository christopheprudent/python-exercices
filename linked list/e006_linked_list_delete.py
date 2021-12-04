from e001_linked_list_append_iterate import singly_linked_list

class linked_list(singly_linked_list):
    def find(self, data):
        for val in self.iterate_item():
            if val == data:
                return True
        return False

    def find_index(self, index):
        _idx = 0
        for val in self.iterate_item():
            if _idx == index:
                return val
            _idx += 1
        return None
    # web solution
    def __getitem__(self, index):
        if index > self.count - 1:
            raise IndexError
            #raise Exception("Index out of range")
            #return "Index out of range"
        current_val = self.head
        for _ in range(index):
            current_val = current_val.next
        return current_val.data
    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise IndexError
            #raise Exception("Index out of range")
            #return "Index out of range"
        current_val = self.head
        for _ in range(index):
            current_val = current_val.next
        _previous = current_val.data
        current_val.data = value
        return _previous 
    def delete_first(self):
        if self.count > 0:
            _first = self.head
            self.head = self.head.next
            del _first
            self.count -= 1
    def delete_last(self):
        if self.count > 0:
            _current = self.head
            for _ in range(self.count -1):
                _current = _current.next
            _last = _current.next
            self.tail = _current
            del _last
            self.count -= 1
    # web solution
    def delete_item(self, data):
        # Delete an item from the list
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.count -= 1
                return
            prev = current
            current = current.next

    def __str__(self):
        current = self.head
        _str = ''
        for i in range(self.count):
            #print("élément #%d = (%s)" %(i, current.data))
            _str += 'élément #{0} = ({1})'.format(i, current.data)
            if i < (self.count -1):
                _str += '\n'
            current = current.next
        return _str


if __name__ == "__main__":
    items = linked_list()
    items.append_item('PHP')
    items.append_item('Python')
    items.append_item('C#')
    items.append_item('C++')
    items.append_item('Java')

    # recherche par valeur
    while True:
        data = input("Entrez la valeur à chercher (vide pour quitter): ")
        if not data:
            break

        _find = items.find(data)
        print("dans la liste: ", _find)

    # recherche par index
    while True:
        index = int(input("Entrez l'index à chercher (-1 pour quitter): "))
        if index == -1:
            break

        _value = items.find_index(index)
        print("valeur de l'index: ", _value)

    try:
        print(items[4])
        print(items[5])
        print(items[10])
    except IndexError:
        print("Index out of range")
        
    for i in range(items.length()):
        #print("élément #%d = (%s)" %(i, items.__getitem__(i)))
        print("élément #%d = (%s)" %(i, items[i]))
    print("\nAffichage éléments")
    print(items)

    print("\nModification par position")
    items[2] = 'Pascal'
    for i in range(items.length()):
        print("élément #%d = (%s)" %(i, items[i]))

    print("\nEffacement éléments")
    items.delete_first()
    items.delete_last()
    items.delete_last()
    for i in range(items.length()):
        print("élément #%d = (%s)" %(i, items[i]))
    
    print("\nAjout éléments")
    items.append_item('C++')
    items.append_item('C++')
    items.delete_item('C++')
    for i in range(items.length()):
        print("élément #%d = (%s)" %(i, items[i]))
