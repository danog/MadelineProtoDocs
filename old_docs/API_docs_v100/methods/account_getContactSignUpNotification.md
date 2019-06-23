---
title: account.getContactSignUpNotification
description: Contact signup notification setting value
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getContactSignUpNotification  
[Back to methods index](index.md)


Contact signup notification setting value



### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->getContactSignUpNotification();
```

Or, if you're into Lua:

```lua
Bool = account.getContactSignUpNotification({})
```

