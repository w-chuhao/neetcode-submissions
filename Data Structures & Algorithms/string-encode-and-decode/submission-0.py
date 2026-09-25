class Solution:
    def encode(self, strs):
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, encoded):
        result = []
        i = 0

        while i < len(encoded):
            j = i

            # Find the "#" after the length
            while encoded[j] != "#":
                j += 1

            # Extract and convert the length
            word_length = int(encoded[i:j])

            # The word starts immediately after "#"
            word_start = j + 1
            word_end = word_start + word_length

            result.append(encoded[word_start:word_end])

            # Move to the beginning of the next encoded word
            i = word_end

        return result