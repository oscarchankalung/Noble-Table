# Overview

## Features

**App ~ Facebook**

* Account / Profile / Relationships
* Post > ShortPost + LongPost
* ~~Group~~
* ~~Event~~
* ~~Message~~

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

## Architect

* Database: PostgreSQL
* Backend: Django and Django REST framework
* Frontend: Hybrid use of Django and React
