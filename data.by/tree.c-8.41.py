class LinkedBinaryTree:
    

    def clone(self):
        if self.is_empty():
            return LinkedBinaryTree()  

        new_tree = LinkedBinaryTree()
        new_root = new_tree.add_root(self._root._element)

        def _clone_subtree(orig_pos, new_pos):
            
            left = self.left(orig_pos)
            if left:
                new_left = new_tree.add_left(new_pos, left.element())
                _clone_subtree(left, new_left)
            right = self.right(orig_pos)
            if right:
                new_right = new_tree.add_right(new_pos, right.element())
                _clone_subtree(right, new_right)

        _clone_subtree(self.root(), new_root)
        return new_tree
  