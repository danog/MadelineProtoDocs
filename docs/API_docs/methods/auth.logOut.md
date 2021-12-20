---
title: "auth.logOut"
description: "Logs out the user."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_logOut.html
---
# Method: auth.logOut
[Back to methods index](index.md)



Logs out the user.



### Return type: [auth.LoggedOut](../types/auth.LoggedOut.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_LoggedOut = $MadelineProto->auth->logOut();
```

Or, if you're into Lua:

```lua
auth_LoggedOut = auth.logOut({})
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|


