class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l = [first]
        for i,j in zip(l,encoded):
            l.append(i^j)
        return l

        '''
        output = [first]
        for i in range(0, len(encoded)):
            output.append(output[i] ^ encoded[i])
        return output


        '''