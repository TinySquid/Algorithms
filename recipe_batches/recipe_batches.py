import math


def recipe_batches(recipe, ingredients):
    """
    recipe - [dict] - keys are ingredients, values are quantites 
    ingredients - [dict] - keys are ingredients, values are quantites 

    - Make sure the ingredients match the recipe, otherwise no batch can be made
    - Loop through ingredients and get batch count via comparison to recipe key value
        - Maintain max count of batches during loop
    - return max batch count 
    """

    # Missing ingredient case
    if len(recipe) != len(ingredients):
        return 0

    max_batch = float("inf")

    for key in ingredients.keys():
        batches = ingredients[key] // recipe[key]
        max_batch = batches if batches < max_batch else max_batch

    return max_batch


if __name__ == "__main__":
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {"milk": 100, "butter": 50, "flour": 5}
    ingredients = {"milk": 132, "butter": 48, "flour": 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}.".format(
            batches=recipe_batches(recipe, ingredients), ingredients=ingredients
        )
    )

