# Overview

## Features

**App ~ Facebook / FetLife**

### Current

```
1. Account: Account / Profile / Relationship
2. Feed: Post > ShortPost + LongPost
```

```py
post = {
  "title": str,
  "text": str,
  "video": file,
  "images": list(file),
  "is_short": bool,
  "is_long": bool,
}
```

### Backlog

```
3. Group
4. Event
5. Message
6. Membership > PersonalMembership + ProfitMembership
```

## Architect

* **Database**: PostgreSQL
* **Backend**: Django and Django REST framework
* **Frontend**: Hybrid use of Django and React
