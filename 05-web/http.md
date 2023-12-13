# HTTP

HyperText Transfer Protocol (***HTTP***) is the most common protocol used to transfer data over the web. It defines how messages are formatted and transmitted, and what actions web servers and browsers should take in response to various commands.

## HTTP Request

In it's most basic form, an HTTP request is just the following text:

```http
GET / HTTP/1.1
Host: www.example.com
```

Which means, that the client want's to make a request to the server, to ***get*** the root document (`/`) of the website `www.example.com`.

### Request Headers

Everything else below this line is called the ***HTTP Header***. It contains additional information about the request, like the host, the user agent, the accepted languages, etc. For example:

```http
GET / HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
```

### Request Body

The request headers may be followed with an empty line, then extra data which is called the ***request body***. For example, when you submit a form, the data you enter is sent in the request body. For example:

```http
POST / HTTP/1.1
Host: www.example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 13

say=Hi&to=Mom
```

This data may include form data, or files, or any other data you want to send to the server.

### Request Methods

Notice that in the previous example, we stopped using the `GET` method, and started using the `POST` method. This is because the `GET` method is used to retrieve data from the server, while the `POST` method is used to send data to the server. There are other methods as well, like:

| Method | Description |
| ------ | ----------- |
| `GET` | Retrieve data from the server |
| `POST` | Send data to the server |
| `PUT` | Send data to the server, and replace the existing data |
| `DELETE` | Delete data from the server |
| `HEAD` | Retrieve only the headers of a resource |

None of them are used as much as `GET` and `POST` though, and any server can select how it responds to each method.

## HTTP Response

After a request is made, the server responds with an HTTP response. It's structure is similar to the request, but it contains different information.

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 13

Hello, World!
```

### Status Codes

The number `200` in the previous example is the ***status code***. It indicates that the request was successful. The word "OK" after it is a text description of it. There are many other status codes, the most common ones are:

| Code | Description |
| ---- | ----------- |
| `200` | OK |
| `301` | Moved Permanently |
| `400` | Bad Request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Not Found |
| `500` | Internal Server Error |
| `503` | Service Unavailable |

### Response Headers & Body

Like the request, the response may contain headers as well. For example:

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 13
Date: Sat, 26 May 2012 16:04:12 GMT
Expires: -1
Cache-Control: private, max-age=0

Hello, World!
```

In this case, everything after the first line, up until the empty line, is the response headers. The response body is everything after that empty line. The body can be HTML, JSON, XML, a file, or anything else, and the headers are always key-value pairs.
