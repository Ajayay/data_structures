class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words)
        longest_word = 0
        ans = ''
        trie = {}
        
        for word in words:
            cur_prefixes_length = 0
            cur_node = trie
            applicable = True
            for i in range(len(word)):
                letter = word[i]
                if letter in cur_node:
                    cur_prefixes_length += 1
                    applicable = applicable and 'end' in cur_node[letter]
                else:
                    cur_node[letter] = {}
                    applicable = applicable and i == len(word) - 1
                    cur_prefixes_length += 1

                if not applicable:
                    break

                cur_node = cur_node[letter]
            cur_node['end'] = True

            if applicable and cur_prefixes_length > longest_word:
                longest_word = cur_prefixes_length
                ans = word

        return ans