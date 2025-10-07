class LFUCache {
    class Node {
        int key, val, freq;
        Node(int key, int val) {
            this.key = key;
            this.val = val;
            this.freq = 1;
        }
    }

    private int capacity, minFreq;
    private Map<Integer, Node> keyToNode;
    private Map<Integer, LinkedHashSet<Integer>> freqToKeys;

    public LFUCache(int capacity) {
        this.capacity = capacity;
        this.minFreq = 0;
        keyToNode = new HashMap<>();
        freqToKeys = new HashMap<>();
    }

    public int get(int key) {
        if (!keyToNode.containsKey(key)) return -1;

        Node node = keyToNode.get(key);
        int oldFreq = node.freq;
        node.freq++;

        freqToKeys.get(oldFreq).remove(key);
        if (freqToKeys.get(oldFreq).isEmpty()) {
            freqToKeys.remove(oldFreq);
            if (oldFreq == minFreq) minFreq++;
        }

        freqToKeys.computeIfAbsent(node.freq, k -> new LinkedHashSet<>()).add(key);

        return node.val;
    }

    public void put(int key, int value) {
        if (capacity == 0) return;

        if (keyToNode.containsKey(key)) {
            keyToNode.get(key).val = value;
            get(key);
            return;
        }

        if (keyToNode.size() >= capacity) {
            LinkedHashSet<Integer> keys = freqToKeys.get(minFreq);
            int evictKey = keys.iterator().next();
            keys.remove(evictKey);
            if (keys.isEmpty()) freqToKeys.remove(minFreq);
            keyToNode.remove(evictKey);
        }

        Node newNode = new Node(key, value);
        keyToNode.put(key, newNode);
        freqToKeys.computeIfAbsent(1, k -> new LinkedHashSet<>()).add(key);
        minFreq = 1;
    }
}
