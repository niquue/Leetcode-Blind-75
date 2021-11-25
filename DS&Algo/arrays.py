new_list = [1, 2, 3]
result = new_list[0]
# Access is constant time operation

# Insert is linear runtime.
# Worst case scenario of insert is inserting at 0th index.
# Appending add items at end, runs in constant time.#
# Append has an "Amortized Constant Space Complexity" - Also happens with Insert operations
# .extend() takes a list and appends it to an existing list by taking each element and appending it until done
# # extend has a O(k) operation - where k is the number of elements.

if 1 in new_list:
    print(True)

for n in new_list:
    if n == 1:
        print(True)
        break
