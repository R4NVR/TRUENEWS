struct node{
    int data;
    struct node* next;
}; 

    int a[]={1,2,3,4,5};
    int i;
    struct node *t,*last,*first;
    first=(struct node*)malloc(sizeof(struct node));
    first->data=a[0];
    first->next=NULL;
    last=first;

    for(i=1;i<5;i++){
        t=(struct node*)malloc(sizeof(struct node));
        t->data=a[i];
        t->next=NULL;
        last->next=t;
        last=t;
    }
    printf("linked list is : \n");
    struct node *p=first;
    while(p != NULL){
        printf("%d\n",p->data);
        p=p->next;
    }
    // insert a node
    struct node *q;
    int x;
    q=(struct node*)malloc(sizeof(struct node));
    printf("enter the value to be inserted= \n");
    scanf("%d",&x);
    q->data=x;
    q->next=NULL;
    last->next=q;
    last=q;
    
    printf("new linked list is : \n");
    p=first;
    while(p != NULL){
        printf("%d\n",p->data);
        p=p->next;
    }
    //insert at first;
    struct node *w;
    int s;
    w=(struct node*)malloc(sizeof(struct node));
    printf("enter the value to be inserted= \n");
    scanf("%d",&s);
    w->data=s;
    w->next=first;
    first=w;
    
    
    printf("new linked list is : \n");
    p=first;
    while(p != NULL){
        printf("%d\n",p->data);
        p=p->next;
    }
    
    
    
    struct node{
        int data;
        struct node* next;
      struct node*prev;
    }; 
    int a[]={1,2,3,4,5,6,7};
    int i;
    struct node *last,*first;
    first=(struct node*)malloc(sizeof(struct node));
    first->data=a[0];
    last=first;
    first->next=NULL;
    first->prev=NULL;
    
    struct node *p;
    p=(struct node*)malloc(sizeof(struct node));
    p=first;
    for(i=1;i<7;i++){
        p=(struct node*)malloc(sizeof(struct node));
        p->data=a[i];
        last->next=p;
        p->next=NULL;
        p->prev=last;
        last=p;
    }
    
    p=first;
    printf("doubly linked list is as follows= \n");
    while (p!=NULL){
       
        printf("%d\n",p->data);
        p=p->next;
    }
    // insert at second index
    /*1 ke baad 23 daldo , toh hame ek pointer banake 1 ka next usse point karvana hoga and 2 ke prev ko bhi */
    
    struct node *q;
    q=(struct node*)malloc(sizeof(struct node));
    int w;
    printf("enter the element to be inserted= \n");
    scanf("%d",&w);
    q->data=w;
    q->prev=first;
    q->next=first->next;
    first->next=q;
    first->next->prev=q;
    
    p=first;
    printf("doubly linked list is as follows= \n");
    while (p!=NULL){
       
        printf("%d\n",p->data);
        p=p->next;
    }