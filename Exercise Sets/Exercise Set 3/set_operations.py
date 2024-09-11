set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

print("Set Difference")
print(f"set1 - set2 = {set1.difference(set2)}")
print(f"set2 - set1 = {set2.difference(set1)}\n")

print("Union of Sets")
print(f"set1 | set2 = {set1.union(set2)}\n")

print("Symmetric Difference")
print(f"set2 ^ set1 = {set2.symmetric_difference(set1)}")
print(f"set1 ^ set2 = {set1.symmetric_difference(set2)}\n")

print("Set Intersection")
print(f"set1 & set2 = {set1.intersection(set2)}")
print(f"set2 & set1 = {set2.intersection(set1)}")