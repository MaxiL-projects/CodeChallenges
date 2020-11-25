team=str(input())
count = int(0)
danger = 7
neighbors = danger - 1

#if string is smaller than length 7, then by definition not dangerous

def football_func(team, danger, neighbors):
    if len(team)<danger:
        return 'NO'
    else:
        for i in range(0,len(team)-danger+1):    
            #print(f'i:{i}')
            count = 0
            for j in range(1,danger):
                #print(f'j:{j}')
                if team[i]==team[i+j]:
                    count = count+1
                    if count==neighbors:   #we need 6 relations for 7 neighbors =)
                        #print(f'count:{count}')
                        return 'YES'        
                else: 
                    break
        if count != danger:
            #print(f'count:{count}')
            return 'NO'


answer = football_func(team, danger, neighbors)
print(answer)