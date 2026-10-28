# Phase 12: Networking — Notes

### Beginner Introduction
**Client–server model** — a *client* (your Python program) sends a **request** to a *server*, which sends back a **response**. Most web communication works this way, using the **HTTP** protocol.

**Parts of a request**
- **URL** — the address of the resource (`https://api.example.com/users`).
- **Method** — the action to perform (`GET`, `POST`, ...).
- **Headers** — extra information (content type, authentication).
- **Body** — data sent to the server (mainly for `POST`/`PUT`/`PATCH`).

**HTTP status code groups**
```
1xx  informational
2xx  success          (200 OK, 201 Created, 204 No Content)
3xx  redirection      (301 Moved Permanently, 304 Not Modified)
4xx  client error     (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests)
5xx  server error     (500 Internal Server Error, 503 Service Unavailable)
```

### HTTP Requests (`requests`)
A third-party library that makes sending HTTP requests simple. Not built in, so install it first.
```bash
pip install requests
```
```python
import requests

response = requests.get(url)
response = requests.post(url, json=data)
response = requests.put(url, json=data)
response = requests.patch(url, json=data)
response = requests.delete(url)
```
**Common request options**
```python
requests.get(
    url,
    params={"key": "value"},        # query string  (?key=value)
    headers={"Header": "value"},    # custom headers
    json=data,                      # send a dict as JSON body
    data=form_data,                 # send form-encoded data
    timeout=5,                      # seconds (always set one)
)
```
**Response object**
```python
response.status_code        # e.g. 200
response.ok                 # True if status < 400
response.text               # body as string
response.json()             # body parsed as JSON -> dict/list
response.content            # body as bytes
response.headers            # response headers
response.url                # final URL
response.raise_for_status() # raises HTTPError for 4xx/5xx
```
**Sessions** — reuse a connection, headers, and cookies across requests.
```python
with requests.Session() as session:
    session.headers.update({"Header": "value"})
    response = session.get(url)
```
**Error handling**
```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except requests.exceptions.Timeout:
    ...
except requests.exceptions.HTTPError:
    ...
except requests.exceptions.RequestException:   # base class for all requests errors
    ...
```

### REST APIs
**REST (Representational State Transfer)** — a style of designing web APIs where data is treated as *resources* identified by URLs, and standard HTTP methods are used to act on them. Requests are **stateless**: each one carries everything the server needs.

| HTTP Method | Action (CRUD) | Typical URL | Description |
|---|---|---|---|
| `GET` | Read | `/users`, `/users/1` | Fetch a list or a single item |
| `POST` | Create | `/users` | Create a new item |
| `PUT` | Update (replace) | `/users/1` | Replace an entire item |
| `PATCH` | Update (partial) | `/users/1` | Modify part of an item |
| `DELETE` | Delete | `/users/1` | Remove an item |

```python
requests.get("https://api.example.com/users")
requests.get("https://api.example.com/users/1")
requests.post("https://api.example.com/users", json={"name": "..."})
requests.delete("https://api.example.com/users/1")
```
**Pagination** — large results are split into pages.
```python
requests.get(url, params={"page": 2, "limit": 50})
```

### JSON APIs
APIs that send and receive data in **JSON** format, the most common format for web APIs.
```python
# receiving JSON
data = response.json()                # parsed to dict/list
data["key"]

# sending JSON (sets Content-Type: application/json automatically)
requests.post(url, json={"key": "value"})

# manual conversion (if needed)
import json
json.dumps(obj)
json.loads(response.text)
```
**Safe handling**
```python
try:
    data = response.json()
except requests.exceptions.JSONDecodeError:
    ...                               # response wasn't valid JSON
```

### Authentication
Proving to the server who you are, so it can decide what you're allowed to access.

**API key** — a secret string sent in a header or query parameter.
```python
requests.get(url, headers={"X-API-Key": api_key})
requests.get(url, params={"api_key": api_key})
```
**Basic auth** — username and password sent with the request.
```python
requests.get(url, auth=("username", "password"))
```
**Bearer token (JWT / OAuth access token)** — a token sent in the `Authorization` header.
```python
requests.get(url, headers={"Authorization": f"Bearer {token}"})
```
**OAuth 2.0 (overview)** — a standard where the user grants your app limited access, and the server issues an *access token* (often short-lived) plus a *refresh token* to get new ones.
```
1. Redirect user to provider to log in and approve access
2. Receive an authorization code
3. Exchange the code for an access token
4. Send the token with requests (Authorization: Bearer ...)
5. Use the refresh token when the access token expires
```
**Session / cookie auth** — log in once, the server sets a cookie, and the `Session` object resends it.
```python
session = requests.Session()
session.post(login_url, data=credentials)
session.get(protected_url)
```
**Security tips**
```python
# keep secrets out of code; load from environment variables
import os
api_key = os.environ.get("API_KEY")
```

### WebSockets (Basic)
A protocol that keeps a **persistent, two-way connection** open between client and server, so either side can send messages at any time. Unlike HTTP (request → response → close), it's ideal for real-time features like chat, live notifications, and streaming data. URLs start with `ws://` or `wss://` (secure).

```bash
pip install websockets
```
**Client**
```python
import asyncio
import websockets

async def client():
    async with websockets.connect("ws://host:port") as websocket:
        await websocket.send("message")
        reply = await websocket.recv()

        # keep receiving messages
        async for message in websocket:
            ...

asyncio.run(client())
```
**Server**
```python
import asyncio
import websockets

async def handler(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(handler, "host", port):
        await asyncio.Future()           # run forever

asyncio.run(main())
```
**HTTP vs WebSocket**
```
HTTP        client asks -> server answers -> connection closes
WebSocket   connection stays open -> both sides send anytime
```