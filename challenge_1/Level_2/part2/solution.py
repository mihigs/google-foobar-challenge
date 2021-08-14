moves = [10, 17, 15, 6, -10, -17, -15, -6];
visited = [None] * 64;

def validMoves(src):
    validMoves = [];
    for move in moves:
        if (src + move > 63) or (src + move < 0): # Is the move out of bounds on the x axis
            continue;
        if abs((src % 8) - ((src + move) % 8)) > 2: # Is the move out of bounds on the y axis
            continue;
        if visited[src + move] == 1: # Is the tile already visited
            continue;
        validMoves.append(move);
    return validMoves;

def tour(srcArr, dest, path = 0):
    nextMoves = [];

    for src in srcArr:
        if src == dest: # Check if we reached the destination
            return path;
        visited[src] = 1;

        for move in validMoves(src): # Store next moves for the next iteration
            nextMoves.append(src + move);

    return tour(nextMoves, dest, path + 1); # Start the next iteration
            
def solution(src, dest):
    if (src < 0) or (src > 63) or (dest < 0) or (dest > 63):
        return;

    return tour([src], dest);
