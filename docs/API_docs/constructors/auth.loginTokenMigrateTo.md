---
title: "auth.loginTokenMigrateTo"
description: "Repeat the query to the specified DC"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_loginTokenMigrateTo.html
---
# Constructor: auth.loginTokenMigrateTo  
[Back to constructors index](/API_docs/constructors/index.md)



Repeat the query to the specified DC

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dc\_id|[int](/API_docs/types/int.md) | Yes|DC ID|
|token|[bytes](/API_docs/types/bytes.md) | Yes|Token to use for login|



### Type: [auth.LoginToken](/API_docs/types/auth.LoginToken.md)


### Example:

```php
$auth_loginTokenMigrateTo = ['_' => 'auth.loginTokenMigrateTo', 'dc_id' => int, 'token' => 'bytes'];
```  
