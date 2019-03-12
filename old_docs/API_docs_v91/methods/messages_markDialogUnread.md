---
title: messages.markDialogUnread
description: Mark dialog as unread 
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.markDialogUnread  
[Back to methods index](index.md)


Mark dialog as unread 

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|unread|[Bool](../types/Bool.md) | Should it be marked or unmarked as read | Optional|
|peer|[Username, chat ID, Update, Message or InputDialogPeer](../types/InputDialogPeer.md) | The dialog to mark as unread | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
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

```lua
Bool = messages.markDialogUnread({unread=Bool, peer=InputDialogPeer, })
```

