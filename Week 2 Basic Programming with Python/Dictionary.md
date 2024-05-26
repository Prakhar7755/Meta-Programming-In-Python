In Python, a dictionary is a mutable, unordered collection of key-value pairs. It's one of the most powerful and commonly used data structures in Python due to its flexibility and efficiency in mapping keys to values. Here's an overview of dictionaries along with their properties and methods, along with code examples:

### Properties of Dictionaries:

1. **Unordered**: Dictionary elements are not ordered, meaning they do not maintain any specific order of insertion.
2. **Mutable**: Dictionaries can be modified after creation.
3. **Keys must be unique and immutable**: Keys within a dictionary must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any data type and mutable.
4. **Flexible**: Values can be of any data type, including other dictionaries, lists, tuples, etc.

### Methods of Dictionaries:

#### 1. Creating a Dictionary:

```python
# Method 1: Using curly braces
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Method 2: Using the dict() constructor
my_dict = dict(name='John', age=30, city='New York')

# Method 3: Using a list of tuples
my_dict = dict([('name', 'John'), ('age', 30), ('city', 'New York')])
```

#### 2. Accessing Elements:

```python
print(my_dict['name'])  # Output: John
```

#### 3. Adding or Modifying Elements:

```python
my_dict['gender'] = 'Male'  # Adding a new key-value pair
my_dict['age'] = 31          # Modifying an existing value
```

#### 4. Removing Elements:

```python
del my_dict['age']     # Remove a particular item
my_dict.pop('city')    # Remove and return value for a given key
my_dict.clear()        # Remove all items
```

#### 5. Copying a Dictionary:

```python
new_dict = my_dict.copy()   # Shallow copy
```

#### 6. Getting Keys, Values, and Items:

```python
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

# Iterating through keys, values, and items
for key in my_dict:
    print(key)             # Prints keys
for value in my_dict.values():
    print(value)           # Prints values
for key, value in my_dict.items():
    print(key, value)      # Prints key-value pairs
```

#### 7. Dictionary Comprehension:

```python
squared_numbers = {x: x*x for x in range(5)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

#### 8. Merging Dictionaries:

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}  # Output: {'a': 1, 'b': 3, 'c': 4}
```

#### 9. Dictionary Membership Test:

```python
print('name' in my_dict)   # Output: True
```

#### 10. Length of a Dictionary:

```python
print(len(my_dict))   # Output: Number of key-value pairs in my_dict
```

These are some of the basic operations and methods associated with dictionaries in Python. They are incredibly versatile and find extensive use in various Python applications.