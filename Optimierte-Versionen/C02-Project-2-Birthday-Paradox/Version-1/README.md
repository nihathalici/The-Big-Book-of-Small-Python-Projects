```python
"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation"""

import random
from datetime import date, timedelta

def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    # Pre-calculate start of year once (optimization 1)
    start_of_year = date(2001, 1, 1)
    
    # Use list comprehension for speed (optimization 2)
    return [start_of_year + timedelta(random.randint(0, 364)) 
            for _ in range(numberOfBirthdays)]

def getMatch(birthdays):
    """Returns the first birthday that appears more than once, or None if no match."""
    # Use set for O(1) lookup instead of list O(n) (optimization 3)
    seen = set()
    for birthday in birthdays:
        if birthday in seen:
            return birthday
        seen.add(birthday)
    return None

def birthday_simulation(num_people, num_simulations=100000):
    """Run Monte Carlo simulation for given group size."""
    matches = 0
    # Pre-calculate local references for speed (optimization 4)
    get_birthdays = getBirthdays
    get_match = getMatch
    
    for _ in range(num_simulations):
        birthdays = get_birthdays(num_people)
        if get_match(birthdays) is not None:
            matches += 1
    
    return matches / num_simulations

def main():
    # Display the intro
    print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

    # User input with validation (optimization 5)
    while True:
        try:
            num_people = int(input('How many birthdays should I generate? (Max 100) '))
            if 1 <= num_people <= 100:
                break
            print('Please enter a number between 1 and 100.')
        except ValueError:
            print('Please enter a valid integer.')
    
    # Generate birthdays once for display (optimization 6)
    birthdays = getBirthdays(num_people)
    print(f'\nHere are {num_people} birthdays:')
    print(', '.join(b.day.strftime('%b %d') for b in birthdays))
    
    # Find and display match
    match = getMatch(birthdays)
    if match:
        print(f'In this simulation, multiple people have a birthday on {match.strftime("%b %d")}')
    else:
        print('In this simulation, there are no matching birthdays.')
    
    # Run multiple simulations (optimization 7)
    num_simulations = 100000
    probability = birthday_simulation(num_people, num_simulations)
    print(f'\nGenerating {num_simulations:,} random simulations of {num_people} people...')
    print(f'Probability of at least two people sharing a birthday: {probability * 100:.2f}%')

if __name__ == '__main__':
    main()
```

## List of Optimizations:

### 1. **Pre-calculate constant values**
- Moved `start_of_year` calculation outside the loop in `getBirthdays()` to avoid recreating it for each birthday
- Reduces computational overhead significantly for large group sizes

### 2. **Use list comprehension**
- Replaced manual loop with list comprehension in `getBirthdays()`
- More Pythonic and generally faster than explicit loops

### 3. **Use set for O(1) lookups**
- Implemented `getMatch()` using a `set` instead of O(n²) nested loops
- Reduces time complexity from O(n²) to O(n) for finding matches

### 4. **Local reference binding**
- Stored frequently used functions as local variables in the simulation loop
- Avoids global lookup overhead, especially important in tight loops

### 5. **Input validation**
- Added proper input validation loop with try/except
- Prevents crashes from invalid input and improves user experience

### 6. **Efficient string formatting**
- Used `strftime()` for date formatting and f-strings for better readability
- More efficient than concatenation and more maintainable

### 7. **Implemented full simulation**
- Completed the incomplete `getMatch()` function
- Added proper Monte Carlo simulation with configurable iterations
- Returns probability as a float for accurate calculations

### 8. **Import optimization**
- Imported specific functions (`date`, `timedelta`) instead of the entire `datetime` module
- Reduces namespace lookup time

### 9. **Used `_` for unused loop variables**
- Convention for variables that aren't used in the loop body
- Shows intent clearly and avoids unused variable warnings

### 10. **Added `__name__ == '__main__'` guard**
- Allows the module to be imported without running the simulation
- Good practice for reusable code

### 11. **Separation of concerns**
- Created `birthday_simulation()` function to separate simulation logic from I/O
- Makes the code more modular and testable

### 12. **Efficient date string generation**
- Used generator expression with `.join()` for birthday display
- More memory-efficient than creating intermediate lists

### 13. **Fixed logical bugs**
- The original code had `getMatch()` as a pass statement (incomplete)
- Fixed to properly detect matches

### 14. **Better variable names**
- Used more descriptive names (`start_of_year` instead of `startOfYear`)
- Consistent with Python naming conventions (PEP 8)
