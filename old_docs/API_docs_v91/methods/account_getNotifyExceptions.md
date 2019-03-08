---
title: account.getNotifyExceptions
description: Get notification exceptions
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getNotifyExceptions  
[Back to methods index](index.md)


Get notification exceptions

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|compare\_sound|[Bool](../types/Bool.md) | Compare sound? | Optional|
|peer|[Username, chat ID, Update, Message or InputNotifyPeer](../types/InputNotifyPeer.md) | Peer | Optional|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->account->getNotifyExceptions(['compare_sound' => Bool, 'peer' => InputNotifyPeer, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.getNotifyExceptions
* params - `{"compare_sound": Bool, "peer": InputNotifyPeer, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.getNotifyExceptions`

Parameters:

compare_sound - Json encoded Bool

peer - Json encoded InputNotifyPeer




Or, if you're into Lua:

```lua
Updates = account.getNotifyExceptions({compare_sound=Bool, peer=InputNotifyPeer, })
```

