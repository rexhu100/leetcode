"""Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs
pairs, determine if two sentences are similar. For example, words1 = ["great", "acting", "skills"] and words2 = [
"fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"],
["acting","drama"], ["skills","talent"]]. Note that the similarity relation is transitive. For example, if "great"
and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar. Similarity is also
symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar. Also,
a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = []
are similar, even though there are no specified similar word pairs. Finally, sentences can only be similar if they
have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus",
"good"].

Note:
- The length of words1 and words2 will not exceed 1000.
- The length of pairs will not exceed 2000.
- The length of each pairs[i] will be 2.
- The length of each words[i] and pairs[i][j] will be in the range [1, 20].
"""
from typing import List
from Solution import Solution


class UF:
    def __init__(self, size: int):
        self.parents = list(range(size))
        self.tree_sizes = [1 for _ in range(size)]

    def union(self, node1: int, node2: int):
        r1, r2 = self._get_root(node1), self._get_root(node2)
        if r1 == r2:
            return

        if self.tree_sizes[r1] > self.tree_sizes[r2]:
            self.parents[r2] = r1
            self.tree_sizes[r1] += self.tree_sizes[r2]
        else:
            self.parents[r1] = r2
            self.tree_sizes[r2] += self.tree_sizes[r1]

    def find(self, node1: int, node2: int) -> bool:
        return self._get_root(node1) == self._get_root(node2)

    def _get_root(self, node: int):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]

        return node


def sentence_similarity_two(words1, words2, pairs: List[List[str]]):
    word_map = dict()
    index = 0
    for pair in pairs:
        for w in pair:
            if w not in word_map:
                word_map[w] = index
                index += 1

    connectivity = UF(index)
    for pair in pairs:
        connectivity.union(word_map[pair[0]], word_map[pair[1]])

    for i in range(len(words1)):
        if words1[i] == words2[i]:
            continue

        if words1[i] not in word_map or words2[i] not in word_map or not connectivity.find(word_map[words1[i]], word_map[words2[i]]):
            return False

    return True


def main():
    sol = Solution()
    words1 = ["great", "acting", "skills", "laugh"]
    words2 = ["fine", "drama", "talent", "laugh"]
    pairs =[["great", "good"], ["fine", "good"],["acting", "drama"], ["skills", "talent"]]

    print(sol.areSentencesSimilarTwo(words1, words2, pairs))
    print(sentence_similarity_two(words1, words2, pairs))


if __name__ == "__main__":
    main()
