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
    int postindex;
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        postindex=inorder.length-1;
        return build(inorder,postorder,0,inorder.length-1);
    }
    public TreeNode build(int[] inorder,int[] postorder,int start,int end)
    {
        if(start>end)
        {
            return null;
        }
        TreeNode root=new TreeNode(postorder[postindex]);
        postindex--;
        int index=0;
        for(int i=start;i<=end;i++)
        {
            if(inorder[i]==root.val)
            {
               index=i;
               break;
            }
        }
        root.right=build(inorder,postorder,index+1,end);
        root.left=build(inorder,postorder,start,index-1);
        
        return root;
    }
}