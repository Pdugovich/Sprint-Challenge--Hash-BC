#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for k, v in enumerate(weights):
        hash_table_insert(ht, v, k)

    for k, v in enumerate(weights):
        if hash_table_retrieve(ht, limit - v):
            index = hash_table_retrieve(ht, limit - v)

            if index >= k:
                return [index, k]
            elif index < k:
                return [k, index]

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
