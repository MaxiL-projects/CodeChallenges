team=str(input())
count = int(0)
danger = 7
neighbors = danger - 1


def football_func(team, danger, neighbors):

                                                    #if string is smaller than length 7, then by definition not dangerous
    if len(team)<danger:
        return 'NO'
    else:
        for i in range(0,len(team)-neighbors):      #because we calculate for the number of neighbors
            #print(f'i:{i}')
            count = 0                               #reset if not correct (through break)
            for j in range(1,danger):
                #print(f'j:{j}')
                if team[i]==team[i+j]:
                    count = count+1
                    if count==neighbors:            #we need 6 relations for 7 neighbors =). 
                        #print(f'count:{count}')
                        return 'YES'        
                else: 
                    break
        if count != danger:                         #if after iterating 6 same neighbors not found, no danger
            #print(f'count:{count}')
            return 'NO'


answer = football_func(team, danger, neighbors)
print(answer)