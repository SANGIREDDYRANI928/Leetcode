import java.util.HashMap;
class LRUCache {
    class Node{
        int key;
        int value;
        Node prev;
        Node next;
        Node(int key,int value)
        {
            this.key=key;
            this.value=value;
        }
    }
    Node lru;
    Node mru;
    int capacity;
    HashMap<Integer,Node> map;

    public LRUCache(int capacity) {
        this.capacity=capacity;
        map=new HashMap<>();
        lru=new Node(0,0);
        mru=new Node(0,0);
        lru.next=mru;
        mru.prev=lru;
    }
    public void insert(Node newNode)
    { 
       newNode.prev=mru.prev;
       mru.prev.next=newNode;
       newNode.next=mru;
       mru.prev=newNode;
    }
    public void remove(Node newNode)
    {
       newNode.prev.next=newNode.next;
       newNode.next.prev=newNode.prev;
    }
    public int get(int key) {
        if(!map.containsKey(key))
        {
            return -1;
        }
        Node newNode=map.get(key);
        remove(newNode);
        insert(newNode);
        return newNode.value;
    }
    
    public void put(int key, int value) {
        if(map.containsKey(key))
        {
            Node newNode=map.get(key);
            newNode.value=value;
            remove(newNode);
            insert(newNode);
            return;
        }
        Node newNode=new Node(key,value);
        map.put(key,newNode);
        insert(newNode);
        if(map.size()>capacity)
        {
           Node delete=lru.next;
           remove(delete);
           map.remove(delete.key);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */