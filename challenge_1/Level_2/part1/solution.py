def solution(h, q):
    # Check if the height is inside its domain
    if h < 1 or h > 30:
        return

    # Check if the array fullfils the requirements
    lenQ = len(q)
    if lenQ > 10000 or lenQ < 1:
        return

    if len(q) != len(set(q)):
        return

    rootNode = (2 ** h) - 1

    # Result array creation
    p = []

    for number in q:
        p.append(traverse(rootNode, number, h))
    
    return p

# Recursive function for traversing the binary tree
def traverse(node, number, height, parent = -1):
    if number == node:
        return parent
    if number < node:
        return traverse(node - (2 ** (height - 1)), number, height - 1, node)
    if number > node:
        return traverse(parent - 1, number, height, parent)

# print(solution(3, [7, 3, 5, 1]))
print(solution(5, [19, 14, 28]))

