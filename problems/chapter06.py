"""
Practice exercises from Algorithms, by  Dasgupta, Papadimitriou, Vazirani (2006)
"""

def contiguous_sum_6_1(inputs):
    if not inputs:
        return []

    start_locs = list(range(len(inputs)))
    sums = inputs[:]

    for i, val in enumerate(inputs):
        if i == 0:
            continue
        
        x = sums[i-1] + val
        if x > val:
            sums[i] = x
            start_locs[i] = start_locs[i-1]

    largest = sums[0]
    largest_index = 0

    for i, s in enumerate(sums):
        if s > largest:
            largest = s
            largest_index = i
    
    return inputs[start_locs[largest_index]:largest_index+1]


def hotel_stops_6_2(inputs):
    costs = [0] * len(inputs)
    origins = [0] * len(inputs)

    for i, a in enumerate(inputs):

        best_origin = -1
        cost = (200  - a)**2

        for j in range(i):
            cost_to_reach_j = costs[j]
            cost_from_j_to_i = (200 - (a - inputs[j]))**2
            c = cost_to_reach_j + cost_from_j_to_i
            if c  < cost:
                cost = c
                best_origin = j
        
        costs[i] = cost
        origins[i] = best_origin
    
    route = [inputs[-1]]
    o = origins[-1]
    while o > -1:
        route.append(inputs[o])
        o = origins[o]

    return route[::-1]


def word_split_6_4(text, is_word):
    """A substring ending at element i_n is a valid set of words if
    there is some valid set of words ending at i_j-1 for which i_j to i_n is a valid word.

    
    text: string with no delineation between words
    is_word: boolean function that takes a string as argument
        and returns whether the string is a single word or not
    """
    memo = dict()

    for i in range(len(text)):
        for j in range(i+1):
            word = text[j:i+1]
            if is_word(word):
                if j == 0 or j-1 in memo:
                    memo[i] = j
                    break
    
    x = len(text)-1
    is_word_string = x in memo
    words = []

    if is_word_string:
        while x >= 0:
            words.append(text[memo[x]:x+1])
            x = memo[x] - 1
        words.reverse()

    return is_word_string, words


def pebbling_a_checkerboard_6_5(checkerboard):
    """
    Args:
        checkerboard: 4 x N list of ints
    
    Types:
    0: _ _ _ _
    1: x _ _ _
    2: _ x _ _
    3: _ _ x _
    4: _ _ _ x
    5: x _ x _
    6: x _ _ x
    7: _ x _ x
    """
    pass


def symbol_multiplication_6_6(input):
    """Let us define multiplication according to the table below.
    Find an efficient algorithm that examines a string of symbols
    and determines whether it is possible to parenthesize them
    in such a way that the resulting expression is 'a'.
    Example: ((b(bb))(ba))c = a
    """
    # Multiplication table. ab = b, bc = a, etc.
    M = {
        'a': {
            'a': 'b',
            'b': 'b',
            'c': 'a',
        },
        'b': {
            'a': 'c',
            'b': 'b',
            'c': 'a',
        },
        'c': {
            'a': 'a',
            'b': 'c',
            'c': 'c',
        },
    }

    if not input:
        return False
    if len(input) == 1:
        return input[0] == 'a'
    if len(input) == 2:
        return M[input[0]][input[1]] == 'a'

    def combine_possibilities(a, b):
        poss = set()
        for a_letter in a:
            for b_letter in b:
                poss.add(M[a_letter][b_letter])
        return poss

    # P(i, j) is the possible values that can be produced
    # by multiplying all the elements between i and j inclusive
    P = []
    for i in range(len(input)):
        row = []
        for j in range(len(input)):
            if i == j:
                row.append({input[i]})
            else:
                row.append(set())
        P.append(row)

    for subproblem_size in range(1, len(input)):
        for i in range(len(input)-subproblem_size):
            j = subproblem_size + i

            local_possibilities = set()
            sub = 1
            while j-sub >= i:
                p = combine_possibilities(P[i][j-sub], P[j-sub+1][j])
                local_possibilities |= p
                sub += 1
            P[i][j] = local_possibilities
            
    return 'a' in P[0][-1]
