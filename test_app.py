
# testing app
import app # import app.py

def test_index():
    # create a test client
    tester = app.app.test_client()
    # use the test client to make a request to '/'
    response = tester.get('/', content_type='html/text')
    # compare the response data to expected result
    assert response.status_code == 200
    assert response.data == b'<h1> Hello World Danford</h1>'