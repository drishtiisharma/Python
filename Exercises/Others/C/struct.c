#include <stdio.h>
#include <string.h>

struct emp{
    int id;
    float salary;
};

int main(){
    struct emp emp1;
    emp1.id = 102;
    emp1.salary = 85000;
    
    printf("old:\n");
    printf("id: %d\n",emp1.id);
    printf("salary: %f\n",emp1.salary);


    struct emp alice;
    alice.id = 101;
    alice.salary = 45000;

    emp1 = alice;

    printf("new:\n");
    printf("id: %d\n",emp1.id);
    printf("salary: %f\n",emp1.salary);

}

