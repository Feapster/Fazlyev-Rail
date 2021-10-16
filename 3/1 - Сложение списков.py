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


def length(first):
    i = 1
    current = first
    while current.next is not None:
        i += 1
        current = current.next
    return i


def sum_lists(first, second):
    current_1 = first
    current_2 = second
    len_1 = min(length(first),length(second))
    len_2 = max(length(first), length(second))
    s = Node(0)
    current = s
    for i in range(len_2 - 1):
        node = Node(0)
        current.next = node
        current = current.next
    current_3 = s
    for i in range(len_1):
        current_3.value = current_1.value + current_2.value
        current_1 = current_1.next
        current_2 = current_2.next
        current_3 = current_3.next
    print_list(s)
    s = reverse_link_values(s)
    current = s
    for i in range(len):
        if current.value >= 10 and current.next is not None:
            current.next.value += 1
            current.value -= 10
        if current.value >= 10 and current.next is None:
            node = Node(0)
            current.next = node
            current.next.value += 1
            current.value -= 10
        current = current.next
    return s


l = 12
p = 8

first = Node(0)
current = first

for i in range(1,l):
    node = Node(i * 2)
    current.next = node
    current = current.next

second = Node(p)
current = second



for i in range(p - 1, -1, - 1):
    node = Node(i * 4)
    current.next = node
    current = current.next


print_list(first)
print_list(second)

summ = sum_lists(first, second)

print_list(summ)
