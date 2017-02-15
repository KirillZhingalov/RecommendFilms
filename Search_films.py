import helpfulFunc as hf
import os.path
import json

def check_exist_db(file_with_db):
  if not os.path.exists(file_with_db): 
    return False
  return True

def user_db():
  ans = input('Standart db file not found. Do you want use your bd?(y/n)')
  if ans == 'yes' or ans == 'y':
    users_db_file = input('Input file name: ')
    return users_db_file
  else:
    return False

def load_from_db(file_with_db):
  with open(file_with_db) as file:
    return json.load(file)

def search_film(movies_list, word):
  finded_films = list()
  for film in movies_list:
    if word.upper() in film['title'].upper():
      finded_films.append(film['title'])
  return finded_films

if __name__ == "__main__":
  file_with_db = "FilmsDB"
  if not check_exist_db(file_with_db):
    file_with_db = user_db()
    if not file_with_db:
      print('You can create data base file with command "python MakeDB.py"')

  movies_list = load_from_db(file_with_db)
  word = input('Input word: ')
  print('Films with your word in title:')
  for film in search_film(movies_list, word):
    print(film)

