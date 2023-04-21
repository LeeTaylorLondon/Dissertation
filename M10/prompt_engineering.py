""" Author: Lee Taylor """


prompt = \
    f"Write one list full of synonyms and antonyms for my target word 'Accessible', ordered by closest semantic " \
    f"meaning to my target word starting with synonyms. " + \
    "Write this information in a python dictionary, {my_target_word: one python list of synonyms with antonyms}\n\n"

with open('Accessible.txt', 'r') as f:
    lines = f.readlines()

replace = 'Accessible'
prompts = []
for tgt_word in lines:
    prompts.append(prompt.replace(replace, tgt_word.strip()))

with open('prompts.txt', 'w') as f:
    f.writelines(prompts)
