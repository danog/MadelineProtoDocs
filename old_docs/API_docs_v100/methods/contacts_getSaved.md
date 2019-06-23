---
title: contacts.getSaved
description: Get saved contacts
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.getSaved  
[Back to methods index](index.md)


Get saved contacts



### Return type: [Vector\_of\_SavedContact](../types/SavedContact.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_SavedContact = $MadelineProto->contacts->getSaved();
```

Or, if you're into Lua:

```lua
Vector_of_SavedContact = contacts.getSaved({})
```

