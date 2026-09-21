import java.util.*;
class TimeMap {
    class Pair{
        String value;
        int timestamp;
        Pair(String value,int timestamp)
        {
            this.value=value;
            this.timestamp=timestamp;
        }
    }
    HashMap<String,ArrayList<Pair>> mp;
    public TimeMap() {
        mp=new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if(!mp.containsKey(key))
        {
            mp.put(key,new ArrayList<>());
        }
        mp.get(key).add(new Pair(value,timestamp));
        
    }
    
    public String get(String key, int timestamp) {
        if(!mp.containsKey(key)) return "";
        ArrayList<Pair> l=mp.get(key);
        int low=0;
        int h=l.size()-1;
        String ans="";
        while(low<=h)
        {
            int mid=(low+h)/2;
            if(l.get(mid).timestamp<=timestamp)
            {
                ans=l.get(mid).value;
                low=mid+1;
            }
            else{
                h=mid-1;
            }
        }
        return ans;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */