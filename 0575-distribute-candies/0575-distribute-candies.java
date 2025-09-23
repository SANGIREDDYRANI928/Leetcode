class Solution {
    public int distributeCandies(int[] candyType) {
        int c=0;
        int maxi=(candyType.length)/2;
        HashSet<Integer> h=new HashSet<>();
        for(int i=0;i<candyType.length;i++)
        {if(h.contains(candyType[i])==false){
            h.add(candyType[i]);
            c+=1;
        }
        if(c==maxi)
        {
            return c;
        }
        }
        return c;


        
    }
}