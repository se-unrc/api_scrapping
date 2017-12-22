

## ToDo
* Write an API spec based in [OAS](https://github.com/OAI/OpenAPI-Specification)

* Write the real API using the above specification (maybe using sinatra? or check links section where is a codegen?)

* Then expose the API

* Write a scrapper that given the API OAS specification hit the API to build a progresive state chart that represent the available calls from a client point of view. A first approach of scrapping could be:

  + Take all endpoints from API OAS and hit them using curl passing the corresponding parameters
    - Then take the answer and inspect the response code, then build states reachable from initial state if response code is 200ok and states unreachable from initial state if response code is different than 200ok.

## Usage

Get an specification from `oas` directory and generate the client and server using the following commands

```bash
$ swagger-codegen generate -i oas/minimal_pet_store.yaml -l ruby -o tmp/client
```

and then generate the server with the following command
```bash
$ swagger-codegen generate -i oas/minimal_pet_store.yaml -l sinatra -o tmp/server
```

start the server

```bash
$ rackup -p 4567 config.ru
```

## Links
- [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification)
- [Swagger Specifications](https://swagger.io/specification/)
- [Swagger CodeGen](https://github.com/swagger-api/swagger-codegen)
- [Codegen](https://github.com/capitalone/oas-nodegen)
