class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        li=list(word)
        firstLtter=li[0]

        if firstLtter>='A' and firstLtter<='Z': #첫글자가 대문자

            li.pop(0)

            if len(li)==0:
                return True

            if li[0] >= 'a' and li[0]<='z': # 두번째 글자가 소문자
                for w in li[1:]:
                    if w < 'a' or w > 'z':
                            return False

            if li[0] >= 'A' and li[0]<='Z': # 두번째 글자가 대문자
                    for w in li[1:]:
                        print("2: "+w)
                        if w < 'A' or w > 'Z':
                            return False 


        else: # 첫글자가 소문자

            for w in li:
                print("3: "+w)
                if w < 'a' or w > 'z':
                    return False



        return True

