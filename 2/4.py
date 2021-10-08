class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_list(first):
    # Выводим список
    print("____________")
    current = first
    i = 0
    while current is not None and i < 7:
        print(current.value)
        current = current.next
        i += 1
    print(current)  # None

def switch(first, c_1, c_2):
    current_1 = first
    current_2 = first
    prev_1 = first
    prev_2 = first
    while current_1.value != c_1:
        current_1 = current_1.next
    while current_2.value != c_2:
        current_2 = current_2.next
    while prev_1.next is not None and prev_1.next.value != c_1:
        prev_1 = prev_1.next
    while prev_2.next is not None and prev_2.next.value != c_2:
        prev_2 = prev_2.next
    next_1 = current_1.next
    next_2 = current_2.next
    if current_1.value == first.value:
        current_1.next = next_2
        current_2.next = current_1
        return current_2
    elif current_1.next.value == current_2.value:
        current_1.next = next_2
        prev_1.next = current_2
        current_2.next = current_1
    else:
        current_2.next = next_1
        prev_2.next = current_1
        current_1.next = next_2.next
        prev_1.next = current_2
    return first


c_1 = 0
c_2 = 1
e = 2

first = Node(0)
current = first

for i in range(1, e):
    node = Node(i)
    current.next = node
    current = current.next



print_list(first)
first = switch(first, c_1, c_2)
print_list(first)
