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

    items[2] = 'Pascal'
    for i in range(items.length()):
        print("élément #%d = (%s)" %(i, items[i]))
