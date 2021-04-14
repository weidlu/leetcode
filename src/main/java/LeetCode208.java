public class LeetCode208 {




    class Trie {

        tireNode root;

        /** Initialize your data structure here. */
        public Trie() {
            root = new tireNode();
        }

        /** Inserts a word into the trie. */
        public void insert(String word) {
            tireNode node = root;
            for (char c : word.toCharArray()) {
                if(node.next[c - 'a'] == null){
                    node.next[c - 'a'] = new tireNode();
                }
                node = node.next[c - 'a'];
            }
            node.isEnd = true;
        }

        /** Returns if the word is in the trie. */
        public boolean search(String word) {
            tireNode node = root;
            for (char c : word.toCharArray()) {
                node = node.next[c - 'a'];
                if (node == null) {
                    return false;
                }
            }
            return node.isEnd;
        }

        /** Returns if there is any word in the trie that starts with the given prefix. */
        public boolean startsWith(String prefix) {
            tireNode node = root;
            for (char c : prefix.toCharArray()) {
                node = node.next[c - 'a'];
                if (node == null) {
                    return false;
                }
            }
            return true;
        }

        class tireNode{
            private boolean isEnd;
            tireNode[] next;

            tireNode(){
                this.isEnd = false;
                next = new tireNode[26];
            }
        }
    }
}
