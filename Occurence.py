import array as arr

array = str(input("Enter a sentence:"))
occ = str(input("Enter what word you want to check the occurence of:"))
array = arr.array(array)
print("Original array: "+str(array))
print("Number of occurences: "+str(array.count(occ)))

