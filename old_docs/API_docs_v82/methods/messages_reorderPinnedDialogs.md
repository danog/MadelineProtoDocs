---
title: messages.reorderPinnedDialogs
description: Reorder pinned dialogs
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.reorderPinnedDialogs  
[Back to methods index](index.md)


Reorder pinned dialogs

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|force|[Bool](../types/Bool.md) | Force reordering | Optional|
|order|Array of [Username, chat ID, Update, Message or InputDialogPeer](../types/InputDialogPeer.md) | New order | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->reorderPinnedDialogs(['force' => Bool, 'order' => [InputDialogPeer, InputDialogPeer], ]);
```

Or, if you're into Lua:

```lua
Bool = messages.reorderPinnedDialogs({force=Bool, order={InputDialogPeer}, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PEER_ID_INVALID|The provided peer id is invalid|


