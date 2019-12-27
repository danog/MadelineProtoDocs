---
title: account.getAuthorizations
description: Get logged-in sessions
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getAuthorizations  
[Back to methods index](index.md)


Get logged-in sessions



### Return type: [account\_Authorizations](../types/account_Authorizations.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_Authorizations = $MadelineProto->account->getAuthorizations();
```

Or, if you're into Lua:

```lua
account_Authorizations = account.getAuthorizations({})
```

