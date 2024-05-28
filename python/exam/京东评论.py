import requests
import json
from yuri_util import *

class Person:
  def __init__(self, name, age, **kwargs) -> None:
    self.name = name
    self.age = age

s = '{ "name": "张三", "age": 30, "city": "北京" }'
info() << json.loads(s)
person = Person(**json.loads(s))
info() << person.name