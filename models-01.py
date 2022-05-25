'''
The primary means of defining objects in pydantic is via models (models are simply classes which inherit from BaseModel).
You can think of models as similar to types in strictly typed languages, or as the requirements of a single endpoint in an API.
Untrusted data can be passed to a model, and after parsing and validation pydantic guarantees that the fields of the resultant model instance will conform to the field types defined on the model.

pydantic is primarily a parsing library, not a validation library. Validation is a means to an end: building a model which conforms to the types and constraints provided.

In other words, pydantic guarantees the types and constraints of the output model, not the input data.

This might sound like an esoteric distinction, but it is not. If you're unsure what this means or how it might affect your usage you should read the section about Data Conversion below.

Although validation is not the main purpose of pydantic, you can use this library for custom validation.
'''
############################## Basic Model Usage ###############################
from pydantic import BaseModel
'''
User here is a model with two fields:
  - id which is an integer and is required
  - name which is a string and is not required (it has a default value)
The type of name is inferred from the default value, and so a type annotation is not required (however note this warning about field order when some fields do not have type annotations).
'''
class User(BaseModel):
    id: int
    name = 'Jane Doe'

# user here is an instance of User. Initialisation of the object will perform all parsing and validation, if no ValidationError is raised, you know the resulting model instance is valid.
user = User(id='123')

# Fields of a model can be accessed as normal attributes of the user object. The string '123' has been cast to an int as per the field type
assert user.id == 123

# name wasn't set when user was initialised, so it has the default value
assert user.name == 'Jane Doe'

# The fields which were supplied when user was initialized
# Either .dict() or dict(user) will provide a dict of fields, but .dict() can take numerous other arguments.
assert user.dict() == dict(user) == {'id': 123, 'name': 'Jane Doe'}

# This model is mutable so field values can be changed.
user.id = 321
assert user.id == 321

############################### Model Properties ###############################
'''
Models possess the following methods and attributes:
- dict() - returns a dictionary of the model's fields and values; cf. exporting models
- json()
returns a JSON string representation dict(); cf. exporting models
- copy() - returns a copy (by default, shallow copy) of the model; cf. exporting models
- parse_obj() - a utility for loading any object into a model with error handling if the object is not a dictionary; cf. helper functions
- parse_raw() - a utility for loading strings of numerous formats; cf. helper functions
- parse_file() - like parse_raw() but for file paths; cf. helper function
- from_orm() - loads data into a model from an arbitrary class; cf. ORM mode
- schema() - returns a dictionary representing the model as JSON Schema; cf. schema
- schema_json() - returns a JSON string representation of schema(); cf. schema
- construct() - a class method for creating models without running validation; cf. Creating models without validation
- __fields_set__ - Set of names of fields which were set when the model instance was initialised
- __fields__ - a dictionary of the model's fields
- __config__ - the configuration class for the model, cf. model config
'''

print(user.dict())

print(user.parse_obj({'id': '123', 'name': 'Jane Doe'}))
