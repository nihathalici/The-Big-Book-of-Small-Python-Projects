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
