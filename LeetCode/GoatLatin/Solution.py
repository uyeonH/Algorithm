class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        #  쪼개어 문자열을 리스트로 변환
        words=S.split()
        result=[]
        answer=[]
        count=1

        for word in words:
        
            # 모음 체크
            if word[0] in ['a','e','i','o','u','A','E','I','O','U']:
                result.append(word+'ma')
                
            # 자음 체크    
            else:
                result.append(word[1:]+word[0]+'ma')
                
        # 순서에 맞게 'a' 추가하기
        for word in result:
            answer.append(word+'a'*count)
            count+=1
            
        # 리스트를 다시 문자열로 변환    
        return (' '.join(answer))
