#include

void foo(void);
void bar(int);

int main(int argc, char **argv)
{
    foo();
    bar(100);
}

void foo()
{
    printf("Hello, it's foo function here\n");
}

void bar(int x)
{
    printf("Hello, it's bar function here. Wow! You send me a %d... it's such a number! ;)\n", x);
}
