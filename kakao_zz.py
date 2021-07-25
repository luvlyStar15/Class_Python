def solution(priorities:list,location:int)->int:
    loc = [i for i in range(len(priorities))]
    final = []

    while(len(priorities)!=0):
        if(priorities[0] == max(priorities)):
            final.append(loc.pop(0))
            priorities.pop(0)

        else:
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))

    return final.index(location)+1
