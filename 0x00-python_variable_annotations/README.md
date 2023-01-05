# Python Variable Annotation

This project tries to complete type-annotation of python variables in Python3

## Completed Tasks
- [Basic annotations - add](https://github.com/getdaniel/alx-backend-python/blob/main/0x00-python_variable_annotations/0-add.py)
a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.
- [Basic annotations - concat](https://github.com/getdaniel/alx-backend-python/blob/main/0x00-python_variable_annotations/1-concat.py)
a type-annotated function concat that takes a string str1 and a string str2 as arguments and returns a concatenated string.
- [Basic annotations - floor](https://github.com/getdaniel/alx-backend-python/blob/main/0x00-python_variable_annotations/2-floor.py)
a type-annotated function floor which takes a float n as argument and returns the floor of the float.
- [Basic annotations - to string](https://github.com/getdaniel/alx-backend-python/blob/main/0x00-python_variable_annotations/3-to_str.py)
a type-annotated function to_str that takes a float n as argument and returns the string representation of the float.
- [Define variables](https://github.com/getdaniel/alx-backend-python/blob/main/0x00-python_variable_annotations/4-define_variables.py)
a script that define and annotate the following variables with the specified values: <br/>

-- a, an integer with a value of 1.<br/>
-- pi, a float with a value of 3.14.<br/>
-- i_understand_annotations, a boolean with a value of True.<br/>
-- school, a string with a value of “Holberton”.<br/>
- [Complex types - list of floats](https://github.com/getdaniel/alx-backend-python/blob/main/0x00-python_variable_annotations/5-sum_list.py)
a type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.
- [Complex types - mixed list](https://github.com/getdaniel/alx-backend-python/blob/main/0x00-python_variable_annotations/6-sum_mixed_list.py)
a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.
- [Complex types - string and int/float to tuple](https://github.com/getdaniel/alx-backend-python/blob/main/0x00-python_variable_annotations/7-to_kv.py)
a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.
- [Complex types - functions](https://github.com/getdaniel/alx-backend-python/blob/main/0x00-python_variable_annotations/8-make_multiplier.py)
a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.
- [Le's duck type an iterable object](https://github.com/getdaniel/alx-backend-python/blob/main/0x00-python_variable_annotations/9-element_length.py)
contains an annotation of the function's (shown below) parameters and return values with the appropriate types.
```
def element_length(lst):
  return [(i, len(i)) for i in lst]
```
- [Duck typing - first element of a sequence](https://github.com/getdaniel/alx-backend-python/blob/main/0x00-python_variable_annotations/100-safe_first_element.py)
contains an augmentation of the following code with the correct duck-typed annotations:
```
# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
```
- [More involved type annotations](https://github.com/getdaniel/alx-backend-python/blob/main/0x00-python_variable_annotations/101-safely_get_value.py)
contains a script that includes the code below with type annotations added to it.

```
def safely_get_value(dct, key, default = None):
  if key in dct:
      return dct[key]
  else:
      return default
```
- [Type checking](https://github.com/getdaniel/alx-backend-python/blob/main/0x00-python_variable_annotations/102-type_checking.py)
contains the code below and uses mypy to validate it and apply any necessary changes.

```
def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
  zoomed_in: Tuple = [
      item for item in lst
      for i in range(factor)
  ]
  return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
```
