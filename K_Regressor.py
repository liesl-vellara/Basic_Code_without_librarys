def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def predict(unknown, dataset, movie_ratings, k):
  distances = []
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]
  # creating a variable called numerator to get the sum of the fraction of each rating divided by its respective distance
  numerator = 0
  # creating a variable that will have the sum of all the fraction of one divided by each movie distance
  denominator = 0
  for neighbor in neighbors:
    title = neighbor[1]
    numerator += movie_ratings[title]/neighbor[0]
    denominator += 1/neighbor[0]
  return numerator/denominator
