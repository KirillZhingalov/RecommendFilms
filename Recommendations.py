import Search_films as sf

def get_users_film(movies_list, users_request):
  for film in movies_list:
    if film['title'] == users_request:
      return film

def get_important_details(movie_dict):
  movie_details = dict({'title':movie_dict['title'], 'keywords':set(), 'genres':set()})
  for keyword in movie_dict['keywords']:
    movie_details['keywords'].add(keyword)
  for genre in movie_dict['genres']:
    movie_details['genres'].add(genre['name'])
  return movie_details

def is_films_common(users_movie_dict, other_movie_dict):
  if users_movie_dict['keywords'] & other_movie_dict['keywords'] and \
     users_movie_dict['genres'] & other_movie_dict['genres']:
    return True
  return False

def make_recommend_list(movies_list, users_film):
  recommend_list = list()
  users_film = get_important_details(users_film)
  for film in movies_list:
    film = get_important_details(film)
    if is_films_common(users_film, film):
      recommend_list.append(film['title'])
  return recommend_list

if __name__ == "__main__":
  file_with_db = "FilmsDB"
  if not sf.check_exist_db(file_with_db):
    file_with_db = sf.user_db()
    if not file_with_db:
      print('You can create data base file with command "python MakeDB.py"')
  
  movies_list = sf.load_from_db(file_with_db)
  film = input('Input film name: ')
  users_film = get_users_film(movies_list, film)
  print("Maybe you'll like:")
  for film in make_recommend_list(movies_list, users_film):
    print(film)

