import pandas as pd
# Create an original index
original_index = pd.Index([1, 2, 3])
# Create a new index by copying the original index
copied_index = pd.Index(original_index, copy=True)

# Modify the original index
original_index[0] = 10

# Print both indexes
print("Original Index:")
print(original_index)

print("\nCopied Index:")
print(copied_index)