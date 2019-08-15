---
title: contacts.exportCard
description: Export contact as card
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.exportCard  
[Back to methods index](index.md)


Export contact as card



### Return type: [Vector\_of\_int](../types/int.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_int = $MadelineProto->contacts->exportCard();
```

Or, if you're into Lua:

```lua
Vector_of_int = contacts.exportCard({})
```

