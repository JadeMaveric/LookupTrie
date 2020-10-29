LookupTrees (Trie) are an alternative to Dictionaries that provide better space usage when the keys are similar  

**Usage**  
```python
from poc import *
lk = Lookup('a') # alphabet doesn't matter in the python poc

lk.insert('Julius', 7832)
lk.insert('Julia', 7763)

lk.lookup('Julius')         # Returns 7832
lk.lookup('Julia')          # Returns 7763

lk.delete('Julia')
lk.lookup('Julia')          # Returns None
lk.lookup('Julius')         # Returns 7832
```

The tree after inserting both `Julius`, `Julia` and `Jupyter` would lookup something like this
```
   ┌p─y─t─e─r(2204)
   │
J─u─l─i┬u─s(7832)
       │
       └a(7763)
```

*An ideal C implentation would have...*  
**Time Complexity:**  
All operations - insert, lookup, delete - are O(k), where k is the length of the key, which for most use cases will be close to constant  

**Space Complexity:**  
Each node in the tree hold 3 values:  
* Letter - 1 byte character that stores the letter the node represents  
* Value  - Pointer to the value held by the string, NULL initialised.  
* Children - Array of pointers to children nodes. The array is as long as the alphabet
If size(alphabet) is A, size(pointer) is P, total number of characters is N, number of unique character is M  
then the worst case is O((1+A\*P+P)\*N)
and the best case is O((1+A\*P+P)\*M)


*Be warned, you're better off using actual dictionaries. There's only a small subset of problems where this is better. (The coupon codes problem in Xtreme 14.0 is why this was developed, and I later learnt they're called tries)*

It's possible to improve space complexity even further by condensing groups of CharacterNodes into a single StringNode wherever possible