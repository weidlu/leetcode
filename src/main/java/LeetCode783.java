public class LeetCode783 {

    int min = Integer.MAX_VALUE;
    TreeNode pre = null;

    public int minDiffInBST(TreeNode root) {
        dfs(root);
        return min;
    }

    public void dfs(TreeNode root) {
        if (root == null) {
            return;
        }
        if (min == 1){
            return;
        }
        dfs(root.left);
        if (pre != null) {
            min = Math.min(root.val - pre.val, min);
        }
        pre = root;
        dfs(root.right);
    }

    //[96,12,null,null,13,null,52,29]
    public static void main(String[] args) {
        TreeNode root = new TreeNode(96);
        TreeNode node1 = new TreeNode(12);
        TreeNode node2 = new TreeNode(13);
        TreeNode node3 = new TreeNode(52);
        TreeNode node4 = new TreeNode(29);
        root.left = node1;
        node1.right = node2;
        node2.right = node3;
        node3.left = node4;

        LeetCode783 leetCode783 = new LeetCode783();
        int i = leetCode783.minDiffInBST(root);
        System.out.println(i);


    }
}
