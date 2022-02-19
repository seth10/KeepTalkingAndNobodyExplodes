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


if __name__ == "__main__":
  standard_password_module = Passwords(["about", "after", "again", "below", "could", "every", "first", "found", "great", "house", "large", "learn", "never", "other", "place", "plant", "point", "right", "small", "sound", "spell", "still", "study", "their", "there", "these", "thing", "think", "three", "water", "where", "which", "world", "would", "write"])
  letter_counts = standard_password_module.letter_frequencies_by_column()
  for row in itertools.zip_longest(*letter_counts, fillvalue='  '):
    print('  '.join(row))
   
"""
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
 
