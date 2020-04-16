#!/usr/bin/python

import math
from functools import reduce

# ================
#     Helpers
# ================

def pipe(*funcs):
  return lambda initialValue: reduce(lambda acc, func: func(acc), funcs, initialValue)

# returns the amount of batches that were made
def highest_shared_value(dict):
  return min(dict.values()) 

# create a dictionary from a list of tuples containing key-value pairs
def list_of_tuples_to_dict(xs):
  def reducer(_dict, _tuple):
    key, value = _tuple
    _dict[key] = value
    return _dict

  return reduce(reducer, xs, {})


# ================
#       Main
#=================

def recipe_batches(recipe, ingredients):
  def initialize_tally(recipe):
    ingredient, amount = recipe
    return (ingredient, 0)

  recipe_copy = recipe.copy()
  ingredients_copy = ingredients.copy()
  # tally = list_of_tuples_to_dict(list(map(initialize_tally, recipe.items())))
  # the below is the same as the above
  tally = pipe(
    lambda xs: map(initialize_tally, xs),
    list,
    list_of_tuples_to_dict
  )(recipe.items())
  
  def increment_tally(recipe, ingredients):
    if len(recipe.keys()) == 0:
      return highest_shared_value(tally)

    for k in recipe.keys():
      while ingredients[k] >= recipe[k]:
        tally[k] += 1
        ingredients[k] -= recipe[k]
      
    return highest_shared_value(tally)


  # if there are more ingredients required in the recipe than there are available ingredients, 
  # then 0 batches can be made
  if len(recipe.keys()) > len(ingredients.keys()):
    return 0
  # else, determine the total amount of batches
  else:
     return increment_tally(recipe_copy, ingredients_copy)

      

print("should be 1", recipe_batches( { 'milk': 100, 'butter': 50, 'flour': 5 },  { 'milk': 100, 'butter': 50, 'flour': 5 }))
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))