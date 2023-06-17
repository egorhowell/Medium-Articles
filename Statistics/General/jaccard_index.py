from typing import List


def jaccard_index(list1: List, list2: List) -> float:
    """
    Computes the Jaccard index for two lists.

    Args:
        list1: First list
        list2: Second list

    Returns:
        The Jaccard index, a similarity score of the two lists

    """

    set1 = set(list1)
    set2 = set(list2)

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    jaccard_index = len(intersection) / len(union)

    return jaccard_index


list1 = [1, 3, 4, 5, 6]
list2 = [1, 4, 6, 7, 8]

result = jaccard_index(list1, list2)
print(result)
