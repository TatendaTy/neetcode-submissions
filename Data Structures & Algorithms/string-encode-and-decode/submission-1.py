class Solution:
    def encode(self, strs: List[str]) -> str:
        string = "" # initialize an empty string
        # iterate through the list and encode the strings
        for word in strs:
            string += str(len(word)) + '#' + word
        return string  

    def decode(self, s: str) -> List[str]:
        result = [] # initialize an empty list to store the decoded words
        pointer1 = 0
        # loop through the encoded words
        while pointer1 < len(s):
            pointer2 = pointer1
            # use the delimiter to split the encoded words
            while s[pointer2] != '#':
                pointer2 += 1 # Keep moving pointer2 forward until it finds '#'
            word_length = int(s[pointer1:pointer2]) # get the length of each word
            result.append(s[pointer2+1: pointer2 + 1 + word_length ])
            pointer1 = pointer2 + 1 + word_length # Move to the next word

        return result
