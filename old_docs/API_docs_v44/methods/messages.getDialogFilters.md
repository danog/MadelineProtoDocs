---
title: messages.getDialogFilters
description: Get [folders](https://core.telegram.org/api/folders)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getDialogFilters.html
---
# Method: messages.getDialogFilters
[Back to methods index](index.md)



Get [folders](https://core.telegram.org/api/folders)



### Return type: [Vector\_of\_DialogFilter](../types/DialogFilter.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_DialogFilter = $MadelineProto->messages->getDialogFilters();
```

Or, if you're into Lua:

```lua
Vector_of_DialogFilter = messages.getDialogFilters({})
```

