# FastAPI Movies API

This is a Python 3 FastAPI-based API that allows users to retrieve and create movie data. The API provides endpoints for listing existing movies and creating new ones.

 
Installation

Clone this repository:
```bash
    git clone https://github.com/example/repo.git
```

Install the required dependencies using pip:
```bash
    pip install -r requirements.txt
```
  

Run the application:
```bash
    uvicorn main:app --reload
```
## Usage

  

**Listing Movies**

To retrieve a list of all movies, send a GET request to the following endpoint:

    http://localhost:8000/movies/

  

The response will contain a JSON object with an array of movie objects. Each movie object will contain the following attributes:

  

 - **id**: the unique identifier of the movie
 - **title**: the title of the movie
 - **overview**: the name of the movie's director
 - **year**: the year the movie was released
 - **rating**: the rating of the movie (out of 10)

### Creating Movies

To create a new movie, send a POST request to the following endpoint:

 - http://localhost:8000/movies/

The request body should be a JSON object with the following attributes:



Example

Here is an example of how to use the API to create a new movie:

Send a POST request to http://localhost:8000/movies/ with the following request body:
```json
    {
    
    "title": "The Shawshank Redemption",
    
    "director": "Frank Darabont",
    
    "year": 1994,
    
    "rating": 9.3
    
    }
```

The API will respond with a JSON object containing the newly created movie:
