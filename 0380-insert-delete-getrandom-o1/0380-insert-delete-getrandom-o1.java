import java.util.*;
class RandomizedSet {
    HashMap<Integer,Integer> mp;
    ArrayList<Integer> list;
    Random rm;
    public RandomizedSet() {
        mp=new HashMap<>();
        list=new ArrayList<>();
        rm=new Random();
        
    }
    
    public boolean insert(int val) {
        if(mp.containsKey(val))
        {
            return false;
        }
        list.add(val);
        mp.put(val,list.size()-1);
        return true;
    }
    
    public boolean remove(int val) {
        if(!mp.containsKey(val))
        {
            return false;
        }
        int index=mp.get(val);
        int last=list.get(list.size()-1);
        list.set(index,last);
        mp.put(last,index);
        list.remove(list.size()-1);
        mp.remove(val);
        return true;
        
    }
    
    public int getRandom() {
        int rand_idx=rm.nextInt(list.size());
        return list.get(rand_idx);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */