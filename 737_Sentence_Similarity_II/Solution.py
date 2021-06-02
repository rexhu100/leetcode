import collections
from typing import List


class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        similars = collections.defaultdict(set)
        for w1, w2 in pairs:
            similars[w1].add(w2)
            similars[w2].add(w1)

        def dfs(words1, words2, visited):
            for similar in similars[words2]:
                if similar in visited: continue
                if words1 == similar:
                    return True
                else:
                    visited.add(similar)
                    if dfs(words1, similar, visited):
                        return True
            return False

        for w1, w2 in zip(words1, words2):
            if w1 != w2 and not dfs(w1, w2, set([w2])):
                return False

        return True
