#include <stdio.h>

struct Grade {
    char letter_grade;
    double gpa_scale;
};

struct GradedModule {
    char name;
    struct Grade grade;
};

struct GradedStudent {
    char name;
    struct GradedModule graded_module;
}



int main(void)
{
printf("To quit or insert data for another student press 0");
return 0;
}