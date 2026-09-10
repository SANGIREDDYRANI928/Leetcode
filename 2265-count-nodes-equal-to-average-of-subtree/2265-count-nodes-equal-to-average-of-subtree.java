class Solution {

    int ans = 0;

    public int averageOfSubtree(TreeNode root) {
        dfs(root);
        return ans;
    }

    // returns {sum, count}
    private int[] dfs(TreeNode node) {

        if (node == null) {
            return new int[]{0, 0};
        }

        // Get information from left subtree
        int[] left = dfs(node.left);

        // Get information from right subtree
        int[] right = dfs(node.right);

        // Calculate sum of current subtree
        int sum = left[0] + right[0] + node.val;

        // Calculate number of nodes in current subtree
        int count = left[1] + right[1] + 1;

        // Calculate average
        int average = sum / count;

        // Check whether current node equals average
        if (node.val == average) {
            ans++;
        }

        // Return sum and count to parent
        return new int[]{sum, count};
    }
}