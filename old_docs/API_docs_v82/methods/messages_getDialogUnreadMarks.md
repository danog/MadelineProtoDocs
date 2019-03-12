---
title: messages.getDialogUnreadMarks
description: Get dialogs marked as unread manually
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getDialogUnreadMarks  
[Back to methods index](index.md)


Get dialogs marked as unread manually



### Return type: [Vector\_of\_DialogPeer](../types/DialogPeer.md)

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

$Vector_of_DialogPeer = $MadelineProto->messages->getDialogUnreadMarks();
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.getDialogUnreadMarks
* params - `{}`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.getDialogUnreadMarks`

Parameters:




Or, if you're into Lua:

```lua
Vector_of_DialogPeer = messages.getDialogUnreadMarks({})
```

