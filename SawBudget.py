import helpfulFunc as hf

def GetBudget(film_number, APIkey):
  film_number = '/movie/' + str(film_number) 
  return hf.make_tmdb_api_request(film_number, APIkey)['budget']

if __name__ == "__main__":
  APIkey = input('Input your API key: ')
  film_number = input('Input film id: ')
  print('Saw2 budget: $%d' % GetBudget(film_number, APIkey))

