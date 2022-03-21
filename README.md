# In the beginning

- I'm not good at English and development, so I apologize for my poor English and development.
- If you find or notice points to be improved, I would appreciate if you told me.
- This project hasn't uploaded to PyPI.
- This generator is imperfect.

# dummy_creator

This is a dummy data generator.  
Unlike [faker](https://faker.readthedocs.io/en/master/) or [mimesis](https://mimesis.name/en/master/), this generates dummy data with parameters defined by you.

Now, you can define parameters with a json file, and output data will create in csv folder.

## How to use

1. Please clone this project.(`$ git clone ~`)
1. In the project directory, use `pip install .` command.
1. You can use this generator with `from dummy_creator import create_dummy` script.
1. You will find dummy data in csv folder with this generator.

## Example

Show very simple input file example below.

input_file.json

```JSON:input_file.json
{
    "gender": {
        "number": 800,
        "label": {
            "1": "male",
            "2": "female"
        },
        "dist": "random",
        "weights": {
            "1": 6,
            "2": 4
        }
}
```

With this input file, you can create 800 dummy data of gender in the ratio of 6:4.  
If you want to use this input file, for example, write script like below.

example.py

```Python: example.py
from dummy_creator import create_dummy

input_file = 'input_file.json'
create_dummy(input_file=input_file.json)
```

Dummy data will be created like below.

```
csv
  ┗ gender.csv
```

## Kinds of distribution

Now, you can use distribution showed below.

- Normal probability distribution (Gauss distribution)
- Logarithmic normal distribution
- Uniform distribution
- Random choices with user-defined-weights
