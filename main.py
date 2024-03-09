# https://youtu.be/povMqm4cttM


'''
Python has the following data types built-in by default, in these categories:

1. Text Type: str

2. Numeric Types: int, float, complex

3. Sequence Types: list, tuple, range

4. Mapping Type: dict

5. Set Types: set, frozenset

6. Boolean Type: bool

7. Binary Types: bytes, bytearray, memoryview

8. None Type: NoneType

'''
# strings
str = 'some string'

# list (like array in js)
items = [1, True, 'false']
items2 = [5, 'six', False]

# can get same elemets from start index to end index, exclude end index
itemsFromInterval = items[1:3] # new list: [True, 'false']
itemsFromIndexToEnd = items[2:] # new list: ['false']
itemsFromStartToIndex = items[:2] # new list: [1, True]

# cobine lists 
itemsCombined = items + items2 # [1, True, 'false', 5, 'six', False]


# print(itemsCombined)
