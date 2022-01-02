---
title: botLogin
description: botLogin parameters, return type and example
grand_parent: "Telegram RPC API"
parent: "Methods"
redirect_from: /bot_login.html
---
## Method: botLogin  


### Parameters:

| Name     |    Type       |
|----------|---------------|
|token| A string with the bot token|

### Return type: [auth.Authorization](API_docs/types/auth.Authorization.md)

### Example ([now fully async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
$authorization = yield $this->botLogin($token);
```
