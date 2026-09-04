# Conditionals

Conditional Statements
- If…else (2 conditions)
- Elif (3 or more conditions) – better because it ignores the remaining conditions once the ‘true’ one is found
- Else – catches anything that isnt caught by the preceding conditions i.e. the conditions before it were ‘false’; provides a default action; comes at last
- Shorthand if – if only 1 statement to execute, can put it on the same line as the if statement, but still need the colon after it
- Shorthand if else – value\_if\_true if conditon else value\_if\_false, aka ternary operator/conditional expression



- Nested if – if statement inside another if statement.
Inner if statement only runs if the outer if condition is true.
Use as per need:
Nested if statement: when the second condition depends on the first to be true and we need true/false checks at multiple levels
Logical operators: when we need all the conditions to be true at the same time.

Match statement
Instead of writing many if…else statements, we can use the match statement
Match selects one of the many code blocks to be executed