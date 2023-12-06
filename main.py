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

file_name = 'recipes.txt'
recipes = read_recipes(file_name)

for recipe_name, recipe_info in recipes.items():
  num_ingredients = recipe_info['num_ingredients']
  ingredients = recipe_info['ingredients']
  print(f"\n{recipe_name}:")
  print(f"Количество ингредиентов: {num_ingredients}")
  for ingredient, info in ingredients.items():
      print(f"- {ingredient}: {info['quantity']} {info['unit']}")

############### Задача№1 ################

def read_recipes(file_name):
  cook_book = {}
  with open(file_name, 'r', encoding='utf-8') as file:
      lines = file.readlines()
      i = 0
      while i < len(lines):
          recipe_name = lines[i].strip()
          i += 1
          num_ingredients = int(lines[i])
          i += 1
          ingredients = []
          for j in range(num_ingredients):
              ingredient_info = lines[i].strip().split('|')
              ingredient_name = ingredient_info[0].strip()
              quantity = float(ingredient_info[1])
              measure = ingredient_info[2].strip()
              ingredients.append({
                  'ingredient_name': ingredient_name,
                  'quantity': quantity,
                  'measure': measure
              })
              i += 1
          cook_book[recipe_name] = ingredients
          i += 1
  return cook_book

cook_book = read_recipes(file_name)

print(cook_book)

################## Задача №2 #######################

def get_shop_list_by_dishes(dishes, person_count, cook_book):
  shop_list = {}
  for dish in dishes:
      if dish in cook_book:
          for ingredient in cook_book[dish]:
              ingredient_name = ingredient['ingredient_name']
              quantity = ingredient['quantity'] * person_count
              measure = ingredient['measure']
              if ingredient_name not in shop_list:
                  shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
              else:
                  shop_list[ingredient_name]['quantity'] += quantity
      else:
          print(f"Блюдо '{dish}' отсутствует в кулинарной книге.")
  return shop_list

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)

print(shop_list)
