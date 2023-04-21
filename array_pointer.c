# include <stdio.h>
/*Playing with pointers,
array pointers
Author: Francis*/


int main()

{
    int myNumbers[5] = {12,43,13,5,89};
    int *ptr = myNumbers;
    int i;


// printing values in arrays
    for (i = 0; i <5; i++) 
    {
        printf("%d\n", myNumbers[i]);
    }


// printing the memory addressess of the arrays 
    for (i = 0; i < 5; i++) 
    {
        printf("%p\n", &myNumbers[i]);

    }

// getting the size of the arrays
printf("%lu", sizeof(myNumbers));


/*showing how pointers and arrays relate with each other*/

// memory address of myNumbers array
printf("%p\n", myNumbers);

// memory address of first element of the array
printf("%p\n", &myNumbers[0]);

//value of first element in the array
printf("%d\n", *myNumbers);


// looping through the elements of the array with pointers

for (size_t i = 0; i < 5; i++)
{
    printf("%d\n", *(ptr + i));
}




    return 0;
}
