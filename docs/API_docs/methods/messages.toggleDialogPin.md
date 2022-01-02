---
title: "messages.toggleDialogPin"
description: "Pin/unpin a dialog"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_toggleDialogPin.html
---
# Method: messages.toggleDialogPin
[Back to methods index](index.md)



Pin/unpin a dialog

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|pinned|[Bool](../types/Bool.md) | Whether to pin or unpin the dialog | Optional|
|peer|[Username, chat ID, Update, Message or InputDialogPeer](../types/InputDialogPeer.md) | The dialog to pin | Yes|


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

$Bool = $MadelineProto->messages->toggleDialogPin(['pinned' => Bool, 'peer' => InputDialogPeer, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.toggleDialogPin({pinned=Bool, peer=InputDialogPeer, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|PINNED_DIALOGS_TOO_MUCH|Too many pinned dialogs|


