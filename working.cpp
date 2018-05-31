#include<bits/stdc++.h>
using namespace std;

struct node{
int data;
struct node *left;
struct node *right;
};

queue<struct node *>my;

int order(struct node * root)
{
    cout<<root->data<<"\n";
    if(root->left!=NULL)
    my.push(root->left);
   // cout<<root->left->data<<"\n";
    if(root->right!=NULL)
    my.push(root->right);
    struct node * aa;
    if(my.empty())return 0;;
    aa = my.front();
    my.pop();
    order(aa);

}

int main()
{
    struct node *a1 = (struct node *)malloc(sizeof(struct node *));
    struct node *a2 = (struct node *)malloc(sizeof(struct node *));
    struct node *a3 = (struct node *)malloc(sizeof(struct node *));
    struct node *a4 = (struct node *)malloc(sizeof(struct node *));
    struct node *a5 = (struct node *)malloc(sizeof(struct node *));

    a1->data = 1;
    a2->data = 2;
    a3->data = 3;
    a4->data = 4;
    a5->data = 5;
    a1->left = a2;
    a1->right = a3;
    a2->left = a4;
    a2->right = NULL;
    a3->right = a5;
    a3->left = NULL;
    a4->left = NULL;
    a4->right = NULL;
    a5->left = NULL;
    a5->right = NULL;
    order(a1);
}
