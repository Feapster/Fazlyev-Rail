class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_list(first):
    # Выводим список
    print("____________")
    current = first
    i = 0
    while current is not None:
        print(current.value)
        i += 1
        current = current.next
    print(current)  # None


def get_by_index(first, position):
    i = 0
    current = first
    while i != position:
        i += 1
        if current.next is None:
            return 0
        current = current.next
    return current.value


first = Node(0)
current = first

for i in range(1, 3, 2):
    node = Node(i)
    current.next = node
    current = current.next

pos = 1

print_list(first)

print(get_by_index(first,pos))