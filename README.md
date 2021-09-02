# Simple ticket system
Test task for Selectel

### How to start
#### Local
1. Clone repo
2. pip install -r requirements.txt
3. Make ```Flask run```

#### Docker
1. Clone repo
2. docker-compose up -d

### Flake8
You can run flake with ```make codestyle```
### isort
You can run isort with ```make optimize_imports```

## ENDPOINTS

### Create ticket:
PATH: ```api/v1/ticket``` - POST
PAYLOAD:
```
{
    "subject": "Your subject",
    "text": "Your text",
    "email": "test@mail.ru"
}
```
RESPONSE:
```
{
    "comments": [],
    "created": "2021-09-02 18:33:15.035960",
    "email": "test@mail.ru",
    "id": 11,
    "status": "OPEN",
    "subject": "Your123 subject",
    "text": "Your text",
    "updated": "None"
}
```

### Get ticket
PATH: ```api/v1/ticket/:id``` - GET
RESPONSE:
```
{
    "comments": [],
    "created": "2021-09-02 18:33:15.035960",
    "email": "test@mail.ru",
    "id": 11,
    "status": "OPEN",
    "subject": "Your123 subject",
    "text": "Your text",
    "updated": "None"
}
```

### Update status
PATH: ```api/v1/ticket/:id/status``` - PATCH
PAYLOAD:
```
{
    "status": "CLOSED"
}
```

### Add comment
PATH: ```api/v1/ticket/:id/comment``` - POST
PAYLOAD:
```
{
    "text": "Your commentary",
    "email": "test@mail.ru"
}
```
RESPONSE:
```
{
    "created": "2021-09-02 18:36:03.124839",
    "email": "test@mail.ru",
    "id": 1,
    "text": "Your commentary",
    "ticket_id": 11
}
```