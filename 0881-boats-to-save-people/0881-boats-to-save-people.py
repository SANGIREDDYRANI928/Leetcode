class Solution:
    def numRescueBoats(self, people, limit) :
        count=0
        people.sort()
        p1=0
        p2=len(people)-1
        while p1<p2:
            sum1=people[p1]+people[p2]
            if(sum1>limit):
                if people[p2]<=limit:
                    count+=1
                    p2-=1
            elif(sum1<=limit):
                count+=1
                p1+=1
                p2-=1
        if p1==p2:
            return count+1
        else:
            return count
        