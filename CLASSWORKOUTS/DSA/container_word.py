#company : travidux

class ContainerWord:

    def solution(self,source,target):

        prsent=True

        for ch in target:

            if ch not in source:

                prsent=False

                break
            
        return prsent
         
contaioner_instance=ContainerWord()

print(contaioner_instance.solution("supindasv","vsdas"))
