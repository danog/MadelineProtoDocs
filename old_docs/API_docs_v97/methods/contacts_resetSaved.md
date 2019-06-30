---
title: contacts.resetSaved
description: Reset saved contacts
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.resetSaved  
[Back to methods index](index.md)


Reset saved contacts



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

$Bool = $MadelineProto->contacts->resetSaved();
```

Or, if you're into Lua:

```lua
Bool = contacts.resetSaved({})
```

