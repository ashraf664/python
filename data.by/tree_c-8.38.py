def  delete_suptree(self,p):
    node=self._valiodate(p)
    parent=node._parent

    if parent is not None:
        if parent._left is node:
            parent._left=None
        else:
           parent._right=None
    else:
        self._root=None
    count= self._suptree_size(node)
    self._size-=count 
