"""
Author: Lee Taylor

This is a step in the process of analysing ChatGPT.

The purpose of this Python file is to convert the text/python output from
ChatGPT's GPT-3.5-S (S = 'speedy') model to usable Python code.
"""


# Read ChatGPT output
with open("GPT-3.5-S.txt", 'r') as f:
    string = f.read()

# Seperate different formats into elements in a list
chunks = string.split('---')

# Assign variable names to work with
word_dict_ = chunks[0]
_dict_ = chunks[1]

# # Check output
# for _ in word_dict_.split('word_dict = '):
#     print(_)

# Add Python dictionary formatting
word_dict_ = word_dict_.replace('word_dict = ', 'dict_.update(')
word_dict_ = word_dict_.replace('}', '})')

# Check result of operations
print(word_dict_)

# Perform similar opertations to convert the second format
_dict_ = _dict_.replace('{', 'dict_.update({')
_dict_ = _dict_.replace('}', '})')

# Check result of operations
print(_dict_)

# Form final Python file text content
gpt_py_ = word_dict_ + '\n' + _dict_

# Write converted output to .py file
with open('Formatted_GPT-3.5-S.py', 'w') as f:
    f.write(gpt_py_)

