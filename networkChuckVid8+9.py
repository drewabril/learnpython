#more lists, adding things with several methods
#python list:

camping_list = ["tent", "sleeping bag", "water", "coffee", "knife"]

camp_site = ["Crystal Lake", 404, 89.3, True]

#append method. adds one at a time
camping_list.append("toilet paper")

print(camping_list)

camping_list.append("bidet")
print(camping_list)


#extend method, provide another list to add to first one
camping_list.extend(["marshmallows", "truck"])
print(camping_list)

# just add two lists with a + operator
camping_list = camping_list + ["dog", "charger"]

print(camping_list)

#add things to a specific place on a list
camping_list.insert(3, "golf clubs")

print(camping_list)

camping_list.insert(-1, "tea")
print(camping_list)


#remove one item from a list
camping_list.remove("dog")
print(camping_list)


#remove something from a list by index/order
camping_list.pop(3)
print(camping_list)

#confirm what was removed from the list
print("The " + camping_list.pop(3) + " was removed from your list")

#how many items are on the list?
print(len(camping_list))
