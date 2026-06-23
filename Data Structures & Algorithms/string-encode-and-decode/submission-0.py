class Solution:

    def encode(self, strs: List[str]) -> str:

        encode = ""

        for string in strs:
            encode += string + '£'

        return encode

        

    def decode(self, s: str) -> List[str]:

        string = ""
        output = []
        for ch in s:

            if ch != '£':
                string += ch
                continue
            
            output.append(string)
            string = ""

        return output
