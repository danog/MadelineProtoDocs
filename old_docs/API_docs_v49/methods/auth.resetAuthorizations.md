---
title: auth.resetAuthorizations
description: Terminates all user's authorized sessions except for the current one.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_resetAuthorizations.html
---
# Method: auth.resetAuthorizations
[Back to methods index](index.md)



Terminates all user's authorized sessions except for the current one.

After calling this method it is necessary to reregister the current device using the method [account.registerDevice](../methods/account.registerDevice.md)



### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->auth->resetAuthorizations();
```

Or, if you're into Lua:

```lua
Bool = auth.resetAuthorizations({})
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|406|FRESH_RESET_AUTHORISATION_FORBIDDEN|You can't logout other sessions if less than 24 hours have passed since you logged on the current session|
|-503|Timeout|Timeout while fetching data|


