---
title: account.setAuthorizationTTL
description: account.setAuthorizationTTL parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_setAuthorizationTTL.html
---
# Method: account.setAuthorizationTTL
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|authorization\_ttl\_days|[int](../types/int.md) | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->setAuthorizationTTL(['authorization_ttl_days' => int, ]);
```

Or, if you're into Lua:

```lua
Bool = account.setAuthorizationTTL({authorization_ttl_days=int, })
```

