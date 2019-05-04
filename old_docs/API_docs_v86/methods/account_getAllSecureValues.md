---
title: account.getAllSecureValues
description: Get all secure telegram passport values
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getAllSecureValues  
[Back to methods index](index.md)


Get all secure telegram passport values



### Return type: [Vector\_of\_SecureValue](../types/SecureValue.md)

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

$Vector_of_SecureValue = $MadelineProto->account->getAllSecureValues();
```

Or, if you're into Lua:

```lua
Vector_of_SecureValue = account.getAllSecureValues({})
```

