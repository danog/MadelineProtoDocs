---
title: messages.toggleDialogPin
description: Pin or unpin dialog
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.toggleDialogPin  
[Back to methods index](index.md)


Pin or unpin dialog

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|pinned|[Bool](../types/Bool.md) | Pin or unpin the dialog? | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The peer to pin | Optional|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->toggleDialogPin(['pinned' => Bool, 'peer' => InputPeer, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.toggleDialogPin`

Parameters:

pinned - Json encoded Bool

peer - Json encoded InputPeer




Or, if you're into Lua:

```lua
Bool = messages.toggleDialogPin({pinned=Bool, peer=InputPeer, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PEER_ID_INVALID|The provided peer id is invalid|


