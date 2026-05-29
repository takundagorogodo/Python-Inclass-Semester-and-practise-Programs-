# Import Counter to count occurrences of elements
from collections import Counter

# Input string
a = "aaaaabbbbccc"

# Create a Counter object
my_counter = Counter(a)

# Display Counter as a dictionary-like object
print(my_counter)

# Display items as (key, value) pairs
print(my_counter.items())

# Display only the values (counts)
print(my_counter.values())

# Display only the keys (elements)
print(my_counter.keys())

# Convert elements back into a list (repeats elements by their count)
print(list(my_counter.elements()))

# Get the most common element (top 1)
print(my_counter.most_common(1))

# Get the (element, count) tuple of the most common element
print(my_counter.most_common(1)[0])

# Get only the element (character) with highest frequency
print(my_counter.most_common(1)[0][0])


# Import namedtuple to create lightweight objects
from collections import namedtuple

# Define a namedtuple Point with fields x and y
Point = namedtuple('Point', 'x , y')

# Create a Point instance
pt = Point(1, -4)

# Access namedtuple attributes
print(pt.x, pt.y)


# Import OrderedDict to maintain insertion order
from collections import OrderedDict

# Create an OrderedDict
order_dict = OrderedDict()

# Insert key-value pairs
order_dict['a'] = 1
order_dict['b'] = 2
order_dict['c'] = 3
order_dict['d'] = 4
order_dict['e'] = 5

# Reassign value to existing key (order remains unchanged)
order_dict['a'] = 1

# Print the OrderedDict
print(order_dict)


# Import defaultdict to provide default values for missing keys
from collections import defaultdict

# Create a defaultdict with list as default factory
# d = defaultdict(int)
d = defaultdict(list)

# Assign values to keys
d['a'] = 1
d['b'] = 2

# Access existing keys
print(d['a'])
print(d['b'])

# Access a missing key (returns default value: empty list)
print(d['c'])


# Import deque for fast append and pop operations
from collections import deque

# Create an empty deque
d = deque()

# Append elements to the right
d.append(1)
d.append(3)
d.append(2)
print(d)

# Append more elements
d.append(5)

# Append elements to the left
d.appendleft(7)
d.appendleft(90)
print(d)

# Remove element from the left
d.popleft()
print(d)

# Remove element from the right
d.pop()
print(d)

# Extend deque from the right
d.extend([3, 6, 9, 2, 4])

# Extend deque from the left (adds in reverse order)
d.extendleft([67, 98, 56, 24, 47])
print(d)

# Rotate deque to the left
d.rotate(-4)
print(d)

# Rotate deque to the right
d.rotate(2)
print(d)

# Remove all elements from the deque
d.clear()
