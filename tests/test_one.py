
class TestOne:
    def test_one(self):
        print("Hello World!")
        assert 1 == 1


    def test_that_file_data_is_correct(self):
        with open("testdata/hello.txt") as f:
            data = f.read()
            assert data == "Hello World!"