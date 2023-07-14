#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Grade {
    char* letterGrade;
    double gpaScale;
    int index;
};

struct GradedModule {
    char* name;
    struct Grade grade;
};

// struct GradedStudent {
//     char name;
//     struct gradedModule module;
// };


// struct Grade createGradeMapping()
// {
//     char letterGrades[] = {A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, E+, E, E-, F+, F}; 
// //     double gpaScaleGrades[] = {4.2, 4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6, 2.4, 2.2, 2, 1.8, 1.6, 1.4, 1.2, 1};

// // }
 
        



int main(void)
{

    // assigning value to struct elements  
    struct Grade g1 = {"A+", 4.2};
    struct Grade g2 = {"A", 4};
    struct Grade g3 = {"A-", 3.8};
    struct Grade g4 = {"B+", 3.6};
    struct Grade g5 = {"B", 3.4};
    struct Grade g6 = {"B-", 3.2};
    struct Grade g7 = {"C+", 3};
    struct Grade g8 = {"C", 2.8};
    struct Grade g9 = {"C-", 2.6};
    struct Grade g10 = {"D+", 2.4};
    struct Grade g11 = {"D", 2.2};
    struct Grade g12 = {"D-", 2};
    struct Grade g13 = {"E+", 1.8};
    struct Grade g14 = {"E", 1.6};
    struct Grade g15 = {"E-", 1.4};
    struct Grade g16 = {"F+", 1.2};
    struct Grade g17 = {"F", 1};

    char n1[100], m1[100];
    int p1;

    printf("To quit or insert data for another student press 0\n");
    printf("Enter student name: ");
    fgets(n1, sizeof(n1), stdin);
    // printf("Your name is: %s", n1);
    printf("Enter module name: ");
    fgets(m1, sizeof(m1), stdin);
    // printf("Your module is: %s", m1);
    printf("Enter grade (%%): ");
    scanf("%d", &p1);
    // printf("Your number is: %d\n", p1);

    if (p1>=90)
    {
        struct Grade g = {"A+", 4.2};
        // printf("Output: %s", g.letterGrade);
        struct gradedModule gm = {n1, g};
        
        
    }
    else if(p1>=80)
    {
        struct Grade g = {"A", 4};
            
    }
    else if(p1>=70)
    {
        struct Grade g = {"A-", 3.8};
    
    }
    else if(p1>=67)
    {
        struct Grade g = {"B+", 3.6};
    
    }
    else if(p1>=64)
    {
        struct Grade g = {"B", 3.4};
    
    }
    else if(p1>=60)
    {
        struct Grade g = {"B-", 3.2};
    
    }
    else if(p1>=57)
    {
        struct Grade g = {"C+", 3};
    
    }
    else if(p1>=54)
    {
        struct Grade g = {"C", 2.8};
    
    }
    else if(p1>=50)
    {
        struct Grade g = {"C-", 2.6};
    
    }
    else if(p1>=49)
    {
        struct Grade g = {"D+", 2.4};
    
    }
    else if(p1>=47)
    {
        struct Grade g = {"D", 2.2};
    
    }
    else if(p1>=45)
    {
        struct Grade g = {"D-", 2};
    
    }
    else if(p1=44)
    {
        struct Grade g = {"E+", 1.8};
    
    }
    else if(p1>=42)
    {
        struct Grade g = {"E", 1.6};
    
    }
    else if(p1>=40)
    {
        struct Grade g = {"E-", 1.4};
    
    }
    else if(p1=39)
    {
        struct Grade g = {"F+", 1.2};
    
    }
    else 
    {   struct Grade g = {"F", 1};

    }
    
    printf("%s", g.letterGrade);
    
    

    




return 0;
}


