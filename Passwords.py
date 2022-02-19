#!/usr/bin/env python3

import sys
import time
import random
import collections
import itertools

class Passwords:
  def __init__(self, password_options, options_per_column):
    self.password_options = password_options
    self.options_per_column = options_per_column
    self.password_length = max(map(len, self.password_options))
    # A nested list where each list is the letters that can appear in that column.
    self.letter_options = []
    for column_number in range(self.password_length):
      options = set()
      for password in self.password_options:
        options.add(password[column_number])
      self.letter_options.append(sorted(options))
    # Debugging counters
    self.total_combos_generated = 0
    self.valid_combos_generated = 0

  def letter_frequencies_by_column(self):
    """
    Prints a table of how many password have each letter in each column.
    """
    all_letter_counts = []
    for column_number in range(self.password_length):
      letters_in_column = map(lambda password: password[column_number], self.password_options)
      occurrences = collections.Counter(letters_in_column)
      letter_counts = [letter + str(count) for (letter, count) in sorted(occurrences.items(), key=lambda pair: pair[1], reverse=True)]
      all_letter_counts.append(letter_counts)
    for row in itertools.zip_longest(*all_letter_counts, fillvalue='  '):
      print('  '.join(row))

  def possible_words_from_letters_in_column(self, letters, column):
    """
    If you only know one column of letters (for example, the 6 letter choices in column 0), which passwords could be the correct one?
    """
    return [password for password in self.password_options if password[column] in letters]

  def average_possible_words_in_column(self, column=0):
   """
   Assume you're given only one column of information (for example, the 6 possible letters in the first column). How many passwords could be the correct one?
   This method takes every possible combination of letters in that column, counts how many passwords would be valid, and returns the average.
   """
   options = self.letter_options[column]
   combinations = list(itertools.combinations(options, self.options_per_column))
   possible_combinations = len(combinations)
   total_possible_words = 0
   for possible_letters in combinations:
     total_possible_words += len(self.possible_words_from_letters_in_column(possible_letters, column))
   return total_possible_words / possible_combinations

  def average_possible_passwords_given_columns_one_and_two(self):
    """
    Iterate through every possible combiination of letters in column 1 and column 2. First make sure the combination is valid (there's at least one possible password). Here we're assuming there's some combination of values for the rest of the columns that would lead to exactly one correct results, as the game dictates.
    Add the possible passwords for this combination to a total. Then, divide by the total number of valid combinations we checked. This is the average number of passwords you can narrow it down two given the possible letters from the first two columns.
    """
    combinations_from_column_1 = list(itertools.combinations(self.letter_options[0], 6))
    combinations_from_column_2 = list(itertools.combinations(self.letter_options[1], 6))
    valid_combinations = 0
    total_possible_passwords = 0
    for column1 in combinations_from_column_1:
      for column2 in combinations_from_column_2:
        possible_passwords = len([password for password in self.password_options if password[0] in column1 and password[1] in column2])
        if possible_passwords > 0:
          valid_combinations += 1
          total_possible_passwords += possible_passwords
    return total_possible_passwords / valid_combinations

  def get_valid_letter_combo(self):
    while True:
      options = [random.sample(self.letter_options[i], self.options_per_column) for i in range(self.password_length)]
      self.total_combos_generated += 1
      if len([password for password in self.password_options if all([password[i] in options[i] for i in range(self.password_length)])]) == 1:
        self.valid_combos_generated += 1
        return options

  def average_possible_passwords_given_columns(self):
    # TODO: keep track of which valid letter combos I've already tried and ignore exact repeats. Count how many times this actually comes up and what impact it has on time to execute.
    combinations_tested = 0
    total_possible_passwords = [0 for _ in range(self.password_length-1)]
    last_print = time.time()
    print('Number of possible passwords given the first N columns of letter possibilities')
    while True:
      try:
        options = self.get_valid_letter_combo()
        possible_passwords = self.password_options
        for column in range(len(total_possible_passwords)):
          possible_passwords = [password for password in possible_passwords if password[column] in options[column]]
          total_possible_passwords[column] += len(possible_passwords)
        combinations_tested += 1
        if time.time() - last_print > 1:
          last_print = time.time()
          sys.stdout.write(f'\rCombinations tested: {combinations_tested}, 0: {len(self.password_options):.3f},  ')
          for column in range(len(total_possible_passwords)):
            sys.stdout.write(f'{column+1}: {total_possible_passwords[column] / combinations_tested:.3f},  ')
          sys.stdout.write(f'{self.password_length}: {1:.3f}')
          sys.stdout.flush()
      except KeyboardInterrupt:
        print()
        return


if __name__ == "__main__":
  standard_password_module = Passwords(["about", "after", "again", "below", "could", "every", "first", "found", "great", "house", "large", "learn", "never", "other", "place", "plant", "point", "right", "small", "sound", "spell", "still", "study", "their", "there", "these", "thing", "think", "three", "water", "where", "which", "world", "would", "write"], 6)
  standard_password_module.average_possible_passwords_given_columns()
  print(f'Of {standard_password_module.total_combos_generated:,} generated letter combinations, only {standard_password_module.valid_combos_generated:,} were valid (having exactly one correct password), or {standard_password_module.valid_combos_generated / standard_password_module.total_combos_generated * 100:.2f}%.')

"""
Simulation ~500,000 valid letter combinations: 
Given the first 0 columns of information, there are, on average, 35.0 possible passwords.
Given the first 1 columns of information, there are, on average, 14.07 possible passwords (should be 14 exactly).
Given the first 2 columns of information, there are, on average, 6.19 possible passwords (should be 6.029303267166398 exactly).
Given the first 3 columns of information, there are, on average, 3.49 possible passwords.
Given the first 4 columns of information, there are, on average, 1.62 possible passwords.
Given the first 5 columns of information, there are, on average, 1.0 possible passwords.

Given a random set of 6 letters from column one and 6 from column two, there are 15,030,015 possibilities.
Of those, 14,956,967 are possible (some combinations have 0 password options).
On average, 6.0293 passwords will be possible.

Number of combinations per column: 5005, 3003, 462, 3003, 462
Average possible words per column (assuming 6 letter options in a column):
14.0
15.0
19.09090909090909
15.0
19.09090909090909
=> Column one has the fewest possible words, then column two (tied with 4). The operator should give the expert the first two columns.

t6  h8  e7  l6  e8
w6  o7  u6  n6  t6
s5  e3  i6  e5  r5
a3  t3  a5  r4  d5
p3  i2  r4  s3  l3
f2  r2  t2  i2  n2
l2  a2  o1  c2  y2
b1  l2  l1  u1  w1
c1  b1  v1  o1  g1
e1  f1  h1  a1  k1
g1  g1  g1  g1  h1
h1  v1      h1
n1  m1      d1
o1  p1      t1
r1
"""
