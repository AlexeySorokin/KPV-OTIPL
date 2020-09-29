import numpy as np


def longest_common_substring(first, second):
    table = np.zeros(shape=(len(first), len(second)), dtype=int)
    for j in range(len(second)):
        table[0,j] = int(first[0] == second[j])
    for i in range(len(first)):
        table[i,0] = int(first[i] == second[0])
    for i in range(1, len(first)):
        for j in range(1, len(second)):
            table[i, j] = table[i-1,j-1]+1 if first[i] == second[j] else 0
    i_max, j_max = np.unravel_index(np.argmax(table), table.shape)
    max_length = table[i_max, j_max]
    answer = {"first_start": i_max-max_length+1, "first_end": i_max+1,
              "second_start": j_max-max_length+1, "second_end": j_max+1,
              "length": max_length, "match": first[i_max-max_length+1:i_max+1]}
    return answer
