import helpfulFunc as hf
import json
import os.path

MOVIES_COUNT = 1000
FILE_WITH_DB = 'FilmsDB'

def make_movie_dict(movie_id, APIkey):
  movie_dict = dict()
  movie_dict.update(hf.make_tmdb_api_request('/movie/'+str(movie_id), APIkey))
  return movie_dict

def add_keywords(movie_dict, movie_id, APIkey):
  movie_dict.update({'keywords': list()})
  keywords = hf.make_tmdb_api_request('/movie/'+str(movie_id)+'/keywords',
                                      APIkey)
  for word in keywords['keywords']:
    movie_dict['keywords'].append(word['name'])
  return movie_dict

def make_movies_list(APIkey):
  movies_list = list()
  num_movie = 0 
  suc_load = 0
  while suc_load <= MOVIES_COUNT:
    try:
      movie_dict = make_movie_dict(num_movie, APIkey) 
      movie_dict = add_keywords(movie_dict, num_movie, APIkey)    
      movies_list.append(movie_dict)
      suc_load += 1
    except:
      pass
      #print("No movie with id %d" % num_movie)
    num_movie += 1
  return movies_list


def list_to_json(movies_list):
  with open(FILE_WITH_DB, 'w') as file:
    json.dump(movies_list, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
  APIkey = input('Input you API key: ')
  while len(APIkey) != 32:
    APIkey = input('Wrong API key. Repeat: ')
 
  if os.path.exists(FILE_WITH_DB):
    print('Database already exist')
  else:
    print('Downloading films info...')  
    list_to_json(make_movies_list(APIkey))
    print('Database with films writen to %s' % FILE_WITH_DB)
