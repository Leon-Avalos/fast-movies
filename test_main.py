import unittest2
from fastapi.testclient import TestClient
from main import app


class TestMoviesAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Blyat', response.content)

    def test_get_all_movies(self):
        response = self.client.get('/movies')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), movies)

    def test_get_movie_by_id(self):
        response = self.client.get('/movies/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), movies[0])

    def test_get_movie_by_invalid_id(self):
        response = self.client.get('/movies/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_get_movies_by_category(self):
        response = self.client.get('/movies/?category=Acción&year=2009')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), ['Acción', '2009'])
