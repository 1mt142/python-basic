
# Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# -1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Check if "apple" is present in the list


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("ok")


# Change Item Value | To change the value of a specific item, refer to the index number:

thislist[1] = "Imtiaz"
print(thislist[1])
# insert | item middle of array
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# ---

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("thislist")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# To append elements from another list to the current list, use the extend() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# pop
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# clear

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


# looping

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# by index
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
