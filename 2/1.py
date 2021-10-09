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


def reverse_link(first):
    if first.next.next is None:
        current = first
        current_1 = first.next
        current_1.next = current
        current.next = None
        return current_1
    prev_1 = first
    prev_2 = first.next
    current = first.next.next
    prev_2.next = prev_1
    prev_1.next = None
    while current.next is not None:
        prev_1 = prev_2
        prev_2 = current
        current = current.next
        prev_2.next = prev_1
    current.next = prev_2
    return current


first = Node(0)
current = first
current = current.next

for i in range(2):
    node = Node(i)
    current.next = node
    current = current.next


print_list(first)

first = reverse_link(first)

print_list(first)
