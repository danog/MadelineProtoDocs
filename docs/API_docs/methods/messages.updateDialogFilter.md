---
title: messages.updateDialogFilter
description: messages.updateDialogFilter parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_updateDialogFilter.html
---
# Method: messages.updateDialogFilter  
[Back to methods index](index.md)


### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[int](../types/int.md) | Yes|
|filter|[DialogFilter](../types/DialogFilter.md) | Optional|


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

$Bool = $MadelineProto->messages->updateDialogFilter(['id' => int, 'filter' => DialogFilter, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.updateDialogFilter({id=int, filter=DialogFilter, })
```

