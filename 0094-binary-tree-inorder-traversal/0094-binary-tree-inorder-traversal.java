import java.util.*;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    public List<Integer> inorderTraversal(TreeNode root) {
        
        Stack<TreeNode> s=new Stack<>();
        ArrayList<Integer> a=new ArrayList<>();
        while(root!=null || s.empty()==false)
        {
            while(root!=null)
            {
                s.push(root);
                root=root.left;

            }
            TreeNode top=s.pop();
            a.add(top.val);
            root=top.right;
        }
        return a;

        
    }
}