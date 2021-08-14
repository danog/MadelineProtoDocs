---
title: payments.getSavedInfo
description: Get saved payment information
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getSavedInfo.html
---
# Method: payments.getSavedInfo
[Back to methods index](index.md)



Get saved payment information



### Return type: [payments.SavedInfo](../types/payments.SavedInfo.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_SavedInfo = $MadelineProto->payments->getSavedInfo();
```

Or, if you're into Lua:

```lua
payments_SavedInfo = payments.getSavedInfo({})
```

