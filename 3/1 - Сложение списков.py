from random import randint


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


def length(first):
    i = 1
    current = first
    while current.next is not None:
        i += 1
        current = current.next
    return i


def sum_lists(first, second):
    first = reverse_link_values(first)
    second = reverse_link_values(second)
    current_1 = first
    current_2 = second
    r = abs(length(first) - length(second))
    if length(first) > length(second):
        for i in range(r):
            current_1 = current_1.next
        for i in range(length(first) - r):
            current_1.value += current_2.value
            current_1 = current_1.next
            current_2 = current_2.next
        s = first
    elif length(first) < length(second):
        for i in range(r):
            current_2 = current_2.next
        for i in range(length(first) - r):
            current_2.value += current_1.value
            current_1 = current_1.next
            current_2 = current_2.next
        s = second
    s = reverse_link_values(s)
    current = s
    for i in range(length(s)):
        if current.value >= 10 and current.next is not None:
            current.next.value += 1
            current.value -= 10
        if current.value >= 10 and current.next is None:
            node = Node(1)
            current.next = node
            current.value -= 10
        current = current.next
    return s


l = 3
p = 2

first = Node(randint(1,9))
current = first

for i in range(l):
    node = Node(randint(1,9))
    current.next = node
    current = current.next

second = Node(randint(1,9))
current = second

for i in range(p):
    node = Node(randint(1,9))
    current.next = node
    current = current.next

print_list(first)
print_list(second)

summ = sum_lists(first, second)

print_list(summ)

