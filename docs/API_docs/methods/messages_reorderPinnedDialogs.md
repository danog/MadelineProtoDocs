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
|order|Array of [InputDialogPeer](../types/InputDialogPeer.md) | New order | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->reorderPinnedDialogs(['force' => Bool, 'order' => [InputDialogPeer, InputDialogPeer], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.reorderPinnedDialogs`

Parameters:

force - Json encoded Bool

order - Json encoded  array of InputDialogPeer




Or, if you're into Lua:

```
Bool = messages.reorderPinnedDialogs({force=Bool, order={InputDialogPeer}, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PEER_ID_INVALID|The provided peer id is invalid|


