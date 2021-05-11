# ICS3U Lists

Your task is to write a program that asks for a bunch of items, then allows the user to interactively ask for details about his/her list.

## Grade ICS3U Initial Input
The user will be asked to input a list as follows:
```python
>> Please Enter a list: [1,2,3,4,"hello",5,6,"milk"]
```
Then you can convert it into a list as follows
```python
list_of_items = input("Please enter a list: ")
# Note: eval is EVIL. I'm only using it here to make things easier.
list_of_items = eval(list_of_items)
```

## Program Execution
Once the list has been entered, the user will have a choice to enter one of 5 possible values:
```
length
first
last
range
sort
```

Given any of these commands, the program should output the appropriate data.

Note that if the user types "range" you will need another set of inputs to get the start and end of the range.

Note on sorting:
1. You need to use the `sorted()` function so as to not ruin the first and last calls.
2. Call sorted like this: `sorted(list_of_items, key=str)`. Trust me. Otherwise you'll get an error saying it doesn't know how to use `<` on ints and strs.

## Example Execution of Code
```
>>> Enter a list of items: ['Milk', 'Bread', 2, 'Pineapple Pizza']

Enter a command: first
Milk

Enter a command: length
4

Enter a command: sort
[2, 'Bread', 'Milk', 'Pineapple Pizza']

Enter a command: range
Sart: 1
End: 3
['Bread', 2]

Enter a command: done
```
Notice how the user can keep entering commands until he/she types done. Think about today's lesson and how that might be accomplished.
