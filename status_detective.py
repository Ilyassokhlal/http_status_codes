import requests

def api_caller(url, method, new_post=None):
    """Makes the api call and returns a status report"""
    # Method seperator
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, json=new_post)
    elif method == 'DELETE':
        response = requests.delete(url)
    else:
        print(f"\n{method} is an invalid method! Please try again! Choose: GET, POST or DELETE")

    # Status code seperator

    if response.status_code == 200:
        print(f"\n{method} {url}")
        print(f"Status: {response.status_code} (Success)")
        print(f"Description: Request succeeded - resource returned")
        return response.json()
    elif response.status_code == 201:
        print(f"\n{method} {url}")
        print(f"Status: {response.status_code}", f"(Success)")
        print(f"Description: Request succeeded - resource created")
        return response.json()
    elif response.status_code == 404:
        print(f"\n{method} {url}")
        print(f"Status: {response.status_code} (Client Error)")
        print(f"Description: Resource not found: {url}")
        return None
    else:
        print(f"\nError {response.status_code}: {response.reason}")
        return None
    

# Task 1: GET /posts/1

api_caller("https://jsonplaceholder.typicode.com/posts/1", "GET")

# Task 2: GET /posts/99999

api_caller("https://jsonplaceholder.typicode.com/posts/99999", "GET")

# Task 3: POST /posts

new_post = {
    "title": "Test Title",
    "body": "Test Body",
    "userId": 1
}
api_caller("https://jsonplaceholder.typicode.com/posts", "POST", new_post=new_post)

# Task 4: DELETE /posts/1

api_caller("https://jsonplaceholder.typicode.com/posts/1", "DELETE")

# Task 5: GET /invalidendpoint

api_caller("https://jsonplaceholder.typicode.com/invalidendpoint", "GET")

# Task 6: GET /users/1/todos

api_caller("https://jsonplaceholder.typicode.com/users/1/todos", "GET")