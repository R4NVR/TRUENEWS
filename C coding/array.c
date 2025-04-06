#include<stdio.h>
int main (){

    int i;
    int n;

    printf("enter the number elements you want in an array = \n");
    scanf("%d",&n);

    int arr[n];

    printf("enter the elements in the array = \n");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);

    }


    for(i=0;i<n;i++){
        printf("%d",arr[i]);
    }
    

// inserting at a particular index
    int x,y;
    printf("enter the index = \n");
    scanf("%d",&x);
    printf("enter the element= \n");
    scanf("%d",&y);
    for(i=n;i>x;i--){
        arr[i]=arr[i-1];

    }
    arr[x]=y;
    n++;
    for(i=n;i>x;i--){ //bymistake reversing aagya
        printf(arr[i]);
    }

    return 0;
}

