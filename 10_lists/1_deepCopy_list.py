import copy

original = [["Tea", 15], ["Coffee", 25]]
backup = copy.deepcopy(original)

backup[0][1] = 99

print("Original:", original)
print("Backup:", backup)