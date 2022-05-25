from datetime import datetime
from pydantic import BaseModel, ValidationError
from typing import List, Optional


class User(BaseModel):
    id: int
    name: str = 'Michael Shuff'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2020-01-01T00:00:00',
    'friends': [1, 2, '2']
}
user = User(**external_data)
print(isinstance(user.id, int))
# > 123
print(repr(user.signup_ts))
# > datetime.datetime(2020, 1, 1, 0, 0)
print(user.friends)
# > [1, 2, 2]
print(user.dict())

try:
    User(singup_ts='broken', friends=[1, 2, 'not a number'])
except ValidationError as e:
    print(e.json())
