---
title: account.getWebAuthorizations
description: Get web [login widget](https://core.telegram.org/widgets/login) authorizations
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getWebAuthorizations  
[Back to methods index](index.md)


Get web [login widget](https://core.telegram.org/widgets/login) authorizations



### Return type: [account\_WebAuthorizations](../types/account_WebAuthorizations.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_WebAuthorizations = $MadelineProto->account->getWebAuthorizations();
```

Or, if you're into Lua:

```lua
account_WebAuthorizations = account.getWebAuthorizations({})
```

