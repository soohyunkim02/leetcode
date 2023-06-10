class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        result = ""
        for word in words:
            roots = []
            for root in dictionary:
                if root == word[:len(root)]:
                    roots.append(root)
            if len(roots):
                word = min(roots, key=len)
            result += word + " "
            
        return result[:-1]