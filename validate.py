import requests
from jsonschema import validate
# def test01():
#     json_data={
#         "code": "SUCCESS",
#         "errMsg": "",
#         "data": False
#         }
#     json_schema={
#         "type": "object",
#         "required": [],
#         "properties": {
#             "code": {
#                 "type": "string"
#                 },
#             "errMsg": {
#                 "type": "string"
#                 },
#             "data": {
#                 "type": "boolean"
#                 }
#             }
#         }
#     validate(json_data,json_schema)
# def test02():
#     url = "http://47.108.157.13:8090/blog/getList"
#     header = {
#         "user_token_header":"eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MywidXNlck5hbWUiOiJ6aGFuZ3NhbiIsImV4cCI6MTc3MTgzOTQ5NX0.8X1XbRmmjT8Qqx-LssGL2qNi9dHLvazelGjoMElRyEA"
#     }
#     r = requests.get(url=url,headers=header)
#     json_schema = {
#         "type": "object",
#         "required": [],
#         "properties": {
#             "code": {
#                 "type": "string"
#             },
#             "errMsg": {
#                 "type": "string"
#             },
#             "data": {
#                 "type": "array",
#                 "items": {
#                     "type": "object",
#                     "required": [],
#                     "properties": {
#                         "id": {
#                             "type": "number"
#                         },
#                         "title": {
#                             "type": "string"
#                         },
#                         "content": {
#                             "type": "string"
#                         },
#                         "userId": {
#                             "type": "number"
#                         },
#                         "deleteFlag": {
#                             "type": "number"
#                         },
#                         "createTime": {
#                             "type": "string"
#                         },
#                         "updateTime": {
#                             "type": "string"
#                         },
#                         "loginUser": {
#                             "type": "boolean"
#                         }
#                     }
#                 }
#             }
#         }
#     }
#     validate(r.json(),json_schema)
# def test03():
#     json_data={
#         "code": "SUCCESS",
#         "errMsg": 20,
#         "data": False
#         }
#     json_schema={
#         "type": "object",
#         "required": [],
#         "properties": {
#             "code": {
#                 "type": "string"
#                 },
#             "errMsg": {
#                 "type": "integer"
#                 },
#             "data": {
#                 "type": "boolean"
#                 }
#             }
#         }
#     validate(json_data,json_schema)
# def test04():
#     json_data={
#         "age":20
#     }
#     json_schema={
#         "type": "object",
#         "properties": {
#             "age": {
#                 "type": "integer",
#                 "minimum": 0,
#                 "maximum": 120
#             }
#         }
#     }
#     validate(json_data,json_schema)
# def test05():
#     json_data={
#         "email":"321",
#         "username":"q11qq"
#     }
#     json_schema={
#         "type": "object",
#         "properties": {
#             "email": {
#                 "type": "string"
#             },
#             "username": {
#                 "type": "string",
#                 "pattern": r"\S{5,10}"
#             }
#         }
#     }
#     validate(json_data,json_schema)
# def test06():
#     json_data={
#         "email":[1,2,3,4,5,6,1]
#     }
#     json_schema={
#         "type": "object",
#         "properties": {
#             "email": {
#                 "type": "array",
#                 "items": {
#                     "type": "number"
#                 },
#                 "minItems": 2,
#                 "maxItems": 20,
#                 "uniqueItems": True
#             }
#         }
#     }
#     validate(json_data,json_schema)
# def test07():
#     json_data = {
#         "code": "SUCCESS",
#         "errMsg": "",
#         "data": [
#             {
#                 "id": 58519,
#                 "title": "Sat Feb 21 23:05:12 CST 2026",
#                 "content": "##在这里写下一篇博客",
#                 "userId": 3,
#                 "deleteFlag": 0,
#                 "createTime": "2026-01-17 14:29",
#                 "updateTime": "2026-01-17T06:29:15.000+00:00",
#                 "loginUser": False,
#             }
#         ]
#     }
#     json_schema = {
#         "type": "object",
#         "required": [],
#         "properties": {
#             "code": {
#                 "type": "string"
#             },
#             "errMsg": {
#                 "type": "string"
#             },
#             "data": {
#                 "type": "array",
#                 "items": {
#                     "type": "object",
#                     "required": [],
#                     "additionalProperties": False,
#                     "maxProperties": 1,
#                     "properties": {
#                         "id": {
#                             "type": "number"
#                         },
#                         "title": {
#                             "type": "string"
#                         },
#                         "content": {
#                             "type": "string"
#                         },
#                         "userId": {
#                             "type": "number"
#                         },
#                         "deleteFlag": {
#                             "type": "number"
#                         },
#                         "createTime": {
#                             "type": "string"
#                         },
#                         "updateTime": {
#                             "type": "string"
#                         },
#                         "loginUser": {
#                             "type": "boolean"
#                         }
#                     }
#                 }
#             }
#         }
#     }
#     validate(json_data,json_schema)
# def test08():
#     json_data={
#         "name":"111",
#         "email":"111"
#     }
#     json_schema={
#         "type": "object",
#         "properties": {
#             "name": {
#                 "type": "string"
#             },
#             "email": {
#                 "type": "string"
#             }
#         },
#         "required": ["name", "email"]
#     }
#     validate(json_data, json_schema)
# def test09():
#     json_data={
#         "creditCard":"111",
#         "billingAddress":"111"
#     }
#     json_schema={
#         "type": "object",
#         "properties": {
#             "creditCard": {
#                 "type": "string"
#             },
#             "billingAddress": {
#                 "type": "string"
#             }
#         },
#         "dependentRequired": {
#             "creditCard": ["billingAddress"]
#         }
#     }
#     validate(json_data, json_schema)
