#include <stdio.h>

int main() {
    int n;
    
    printf("enter the number of elements you want in the array=\n");
    scanf("%d",&n);
    
    int i;
    int arr[n];
    
    printf("enter the elements= \n");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++){
        printf("the elements in the old array is =");
        printf(" %d\n",arr[i]);
    }
    int x;
    printf("enter the element you want to append=");
    scanf("%d",&x);
    arr[n]=x;
    n++;
    for(i=0;i<n;i++){
        printf("the element in new array is = %d\n",arr[i]);
    }
    int y;
    int z;
    printf("enter the element to be inserted at a particular index=\n");
    scanf("%d",&y);
    printf("enter the index at which you want to insert=\n");
    scanf("%d",&z);
    for(i=n;i>z;i--){
        arr[i]=arr[i-1];
    }
    arr[z]=y;
    n++;
    for(i=0;i<n;i++){
        printf("the element in new array is = %d\n",arr[i]);
    }
    
    return 0;
}
*/
// writing the insertion code using pointers

#include <stdio.h>
#include <stdlib.h>
int main (){
    int *n;
    int i;
    int m;
    printf("enter the size of the array you want=  \n");
    scanf("%d",&m);
    n=(int*)malloc(m*sizeof(int));
    printf("the elements to input in the array are= \n");
    for(i=0;i<m;i++){
        scanf("%d",&n[i]);
    }
      
    for(i=0;i<m;i++){
        printf("the elements in the original array are= %d\n",n[i]);
    }
    int q;
    printf("enter the element to be added= \n");
    scanf("%d",&q);
    int v;
    printf("enter the index at which the element is to be added=\n");
    scanf("%d",&v);
    
    
    for(i=m;i>v;i--){
       
        n[i]=n[i-1];
    }
    n[v]=q;
    m++;
    

    for(i=0;i<m;i++){
        printf("the elements in the new array are= %d\n",n[i]);
    }
    
    // DELETION
    int f;
    int g;

    
    printf("enter the index and the element you want to delete= \n");
    scanf("%d %d",&f,&g);
    g=n[f];
    for(i=0;i<m-1;i++){
        n[i]=n[i+1];
    }
    
    m--;
    for(i=0;i<m;i++){
        printf("the elements in the new array are= %d\n",n[i]);
    }
    return 0;
        
}
'''
(( in the deletion only the first element is being deleted , why so?))
'''

// Online C compiler to run C program online finding an element , linear search

#include <stdio.h>

int main() {
    int n;
    int key;
    printf("enter the number of elements you want in the array=\n");
    scanf("%d",&n);
    
    int i;
    int arr[n];
    
    printf("enter the elements= \n");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++){
        printf("the elements in the old array is =");
        printf(" %d\n",arr[i]);
    }
    printf("enter the element you want to search in the array=\n");
    scanf("%d",&key);
    for(i=0;i<n;i++){
        
        if (key==arr[i]){
            printf("found at=%d ",i);
        }
    }
    return -1;
    return 0;
}
    
 