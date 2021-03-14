import java.util.ArrayList;

/**
 * leetcode 706
 * @author weidlu
 */
public class MyHashMap {

    private static final int CAPACITY = 10009;
    private final ArrayList<Pair>[] buckets;

    /**
     * Initialize your data structure here.
     */
    public MyHashMap() {
        buckets = new ArrayList[CAPACITY];
    }

    /**
     * value will always be non-negative.
     */
    public void put(int key, int value) {
        int hash = hash(key);
        ArrayList<Pair> list = buckets[hash];

        if (list != null) {
            for (Pair pair1 : list) {
                if (pair1.key == key) {
                    pair1.val = value;
                    return;
                }
            }
            Pair pair = new Pair(key, value);
            list.add(pair);
        } else {
            ArrayList<Pair> l = new ArrayList<>();
            Pair pair = new Pair(key, value);
            l.add(pair);
            buckets[hash] = l;
        }
    }

    /**
     * Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
     */
    public int get(int key) {
        int hash = hash(key);
        ArrayList<Pair> list = buckets[hash];
        if (list != null){
            for (Pair pair : list) {
                if (pair.key == key){
                    return pair.val;
                }
            }
        }
        return -1;
    }

    /**
     * Removes the mapping of the specified value key if this map contains a mapping for the key
     */
    public void remove(int key) {
        int hash = hash(key);
        ArrayList<Pair> bucket = buckets[hash];
        if (bucket != null){
            int index = -1;
            for (int i = 0; i < bucket.size(); i++) {
                if (bucket.get(i).key == key){
                    index = i;
                    break;
                }
            }
            if (index != -1){
                bucket.remove(index);
            }
        }
    }

    static class Pair {
        int key;
        int val;

        Pair(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }

    private int hash(int key){
        return key % CAPACITY;
    }

}
