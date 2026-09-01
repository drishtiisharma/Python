# Compile Time Polymorphism
- polymorphism is determined at the compile time, before the program runs
- aka ***Static Polymorphism*** or ***Early Binding***
- commonly achieved through ==**Method Overloading**==
- compiler decides which method/operation should be used
- common in languages like java and c++

> [!NOTE]
> Python doesn't support traditional method overloading in the same way.
> 
> **Traditional Method Overloading**
> We define multiple methods with the same name but different parameter lists.
> ```
> class Calculator {
 >   int add(int a, int b) {
>        return a + b;
   > }
 >   int add(int a, int b, int c) {
 >      return a + b + c;
 >   }
>}
>```
> **Why Python doesn't support it?**
> Because Python is dynamically typed and resolves method calls at runtime, so defining multiple methods with the same name would simply cause the **last definition to overwrite the previous one.**

