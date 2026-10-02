class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1.declare an empty hash map
        # 2. loop through the strings
        # -> sort the letters of the word to create a key
        # -> else, create a new list for the sorted key
        # 3. group words with more than one anagram
        anagrams = dict()
        for word in strs:
            # Take the current word, rearrange all of its individual letters into alphabetical order, and glue them back together into a single text string
            sorted_word = ''.join(sorted(word))
            # check if we've already created a group for this specific combination of sorted letters
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                # add the word to the sublist of its anagram
                anagrams[sorted_word] = [word]

        # for group in anagrams.values():
        #     if len(group) > 1:
        #         print(group)

        return list(anagrams.values())