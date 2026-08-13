# REST

- representation state transfer
- design pattern to make the data available to the client applications
- request response pattern
- client sends request containing
  - header: key-value pairs
  - body: data need to send to the server
- server receives the request, executes it and send the response containing
  - header: key-value pairs
  - body: data needs to send the to client
- http methods:
  - will be set by the client while sending the request
  - used to provide the intention of sending the request
  - GET: used to get data from the server
  - POST: send the data to the server
  - PUT: update the entire data on the server
  - DELETE: delete the requested data on the server
  - PATCH: update partial data on the server
- http response status code
  - 1xx: debugging the web server
  - 2xx: success
  - 3xx: redirection
  - 4xx: client error
  - 5xx: server error
- e.g.
  - get list of products
    - GET http://myapp.com/product
  - create a new product
    - POST http://myapp.com/product
    - body: {"title": "product1", "price": 100}
  - update existing product
    - PUT http://myapp.com/product/1
    - body: {"title": "product1", "price": 300}
  - delete existing product
    - DELETE http://myapp.com/product/1

# Flask

- python package used to develop the REST Server
- installation
  - pip install flask
- terminologies
  - route: mapping between the http method, path and handler function
