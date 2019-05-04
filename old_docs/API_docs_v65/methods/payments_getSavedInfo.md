---
title: payments.getSavedInfo
description: Get saved payments info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: payments.getSavedInfo  
[Back to methods index](index.md)


Get saved payments info



### Return type: [payments\_SavedInfo](../types/payments_SavedInfo.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_SavedInfo = $MadelineProto->payments->getSavedInfo();
```

Or, if you're into Lua:

```lua
payments_SavedInfo = payments.getSavedInfo({})
```

