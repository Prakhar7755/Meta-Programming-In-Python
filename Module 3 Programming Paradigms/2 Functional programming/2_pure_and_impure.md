<!-- Pure functions are used in functional programming to assure the integrity of data outside the scope of the pure function.


Yes
Correct
Correct. A pure function is used in functional programming because it does not change or have any effect on a variable, data, list, or set beyond its own scope.     -->

Certainly! In functional programming, understanding the difference between **pure functions** and **impure functions** is crucial. Let's break it down:

1. **Pure Functions**:

   - A pure function always returns the **same output** for the **same input**.
   - It **does not have side effects**, meaning it doesn't modify external state or environment.
   - Benefits of pure functions:
     - Easier to reason about and test.
     - No hidden dependencies or states.
     - Reusable and composable.
     - Can be memoized for performance.
   - Example:
     ```python
     def add(a, b):
         return a + b
     ```

2. **Impure Functions**:
   - An impure function:
     - Has **side effects** (e.g., modifies global variables, changes object state, makes network requests).
     - Does **not always return the same output** for the same input.
   - Examples:
     - Modifying a global variable:
       ```python
       oldValue = 7
       def add(newValue):
           global oldValue
           oldValue += newValue
           return oldValue
       ```
     - Modifying an object's state:
       ```python
       person = {'name': 'John', 'age': 30}
       def increment_age(person):
           person['age'] += 1
           return person['age']
       ```

Remember, pure functions are predictable and reliable, while impure functions introduce complexity and hidden effects. Choose wisely based on your needs! 😊 ¹²³
