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
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> q=new LinkedList<>();
        
        List<List<Integer>> a=new ArrayList<>();
        if(root==null) return a;
        q.add(root);
        while(!q.isEmpty())
        {
          List<Integer> a1=new ArrayList<>();
            int n=q.size();
            for(int i=0;i<n;i++)
            {
              TreeNode x=q.poll();
              a1.add(x.val);
              if(x.left!=null)
                {
                    q.add(x.left);
                }
              if(x.right!=null)
                {
                    q.add(x.right);
                }

            }
           a.add(a1);

        }
        return a;
        
    }
}