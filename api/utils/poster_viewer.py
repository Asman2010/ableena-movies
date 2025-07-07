# from tmdbv3api import TMDb, Movie

# # Initialize TMDb and set your API key
# tmdb = TMDb()
# tmdb.api_key = "dcfd3635a5fa66531d0ed5a71edeb322"  # Replace with your TMDb API key

# movie = Movie()
# movie_name = "Jailer"  # Replace with any movie name you want

# # Search for the movie
# results = movie.search(movie_name, language="ta-IN")

# if results:
#     first_result = results[0]
#     print("Title:", first_result.title)
#     print("Overview:", first_result.overview)
#     print("Poster path:", first_result.poster_path)
#     # Build the full poster URL
#     poster_url = f"https://image.tmdb.org/t/p/w500{first_result.poster_path}"
#     print("Poster URL:", poster_url)
# else:
#     print("Movie not found.")


import requests

api_key = "dcfd3635a5fa66531d0ed5a71edeb322"
movie_name = "Jailer"
url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}&language=ta-IN"

response = requests.get(url)
data = response.json()
print(data)
