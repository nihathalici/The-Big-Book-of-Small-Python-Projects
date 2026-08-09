## **Performance Optimizations:**

1. **`random.sample()` instead of `random.shuffle()` + loop**
   - Directly selects unique digits without having to shuffle the entire list first
   - Shorter and more efficient code

2. **`set()` for faster lookup**
   - Converts the secret number to a set for O(1) access time
   - Instead of O(n) with the `in` operator on strings

## **Code Quality:**

3. **f-Strings instead of `.format()`**
   - More modern, readable string formatting
   - Shorter and clearer syntax

4. **`for-else` construct**
   - More elegant handling of the "out of guesses" case
   - The `else` block only executes when the loop ends without `break`

## **Structural Improvements:**

5. **Separate `getValidGuess()` function**
   - Separates input validation from main logic
   - Improves readability and reusability

6. **Reduced nesting**
   - Less deep indentation through smarter control structures
   - `for` loop with `range()` instead of manual counter variable

7. **Automatic counter variable**
   - `for numGuesses in range(1, MAX_GUESSES + 1)` instead of `numGuesses = 1` with manual incrementing
   - Less boilerplate code, less error-prone

## **Maintainability:**

8. **More consistent error handling**
   - Uniform validation with helpful error messages
   - Better user guidance for incorrect inputs

9. **More compact list processing**
   - `''.join(random.sample(...))` instead of manual string concatenation
   - More Pythonic way of working with sequences

These optimizations make the code faster, more readable, and more maintainable without changing the game's behavior.
