---
title: auth.acceptLoginToken
description: auth.acceptLoginToken parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_acceptLoginToken.html
---
# Method: auth.acceptLoginToken  
[Back to methods index](index.md)


### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|token|[bytes](../types/bytes.md) | Yes|


### Return type: [Authorization](../types/Authorization.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Authorization = $MadelineProto->auth->acceptLoginToken(['token' => 'bytes', ]);
```

Or, if you're into Lua:

```lua
Authorization = auth.acceptLoginToken({token='bytes', })
```

