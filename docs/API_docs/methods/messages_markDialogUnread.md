---
title: messages.markDialogUnread
description: Mark dialog as unread 
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.markDialogUnread  
[Back to methods index](index.md)


Mark dialog as unread 

### Parameters:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|unread|[Bool](../types/Bool.md) | Optional|Should it be marked or unmarked as read|
|peer|[InputDialogPeer](../types/InputDialogPeer.md) | Yes|The dialog to mark as unread|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->markDialogUnread(['unread' => Bool, 'peer' => InputDialogPeer, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.markDialogUnread
* params - `{"unread": Bool, "peer": InputDialogPeer, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.markDialogUnread`

Parameters:

unread - Json encoded Bool

peer - Json encoded InputDialogPeer




Or, if you're into Lua:

```
Bool = messages.markDialogUnread({unread=Bool, peer=InputDialogPeer, })
```

