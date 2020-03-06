---
title: updates.getState
description: You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/updates_getState.html
---
# Method: updates.getState  
[Back to methods index](index.md)


You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates



### Return type: [updates.State](../types/updates.State.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$updates.State = $MadelineProto->updates->getState();
```

Or, if you're into Lua:

```lua
updates.State = updates.getState({})
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|-503|Timeout|Timeout while fetching data|


