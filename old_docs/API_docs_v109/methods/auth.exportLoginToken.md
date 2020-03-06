---
title: auth.exportLoginToken
description: auth.exportLoginToken parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_exportLoginToken.html
---
# Method: auth.exportLoginToken  
[Back to methods index](index.md)


### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|api\_id|[int](../types/int.md) | Yes|
|api\_hash|[string](../types/string.md) | Yes|
|except\_ids|Array of [int](../types/int.md) | Yes|


### Return type: [auth.LoginToken](../types/auth.LoginToken.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth.LoginToken = $MadelineProto->auth->exportLoginToken(['api_id' => int, 'api_hash' => 'string', 'except_ids' => [int, int], ]);
```

Or, if you're into Lua:

```lua
auth.LoginToken = auth.exportLoginToken({api_id=int, api_hash='string', except_ids={int}, })
```

