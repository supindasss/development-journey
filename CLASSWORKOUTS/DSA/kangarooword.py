class Kangaroo:

    def solution(self,source,target):

        present=False

        target_index=0

        source_index=0

        while target_index<len(target) and source_index<len(source):

            if target[target_index]==source[source_index]:

                target_index+=1

            source_index+=1
        
        if target_index==len(target):

            present=True

        return present

ka=Kangaroo()
print(ka.solution("supindas","nda"))