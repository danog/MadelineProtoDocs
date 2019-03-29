---
title: account.unregisterDevice
description: Stop sending PUSH notifications to app
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.unregisterDevice  
[Back to methods index](index.md)


Stop sending PUSH notifications to app

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|token\_type|[int](../types/int.md) | Device token type. Possible values: 1 - APNS, 2 - GCM, 3 - MPNS, 4 - Simple Push, 5 - Ubuntu Phone,6 - Blackberry, and other, see source code of official apps for more info | Yes|
|token|[string](../types/string.md) | Device token type. Possible values: 1 - APNS, 2 - GCM, 3 - MPNS, 4 - Simple Push, 5 - Ubuntu Phone,6 - Blackberry, and other, see source code of official apps for more info | Yes|
|other\_uids|Array of [int](../types/int.md) | Other UIDs | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->unregisterDevice(['token_type' => int, 'token' => 'string', 'other_uids' => [int, int], ]);
```

Or, if you're into Lua:

```lua
Bool = account.unregisterDevice({token_type=int, token='string', other_uids={int}, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|TOKEN_INVALID|The provided token is invalid|


