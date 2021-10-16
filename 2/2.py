class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_list(first):
    # Выводим список
    print("____________")
    current = first
    while current is not None:
        print(current.value)
        current = current.next
    print(current)  # None


def reverse_link_values(first):
    if first is None:
        return None
    elif first.next is None:
        return first
    elif first.next.next is None:
        current = first
        current_1 = first.next
        current.value, current_1.value = current_1.value, current.value
        return current
    len = 1
    current = first
    while current.next is not None:
        current = current.next
        len += 1
    l = 1
    current_1 = first
    for i in range(len//2):
        current_2 = first
        for j in range(len - l):
            current_2 = current_2.next
        current_1.value, current_2.value = current_2.value, current_1.value
        l += 1
        current_1 = current_1.next
    return first


first = Node(0)
current = first

for i in range(1,5):
    node = Node(i)
    current.next = node
    current = current.next


print_list(first)

first = reverse_link_values(first)

print_list(first)
