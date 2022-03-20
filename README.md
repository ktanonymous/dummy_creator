# In the beginning

- I'm not good at English and development, so I apologize for my poor English and development.
- if you find or notice points to be improved, I would appreciate if you told me.
- You can't `pip install` now, so ,in the future, I want to applicable `pip install`.
- This generator is imperfect.

# dummy_creator

This is a dummy data generator.  
Unlike [faker](https://faker.readthedocs.io/en/master/) or [mimesis](https://mimesis.name/en/master/), this generates dummy data with parameters defined by you.

Now, you can define parameters with a json file, and output data will create in csv folder.

## How to use

1. Please clone this project.
1. In the script, import main function from dummy_creator/src/py/main.py
1. Call main function with defining `input_file`.
1. You will find dummy data in csv folder.

## Example of input file

Show very simple input file example below.

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

## Kinds of distribution

You can use distribution showed below.

- Normal probability distribution (Gauss distribution)
- Logarithmic normal distribution
- Uniform distribution
- Random choices with user-defined-weights
