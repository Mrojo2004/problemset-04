import math, queue
from collections import Counter

####### Problem 1 #######

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        x = p.get()
        y = p.get()
        z = TreeNode(x, y, (x.data[0] + y.data[0], ""))
        p.put(z)
        
    # return root of the tree
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code=None):
    if code is None:
        code = {}
    if node.left is None and node.right is None:
        code[node.data[1]] = prefix
    else: 
        get_code(node.left, prefix + "0", code)
        get_code(node.right, prefix + "1", code)
    return code

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    bits = math.ceil(math.log2(len(f)))
    return bits * sum(f.values())

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    return sum(f[c] * len(C[c]) for c in f)

for fname in ['f1.txt', 'alice29.txt', 'asyoulik.txt', 'fields.c', 'grammar.lsp']:
    f = get_frequencies(fname)
    fl = fixed_length_cost(f)
    T = make_huffman_tree(f)
    C = get_code(T)
    hc = huffman_cost(C, f)
    print("%s  fixed=%d  huffman=%d  ratio=%.3f" % (fname, fl, hc, hc / fl))

f = get_frequencies('f1.txt')
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))


