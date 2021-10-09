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


def sum(first,second):
    i = 1
    current_1 = first
    current_2 = second
    while current_1 is not None:
        current_1.value = current_1.value + current_2.value
        current_1 = current_1.next
        current_2 = current_2.next
    return first


first = Node(0)
current = first


for i in range(1, 9):
    node = Node(i)
    current.next = node
    current = current.next


second = Node(0)
current_2 = second


for i in range(4, 12):
    node = Node(i)
    current_2.next = node
    current_2 = current_2.next


print_list(first)

print_list(second)

print_list(sum(first,second))
