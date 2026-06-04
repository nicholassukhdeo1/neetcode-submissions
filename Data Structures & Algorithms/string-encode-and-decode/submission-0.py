class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = []

        # make it into a tuple of word, word_len

        for word in strs:
            encoded_string.append(str(len(word)))
            encoded_string.append('#')
            encoded_string.append(word)

            # maybe instead, remember index or something
            # or word length

            #2hi3how , the index with word length is len(word)

        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:

        # now we take Hello|World
        # add Hello, and World to a new string

        word_list = []
        i = 0

        # build each word, then add the word
        # into word_list when completed

        # the moment you hit a number, yk ur 
        # substr call.

        # for each number in s

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word_list.append(s[j+1 : j+1+length])
            i = j + 1 + length

        return word_list