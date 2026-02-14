import requests

base_url = "https://jsonplaceholder.typicode.com"

class TestOne:
    def test_one(self):
        print("Hello World!")
        assert 1 == 1


    def test_that_file_data_is_correct(self):
        with open("testdata/hello.txt") as f:
            data = f.read()
            assert data == "Hello World!"


    def test_get_posts(self):
        response = requests.get(base_url + "/posts/87")
        assert response.status_code == 200

        data = response.json()
        assert data["id"] ==87
        assert "title" in data 


    def test_get_all_posts(self):
        response = requests.get(base_url + "/posts")
        assert response.status_code == 200

        posts = response.json()
        assert len(posts) == 100