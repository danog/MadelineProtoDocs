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
|order|Array of [Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | New order | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->reorderPinnedDialogs(['force' => Bool, 'order' => [InputPeer, InputPeer], ]);
```

Or, if you're into Lua:

```lua
Bool = messages.reorderPinnedDialogs({force=Bool, order={InputPeer}, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PEER_ID_INVALID|The provided peer id is invalid|


