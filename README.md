# pretty_print_bst
Pretty printing branches of a Python binary tree.

## STRUCTURE

```
class BinTree:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right
```

## HOW TO USE
Place this file next to the file in which you want to use the function:
```
your_folder/
|-- your_file.py
|-- pretty_print.py
```
Add this line to your file:
```
from pretty_print import *

# your code
```
Display your BinTree this way:
```
print_tree(B)
```

## EXAMPLE
```
# your_file.py
from pretty_print import *

B = BinTree(1, BinTree(2, None, None), BinTree(3, None, None))
print_tree(B)

>>>>
 1
/ \
2 3
```

## KNOWN ISSUES (that will probably never be fixed)
* Key length is not taken into account.
