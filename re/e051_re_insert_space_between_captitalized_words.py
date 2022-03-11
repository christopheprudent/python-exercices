# web solution
import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

def insert_space_between_capitalized_words(text):
    return re.sub(r"([A-Z])([a-z0-9]+)", r" \1\2", text)[1:]

print('dev) ' + insert_space_between_capitalized_words("Python"))
print('web) ' + capital_words_spaces("Python"))
print('dev) ' + insert_space_between_capitalized_words("PythonExercises"))
print('web) ' + capital_words_spaces("PythonExercises"))
print('dev) ' + insert_space_between_capitalized_words("PythonExercisesPracticeSolution"))
print('web) ' + capital_words_spaces("PythonExercisesPracticeSolution"))
