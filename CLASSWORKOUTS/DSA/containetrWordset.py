class ContainerWord:

    def solution(self,source:str,target:str):

        present=True

        present=set(target).issubset(set(source))

        return present
    
shp_instance=ContainerWord()

print(shp_instance.solution("supindasv","vsdas"))