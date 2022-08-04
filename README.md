# BloomTech Labs Data Science API Template

## Tech Stack
- Logic: Python
- API Framework: FastAPI
- Validation: Pydantic
- Database: MongoDB
- Unit Testing: DocTest


## API Structure
All endpoints must return JSON compatible data.

- API Root `/` Swagger Docs
- API Version `/version` () -> String
  - HTTP Method: GET
- Create User `/create-user` (User) -> Bool
  - HTTP Method: POST
- Read Users `/read-users` (Query) -> Array[User]
  - HTTP Method: PUT
- Update Users `/update-users` (Query, Update) -> Bool
  - HTTP Method: PATCH
- Delete Users `/delete-users` (Query) -> Bool
  - HTTP Method: DELETE


## App Structure
- `/app/` Application Package
  - `__init__`
  - `api.py` API File
  - `database.py` Database Interface
  - `generators.py` Random Generators
  - `seeds.py` DB Seed Script
  - `utilities.py` General Tools
  - `validation.py` Data Validation Schema
- `.env` Environment Variables
- `Procfile` Server Run Script
- `requirements.txt` Dependencies
- `run.sh` Local Run Script


## Data Schemas
The following classes are used to validate incoming data to the API.
### User
- `name` Required String (maxLength: 128 minLength: 3)
- `age` Required Integer (maximum: 120, minimum: 1)
- `email` Required String(EmailStr)
- `active` Optional Boolean
- `score` Required Float (maximum: 1, minimum: 0)

### UserQuery
- `name` Optional String (maxLength: 128 minLength: 3)
- `age` Optional Integer (maximum: 120, minimum: 1)
- `email` Optional String(EmailStr)
- `active` Optional Boolean
- `score` Optional Float (maximum: 1, minimum: 0)

### UserUpdate
- `name` Optional String (maxLength: 128 minLength: 3)
- `age` Optional Integer (maximum: 120, minimum: 1)
- `email` Optional String(EmailStr)
- `active` Optional Boolean
- `score` Optional Float (maximum: 1, minimum: 0)
