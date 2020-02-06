---
category: Leetcode
---

https://leetcode.com/problems/cousins-in-binary-tree/

1. Problem Analysis
  - Check two values are cousin in given tree
  
2. Prerequisite
  - BFS of tree( queue required )

3. N.B
  - Be aware of depth of tree
  - First check the values in tree are unique. This will change algorithm

4. Plan 1
  - By using queue, traverse tree by depth
  - Check node value is equal to given number
  - Check both childs are equal to given number or not
  - If both values are shown in same depth level, then return true, if not return false
  
5. Plan 2
  - By traversing tree by DFS, record depth of x and y
  - If both values are found, then stop traversing
  - During recording check x and y are not the chidles from same parent
  - If depth of values are same then they are cousin.
  
5. Result
  - Both showed 4ms. 74.92%, 11.2MB 86.67%

Plan 1
```
class Solution {
private:
    bool issame(int a, int x, int y ) {
        return a == x || a == y;
    };
public:
    bool isCousins(TreeNode* root, int x, int y) {
        int countchild = 0;
        int countnode = 1;
        queue<TreeNode*> q;
        q.push(root);
        TreeNode* node;
        bool halffound = false;
        while( !q.empty()) {
            node = q.front();
            q.pop();
            if( issame(node->val, x, y) ) {
                if( halffound )
                    return true;
                halffound = true;
            } else if( node->left && node->right ) {
                if( issame(node->left->val, x, y) && issame(node->right->val, x, y))
                    return false;
            }
            
            if( node->left ) {
                q.push( node->left );
                countchild++;
            }
            if( node->right ) {
                q.push( node->right );
                countchild++;
            }
                                    
            countnode--;
            if( countnode == 0 ) {
                countnode = countchild;
                countchild = 0;
                if( halffound )
                    return false;
            }
        }
        return false;
    }
};
```

Plan2
```
class Solution {
private:
    int levelx = -1;
    int levely = -1;
    bool decided = false;
    void traverse(TreeNode* root, int depth, int x, int y){
        if( !root )
            return;
        
        if( decided )
            return;
        
        if( root->val == x )
            levelx = depth;
        else if(root->val == y)
            levely = depth;
        
        if( root->left && root->right ) {
            if(( root->left->val == x && root->right->val == y) || (root->left->val == y && root->right->val == x )){
                decided = true;
                return;
            }
        }
        
        if(levelx > -1 && levely > -1 ){
            decided = true;
            return;
        }
        
        traverse(root->left, depth +1 , x, y);
        traverse(root->right, depth +1 , x, y);
    }
public:
    bool isCousins(TreeNode* root, int x, int y) {
        traverse(root, 0, x, y);
        if( levelx == levely && levelx > -1 )
            return true;
        return false;
    }
};
```
