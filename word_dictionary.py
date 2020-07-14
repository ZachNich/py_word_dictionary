"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict({
    "joy": "happiness",
    "despair": "massive upset",
    "annoyance": "dealing with settings feeling"
})

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

word_definitions["gratitude"] = "the feeling associated with Joe"
word_definitions["grating"] = "the feeling associated with VSCode errors"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["joy"], word_definitions["despair"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (word, definition) in word_definitions.items():
    print(f'The definition of {word} is {definition}')