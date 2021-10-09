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


def length(first):
    i = 1
    current = first
    while current.next is not None:
        i += 1
        current = current.next
    return i


first = Node(0)
current = first


for i in range(1, 9, 3):
    node = Node(i)
    current.next = node
    current = current.next


print_list(first)

print(length(first))
