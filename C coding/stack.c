#include <stdio.h>
#include <stdlib.h>
int main (){
    // stack using array
    struct stack{
        int size;
        int top;
        int *s;
    };
    
    struct stack st;
    st.size=10;
    st.s=(int*)malloc(st.size*sizeof(int));
    st.top=-1;
    int x;
    while (1){
        

        printf("enter an element= \n");
        scanf("%d",&x);
        if(x==-1){
            break;
        }
    
        if(st.top==st.size-1){
            printf("overflow");
        }
   
        else{
            st.top++;
            st.s[st.top]=x;
        
        }
    }
    
    // display
    int i;
    for(i=st.top;i>=0;i--){
        printf("%d",st.s[i]);
    printf("\n");
    }
    return 0;

}


