lst=[1,2,2,3,4,4,5]
print([item for item in lst if lst.count(item)== 1].reverse())


# The above code will not work as expected because the reverse() method returns None because it modifies the list in place.
# Therefore, the print statement will output None instead of the reversed list.
# To fix this, we can use slicing to reverse the list after filtering it.

# Here is the corrected code:
lst=[1,2,2,3,4,4,5] 
print([item for item in lst if lst.count(item)== 1][::-1])
# Output: [5, 3, 1]