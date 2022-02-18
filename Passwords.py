class Passwords:
  def __init__(self, password_options):
    self.password_options = password_options
    self.password_length = max(map(len, self.password_options))
  
  def letter_options_by_column(self):
    letter_options = []
    for column_number in range(self.password_length):
      options = set()
      for password in self.password_options:
        options.add(password[column_number])
      letter_options.append(sorted(options))
    return letter_options


if __name__ == "__main__":
  standard_password_module = Passwords(["about", "after", "again", "below", "could", "every", "first", "found", "great", "house", "large", "learn", "never", "other", "place", "plant", "point", "right", "small", "sound", "spell", "still", "study", "their", "there", "these", "thing", "think", "three", "water", "where", "which", "world", "would", "write"])
  letter_options = standard_password_module.letter_options_by_column()
  most_options = max(map(len, letter_options))
  for row in range(most_options):
    for column in range(len(letter_options)):
      try:
        print(letter_options[column][row], end='  ')
      except IndexError:
        print(' ', end='  ')
    print()
    
