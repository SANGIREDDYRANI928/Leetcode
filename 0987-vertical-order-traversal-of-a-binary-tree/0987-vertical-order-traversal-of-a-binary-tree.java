class Solution {

    class Pair {
        TreeNode node;
        int row;
        int col;

        Pair(TreeNode node, int row, int col) {
            this.node = node;
            this.row = row;
            this.col = col;
        }
    }

    public List<List<Integer>> verticalTraversal(TreeNode root) {

        List<List<Integer>> ans = new ArrayList<>();

        if (root == null)
            return ans;

        Map<Integer, Map<Integer, ArrayList<Integer>>> map = new TreeMap<>();

        Queue<Pair> queue = new LinkedList<>();

        queue.add(new Pair(root, 0, 0));

        while (!queue.isEmpty()) {

            Pair current = queue.poll();

            TreeNode node = current.node;
            int row = current.row;
            int col = current.col;

            map.putIfAbsent(col, new TreeMap<>());
            map.get(col).putIfAbsent(row, new ArrayList<>());

            map.get(col).get(row).add(node.val);

            if (node.left != null) {
                queue.add(new Pair(node.left, row + 1, col - 1));
            }

            if (node.right != null) {
                queue.add(new Pair(node.right, row + 1, col + 1));
            }
        }

        for (Map<Integer, ArrayList<Integer>> rows : map.values()) {

            List<Integer> list = new ArrayList<>();

            for (ArrayList<Integer> values : rows.values()) {

                Collections.sort(values);

                list.addAll(values);
            }

            ans.add(list);
        }

        return ans;
    }
}