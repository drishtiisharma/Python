# Collections

>`List: [10,20,30]
>`Tuple: (10,20,30)
>`Set: {10,20,30}
>`Dict : {'key' : 'value'}



List
- Multiple items in single variable
- Ordered
- Mutable
- Allows duplicates
- [] brackets
- Accessed through index values
- List functions
- Len() – length of  list
- Index() – returns index of the 1st occurrence of a specified value
- Insert() – inserts item at specified index # eg. x.insert(2,”apple”)
- Append() – adds item at the end of the list
- Extend() – appending elements from other list to current , can also be done using ‘+’ operator
- Removes() – removes specified item
- Pop() – removes item from specified index, if index not specified removes the last item by default
- Del() – removes the item at specified index
- Clear() – empties the list, but the list remains
- Sort() – sorts the list alphanumerically in ascending order by default, for descending, use “reverse = True”. Uppercase before lowecase. If need case insensitive sorting use key=str.lower
- Reverse() – order reversed irrespective of alphabetic sequence
- Copy() – copies 1 list into another, another way is list(), can also use x[:] (the slicing operator
- List comprehension : shortest way to loop through lists

Tuples
- indexed
- Ordered
- Immutable/unchangeable
- Allows duplicates
- Uses () brackets
- Cannot remove items from a tuple, still if needed:
- Tuple->list(remove item)->tuple
- Tuples can be deleted entirely
- Can also be created without parantheses
- Rest functions are same as that of list
- How to change tuple values?
- Tuple->list(update/change/add value)->tuple
- Can add 2 tuples together, and even multiply them (repetition)
- Packing: putting multiple values in a tuple
- Unpacking: taking out values from the tuple and assigning them to separate variables. “\*” can be used when count(var)\<count(elements(tuple)), it will print them all as a list

Sets
- Unindexed
- Unordered
- Unchangeable/immutable
- Duplicates not allowed
- Can remove/add items
- Uses {} brackets
- True is same as 1, False is same as 0 in sets hence only 1 of each pair gets printed(duplicate eliminated)
- Cannot access the values using index, as unordered(either use loop or use in/not in operator with the specific value)
- Add() – can add items to the set (gets added to the last)
- Update() – adds 1 set to another, can also add any iterable object to the set
- Remove() and discard() – both are used to remove elements from the set. Remove() raises error if that element doesn’t exist, discard() doesn’t.
- Pop() is used to remove item too, but we’re not sure what item will be removed – as sets are unordered
- Clear() – used to remove the values, set remains even if empty
- Del() – set is completely deleted
- Joining sets:
- Union() – combines both sets and returns new set ( original sets remain unchanged)
- Update() – adds elements from 1 set to another and returns the modified set (only the set to which other elements from different set are added, is modified)
- Intersection() – will only return the duplicate value/s, can also use (&) operator
- Intersection\_update() – will return the duplicates but in the original(modified) set
- Difference() \_ will return a new set that will have only unique elements from the 1st set which are not present in the other set, can also use the  “-“ operator
- Difference\_update() – will return the unique values in 1st set(which arent present in other) but in the original(modified) set
- Symmetric\_difference() – will return a new set which has unique elements of both sets, can also use “^”
- Symmetric\_difference\_update() - will return an original set(modified) which has unique elements of both sets

Frozenset
- Immutable version of sets
- Unordered
- Unindexed
- Unchangeable
- Cannot even add/remove values from a frozenset
- Can create a copy of frozenset

Dictionary
- Ordered (Python 3.6 and earlier versions were unordered)
- Mutable
- Duplicates not allowed (unique keys, values can be duplicate)
- Stores data in key\:value pairs
- Can access the items of a dictionary by referring to its key name as: dict1[“name”]. can also use get() method. Difference wil be that: get() method wont throw an error if a key doesn’t exist, whereas the regular method does
- Keys() – will return a list of all keys in a dictionary
- Values() – will return list of all values in a dictionary
- Items() – will return list of all items in a dictionary
- Update() – will update dictionary with the already existing key/s, or add a new key\:value pair
- Pop() – removes the item with specified key name
- Popitem() – removes last inserted item
- Del() – removes specified item from dictionary

Difference between pop() and del()
Pop() removes a specified key and returns its value
Del() simply removes the key, without returning anything
- Clear() – empties the dictionary, but doesn’t delete it