import requests

# Определяем API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# GET запрос к API endpoint
response = requests.get(url)

# Убеждаемся, что API вернул статус код 200
assert response.status_code == 200, f"Expected status code 200 but received {response.status_code}"

# Убеджаемся, что данные ответа представлены в формате JSON
assert response.headers['Content-Type'].startswith("application/json"), f"Expected Content-Type to start with 'application/json' but received '{response.headers['Content-Type']}'"

# Преобразование данных ответа в словарь Python
data = response.json()

# Убеждаемся,что ответ содержит данные
assert len(data) > 0, "Response data is empty"

# Доступ к определенному элементу в данных ответа
first_post = data[0]

# Убеждаемся, что первый пост имеет ожидаемые свойства
assert 'id' in first_post, "Missing 'id' property in first post"
assert 'title' in first_post, "Missing 'title' property in first post"
assert 'body' in first_post, "Missing 'body' property in first post"

# Убеждаемся, что первая запись имеет непустые значения для необходимых свойств.
assert first_post['id'] is not None and first_post['id'] != "", "Value for 'id' property in first post is empty"
assert first_post['title'] is not None and first_post['title'] != "", "Value for 'title' property in first post is empty"
assert first_post['body'] is not None and first_post['body'] != "", "Value for 'body' property in first post is empty"

# Убеждаемся, что первый пост имеет ожидаемое количество комментариев
if 'comments' in first_post:
    assert len(first_post['comments']) == 5, f"Expected 5 comments but received {len(first_post['comments'])}"
else:
    print("Missing 'comments' property in first post")
