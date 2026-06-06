from index import app

def run_tests():
    client = app.test_client()

    resp = client.get('/add?i=2&j=3')
    print('GET /add?i=2&j=3 ->', resp.status_code, resp.get_json())

    resp2 = client.post('/add', json={'i':7, 'j':8})
    print('POST /add ->', resp2.status_code, resp2.get_json())

    # error case
    resp3 = client.post('/add', json={'i':'x', 'j':5})
    print('POST /add (invalid) ->', resp3.status_code, resp3.get_json())

if __name__ == '__main__':
    run_tests()
