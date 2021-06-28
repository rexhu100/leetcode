"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:
Input: "eceba"
Output: 3
Explanation: tis "ece" which its length is 3.

Example 2:
Input: "ccaabbb"
Output: 5
Explanation: tis "aabbb" which its length is 5.
"""

from Solution import Solution


def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    max_len = 0
    cur_substring = {}
    n = len(s)
    left, right = 0, 0
    while right <= n:
        while len(cur_substring) > 2:
            cur_substring[s[left]] -= 1
            if cur_substring[s[left]] == 0:
                cur_substring.pop(s[left])

            left += 1

        if right < n:
            cur_substring[s[right]] = cur_substring.get(s[right], 0) + 1

        max_len = max(max_len, right - left)
        right += 1

    return max_len


def main():
    sol = Solution()
    s = "ecweeba"
    print(lengthOfLongestSubstringTwoDistinct(s))
    print(sol.lengthOfLongestSubstringTwoDistinct(s))

    s = "ccaabbb"
    print(lengthOfLongestSubstringTwoDistinct(s))
    print(sol.lengthOfLongestSubstringTwoDistinct(s))

    s = "ccaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbpppppppppppppppppppppzpppppppppppppppppppppppppppppppppppp"
    print(lengthOfLongestSubstringTwoDistinct(s))
    print(sol.lengthOfLongestSubstringTwoDistinct(s))

if __name__ == '__main__':
    main()
