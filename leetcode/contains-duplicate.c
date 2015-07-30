#include<stdio.h>

typedef struct rbnode{
        int v;
        bool color;/*0: red; 1: black*/
        struct rbnode* left;
        struct rbnode* right;
        struct rbnode* p; /*parent*/
} * RBT;

RBT rotateleft(RBT t){
        RBT x = t;
        RBT y = x->right;
        
        y->left->parent = x;
        x->right = y->left;
        
        y->parent = x->parent;
        if(x->parent)
                if(x->parent->left == x)
                        x->parent->left = y;
                else
                        x->parent->right = y;
        //else y is the root node.

        x->parent = y;
        y->left = x;

        return y;
}

RBT rotateright(RBT t){
        RBT x = t;
        RBT y = x->left;
        x->left = y->right;

        y->right->parent = x;

        y->parent = x->parent;
        if(x->parent)
                if(x->parent->left==x)
                        x->parent->left = y;
                else
                        x->parent->right = y;
        //else y is the root node.
        x->parent = y;
        y->right = x;

        return y;
}

bool isRed(RBT t){
        if(t==NULL)
                return 0;
        return t->color;
}



bool insert(RBT t, int val)
{
        RBT x = t;
        RBT y = NULL;
        RBT tnode = (RBT)malloc(sizeof(struct rbnode));

        while(x!=NULL){
                //while x is not NULL, y alwaxs points to the father of x
                y = x;
                if(x->v > val){
                        x = x->left;
                }
                else{
                        x = x->right;
                }
        }

        tnode->v = val;
        tnode->parent = y;

        if(y != NULL)
                if (tnode->v == y->v)
                        //found duplicate
                        return true;

                if (tnode->v < y->v)
                        y->left = tnode;
                else    y->right = tnode;


        //paint tnode red bx default
        tnode->color = 0;
        tnode->left = NULL;
        tnode->right = NULL;
        rb_insert_fixup(x,tnode)

       // if(y==NULL){
       //         //tree t is a emptx tree
       //         tnode->color = 1;
       //         return tnode;
       // }
       // else{
       //         if(x==y->left) y->left = tnode;
       //         else y->right = tnode;
       // }
        
}

rb_insert_fixup(RBT x,RBT z){


