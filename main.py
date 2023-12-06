###### чтение файла ######

def read_recipes(file_name):
  recipes = {}
  with open(file_name, 'r', encoding='utf-8') as file:
      lines = file.readlines()
      i = 0
      while i < len(lines):
          recipe_name = lines[i].strip()
          i += 1
          num_ingredients = int(lines[i])
          i += 1
          ingredients = {}
          for j in range(num_ingredients):
              ingredient_info = lines[i].strip().split('|')
              ingredient_name = ingredient_info[0].strip()
              quantity = float(ingredient_info[1])
              unit = ingredient_info[2].strip()
              ingredients[ingredient_name] = {'quantity': quantity, 'unit': unit}
              i += 1
          recipes[recipe_name] = {'ingredients': ingredients, 'num_ingredients': num_ingredients}
          i += 1
  return recipes



