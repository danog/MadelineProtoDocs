---
title: account.getWebAuthorizations
description: Get telegram web login authorizations
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getWebAuthorizations  
[Back to methods index](index.md)


Get telegram web login authorizations



### Return type: [account\_WebAuthorizations](../types/account_WebAuthorizations.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_WebAuthorizations = $MadelineProto->account->getWebAuthorizations();
```

Or, if you're into Lua:

```lua
account_WebAuthorizations = account.getWebAuthorizations({})
```

