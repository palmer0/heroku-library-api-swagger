var spec =

  {
    "swagger": "2.0",
    "info": {
      "description": "This is a sample Library API. You can register as many authors and books as you want.",
      "version": "1.0.0",
      "title": "Library API",
      "contact": {
        "url": "https://github.com/jesuscg",
        "name": "Jesús Castillo"
      },
      "license": {
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
      }
    },
    "basePath": "/api/v1",
    "schemes": [
      "http"
    ],
    "tags": [
        {
            "name": "Authors",
            "description": "Operations about authors"
        },
        {
            "name": "Books",
            "description": "Management of registered books"
        }
    ],
    "consumes": [
      "application/json"
    ],
    "produces": [
      "application/json"
    ],
    "paths": {
      "/authors": {
        "get": {
          "summary": "List all authors",
          "operationId": "listAuthors",
          "tags": [
            "Authors"
          ],
          "responses": {
            "200": {
              "description": "Return a list of all authors.",
              "schema": {
                "$ref": "#/definitions/Authors"
              }
            }
          },
          "deprecated": false
        },
        "post": {
          "summary": "Creates an author",
          "description": "This endpoint creates an author with supplied first name and last name",
          "operationId": "createAuthor",
          "tags": [
            "Authors"
          ],
          "parameters": [
            {
              "name": "body",
              "in": "body",
              "required": true,
              "description": "Author model to create an author",
              "schema": {
                "$ref": "#/definitions/NewAuthor"
              }
            }
          ],
          "responses": {
            "201": {
              "description": "Returns the author object created.",
              "schema": {
                "$ref": "#/definitions/Author"
              }
            },
            "400": {
              "description": "Bad Request"
            }
          },
          "deprecated": false
        }
      },
      "/authors/{id}": {
        "get": {
          "summary": "Info for a specific author",
          "operationId": "showAuthorById",
          "tags": [
            "Authors"
          ],
          "parameters": [
            {
              "name": "id",
              "in": "path",
              "required": true,
              "description": "The id of the author to retrieve",
              "type": "string"
            }
          ],
          "responses": {
            "200": {
              "description": "Returns an author info",
              "schema": {
                "$ref": "#/definitions/Authors"
              }
            },
            "404": {
              "description": "Not Found"
            }
          },
          "deprecated": false
        },
        "delete": {
          "summary": "Deletes a specific author",
          "description": "Deletes a specific author",
          "operationId": "deleteAuthorById",
          "tags": [
            "Authors"
          ],
          "parameters": [
            {
              "name": "id",
              "in": "path",
              "required": true,
              "description": "The id of the author to delete",
              "type": "string"
            }
          ],
          "responses": {
            "204": {
              "description": "No Content"
            },
            "404": {
              "description": "Not Found"
            }
          },
          "deprecated": false
        },
        "put": {
         "summary": "Updates a specific author",
         "description": "Updates a specific author info",
         "operationId": "updateAuthorById",
         "tags": [
           "Authors"
         ],
         "parameters": [
           {
             "name": "id",
             "in": "path",
             "required": true,
             "description": "Author id to update info",
             "type": "string"
           },
           {
             "name": "body",
             "in": "body",
             "required": true,
             "description": "Author object to update info",
             "schema": {
              "$ref": "#/definitions/NewAuthor"
            }
           }
         ],
         "responses": {
           "200": {
             "description": "OK"
           },
           "400": {
             "description": "Bad Request"
           },
           "404": {
             "description": "Not Found"
           }
         },
         "deprecated": false
       }
      },
      "/books": {
      "get": {
        "summary": "List all books",
        "operationId": "listBooks",
        "tags": [
          "Books"
        ],
        "responses": {
            "200": {
              "description": "Return a list of all books.",
              "schema": {
                "$ref": "#/definitions/Books"
              }
            }
          },
        "deprecated": false
        },
        "post": {
          "summary": "Creates a book",
          "description": "Creates a book.",
          "operationId": "createBooks",
          "tags": [
            "Books"
          ],
          "parameters": [
            {
              "name": "body",
              "in": "body",
              "required": true,
              "description": "Book model to create a book",
              "schema": {
                "$ref": "#/definitions/NewBook"
              }
            }
          ],
          "responses": {
            "201": {
              "description": "Returns the book object created.",
              "schema": {
                "$ref": "#/definitions/Book"
              }
            },
            "400": {
              "description": "Bad Request"
            },
            "404": {
              "description": "Not Found"
            }
          },
          "deprecated": false
        }
     },
    "/books/createBookAndAuthor": {
         "post": {
           "summary": "Creates a book with a new author",
           "description": "Creates a book and an author.",
           "operationId": "createBookAndAuthor",
           "tags": [
             "Books"
           ],
           "parameters": [
             {
               "name": "body",
               "in": "body",
               "required": true,
               "description": "Book model to create a book",
               "schema": {
                 "$ref": "#/definitions/NewBookAndAuthor"
               }
             }
           ],
           "responses": {
             "201": {
               "description": "Returns the book object created.",
               "schema": {
                 "$ref": "#/definitions/Book"
               }
             },
             "400": {
               "description": "Bad Request"
             }
           },
           "deprecated": false
         }
     },
      "/books/{id}": {
         "delete": {
           "summary": "Deletes a specific book",
           "description": "Deletes a specific book",
           "operationId": "deleteBookById",
           "tags": [
               "Books"
           ],
           "parameters": [
               {
                 "name": "id",
                 "in": "path",
                 "required": true,
                 "description": "The id of the book to delete",
                 "type": "string"
               }
          ],
          "responses": {
               "204": {
                 "description": "No Content"
               },
               "404": {
                 "description": "Not Found"
               }
             },
          "deprecated": false
         },
          "get": {
            "summary": "Info for a specific book",
            "operationId": "showBookById",
            "tags": [
              "Books"
            ],
            "parameters": [
              {
                "name": "id",
                "in": "path",
                "required": true,
                "description": "The id of the book to retrieve",
                "type": "string"
              }
            ],
            "responses": {
              "200": {
                "description": "Returns a book info.",
                "schema": {
                  "$ref": "#/definitions/Book"
                }
              },
              "404": {
                "description": "Not Found"
              }
            },
            "deprecated": false
        },
         "put": {
           "summary": "Updates a specific book",
           "description": "Updates a specific book info",
           "operationId": "updateBookById",
           "tags": [
               "Books"
           ],
           "parameters": [
               {
                 "name": "id",
                 "in": "path",
                 "required": true,
                 "description": "The id of the book to update",
                 "type": "string"
               },
               {
                 "name": "body",
                 "in": "body",
                 "required": true,
                 "description": "Book object to update info",
                 "schema": {
                    "$ref": "#/definitions/NewBook"
                 }
               }
             ],
            "responses": {
               "200": {
                 "description": "OK"
               },
               "400": {
                 "description": "Bad Request"
               },
               "404": {
                 "description": "Not Found"
               }
             },
           "deprecated": false
         }
      }
    },
    "definitions": {
      "Author": {
        "required": [
          "id",
          "first_name",
          "last_name"
        ],
        "properties": {
          "id": {
            "type": "integer",
            "format": "int64"
          },
          "first_name": {
            "type": "string"
          },
          "last_name": {
            "type": "string"
          }
       }
    },
    "NewAuthor": {
      "required": [
        "first_name",
        "last_name"
      ],
      "properties": {
        "first_name": {
          "type": "string"
        },
        "last_name": {
          "type": "string"
        }
      }
    },
    "Authors": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/Author"
      }
    },
    "Error": {
      "required": [
        "code",
        "message"
      ],
      "properties": {
        "code": {
          "type": "integer",
          "format": "int32"
        },
        "message": {
          "type": "string"
        }
      }
    },
    "Book": {
      "required": [
        "id",
        "title",
        "author",
        "isbn",
        "published"
      ],
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "title": {
          "type": "string"
        },
        "author": {
          "schema":{
             "$ref": "#/definitions/Author"
          }
        },
        "isbn": {
          "type": "string"
        },
        "published": {
          "type": "string"
        }
      }
    },
    "NewBook": {
      "required": [
        "title",
        "author",
        "isbn",
        "published"
      ],
      "properties": {
        "title": {
          "type": "string"
        },
        "author": {
          "type": "integer",
          "format": "int64"
        },
        "isbn": {
          "type": "string"
        },
        "published": {
          "type": "string",
          "format": "date"
        }
      }
    },
    "NewBookAndAuthor": {
      "required": [
        "title",
        "author",
        "isbn",
        "published"
      ],
      "properties": {
        "title": {
          "type": "string"
        },
        "author": {
          "schema": {
             "$ref": "#/definitions/NewAuthor"
          }
        },
        "isbn": {
          "type": "string"
        },
        "published": {
          "type": "string",
          "format": "date"
        }
      }
    },
    "Books": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/Book"
      }
    },
    "Error": {
      "required": [
        "code",
        "message"
      ],
      "properties": {
        "code": {
          "type": "integer",
          "format": "int32"
        },
        "message": {
          "type": "string"
        }
      }
    }
  }
}
