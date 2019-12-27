---
title: account.getAuthorizationForm
description: Returns a Telegram Passport authorization form for sharing data with a service
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getAuthorizationForm  
[Back to methods index](index.md)


Returns a Telegram Passport authorization form for sharing data with a service

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot\_id|[int](../types/int.md) | User identifier of the service's bot | Yes|
|scope|[string](../types/string.md) | Telegram Passport element types requested by the service | Yes|
|public\_key|[string](../types/string.md) | Service's public key | Yes|


### Return type: [account.AuthorizationForm](../types/account.AuthorizationForm.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account.AuthorizationForm = $MadelineProto->account->getAuthorizationForm(['bot_id' => int, 'scope' => 'string', 'public_key' => 'string', ]);
```

Or, if you're into Lua:

```lua
account.AuthorizationForm = account.getAuthorizationForm({bot_id=int, scope='string', public_key='string', })
```

