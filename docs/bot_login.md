---
title: bot_login
description: bot_login parameters, return type and example
---
## Method: bot_login  


### Parameters:

| Name     |    Type       |
|----------|---------------|
|token| A string with the bot token|

### Return type: [auth.Authorization](API_docs/types/auth_Authorization.md)

### Example ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
$authorization = yield $this->bot_login($token);
```
