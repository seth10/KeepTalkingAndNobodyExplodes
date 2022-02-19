#!/usr/bin/env python3

import sys
import time
import random
import collections
import itertools

class Passwords:
  def __init__(self, password_options):
    self.password_options = password_options
    self.password_length = max(map(len, self.password_options))

  def letter_options_by_column(self):
    """
    Returns a nested list. Each item in the root list is a list of letters that can appear in that column. i.e. The first list is the letters that can show up in the first position, the second list is the letters that can appear in the second position, etc. Each list is sorted.
    """
    letter_options = []
    for column_number in range(self.password_length):
      options = set()
      for password in self.password_options:
        options.add(password[column_number])
      letter_options.append(sorted(options))
    return letter_options

  def letter_frequencies_by_column(self):
    """
    Returns a nested list. Each item in the root list is a list of strings, a single letter followed by the number of times that letter appears in that column. For instance, if the 3rd list starts with 'e7', that means the letter 'e' appears 7 times in the third position. The lists are sorted by most common letters first.
    """
    all_letter_counts = []
    for column_number in range(self.password_length):
      letters_in_column = map(lambda password: password[column_number], self.password_options)
      occurrences = collections.Counter(letters_in_column)
      #letter_counts = sorted([letter + str(count) for (letter, count) in occurrences.items()])
      letter_counts = [letter + str(count) for (letter, count) in sorted(occurrences.items(), key=lambda pair: pair[1], reverse=True)]
      all_letter_counts.append(letter_counts)
    return all_letter_counts

  def possible_words_from_letters_in_column(self, letters, column):
    return list(filter(lambda word: word[column] in letters, self.password_options))

  def average_possible_words_in_column(self, column=0):
   options = self.letter_options_by_column()[column]
   combinations = list(itertools.combinations(options, 6))
   possible_combinations = len(combinations)
   total_possible_words = 0
   for possible_letters in combinations:
     total_possible_words += len(self.possible_words_from_letters_in_column(possible_letters, column))
   return total_possible_words / possible_combinations

  def average_possible_passwords_given_columns_one_and_two(self):
    options_for_column_1 = self.letter_options_by_column()[0]
    options_for_column_2 = self.letter_options_by_column()[1]
    combinations_from_column_1 = list(itertools.combinations(options_for_column_1, 6))
    combinations_from_column_2 = list(itertools.combinations(options_for_column_2, 6))
    valid_combinations = 0
    total_possible_passwords = 0
    for column1 in combinations_from_column_1:
      for column2 in combinations_from_column_2:
        possible_passwords = len([password for password in self.password_options if password[0] in column1 and password[1] in column2])
        if possible_passwords > 0:
          valid_combinations += 1
          total_possible_passwords += possible_passwords
    return total_possible_passwords / valid_combinations

  def average_possible_passwords_given_columns(self, count=3):
    letter_options = self.letter_options_by_column()
    valid_combinations = 0
    total_possible_passwords = 0
    last_print = time.time()
    while True:
      try:
        if time.time() - last_print > 1:
          last_print = time.time()
          sys.stdout.write(f'\rCombinations tried: {valid_combinations}, average possible passwords: {total_possible_passwords / valid_combinations}')
          sys.stdout.flush()
        options = [random.sample(letter_options[i], 6) for i in range(count)]
        possible_passwords = len([password for password in self.password_options if all([password[i] in options[i] for i in range(count)])])
        if possible_passwords > 0:
          valid_combinations += 1
          total_possible_passwords += possible_passwords
      except KeyboardInterrupt:
        print()
        return total_possible_passwords / valid_combinations


if __name__ == "__main__":
  standard_password_module = Passwords(["about", "after", "again", "below", "could", "every", "first", "found", "great", "house", "large", "learn", "never", "other", "place", "plant", "point", "right", "small", "sound", "spell", "still", "study", "their", "there", "these", "thing", "think", "three", "water", "where", "which", "world", "would", "write"])
  print(standard_password_module.average_possible_passwords_given_columns(3))

"""
[Wrong] Given the first 3 columns of information, there are, on average, 3.47 possible passwords.

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
