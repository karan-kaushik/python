# Dictionary Comprehension

## Simple from List
new_dict = {k:v for item in list}

## Simple from dict
new_dict = {k:v for (k,v) in dict.items()}

## With conditions
new_dict = {k:v for (k,v) in dict.items() if test}
