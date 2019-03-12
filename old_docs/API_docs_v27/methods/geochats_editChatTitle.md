---
title: geochats.editChatTitle
description: Edit geochat title
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: geochats.editChatTitle  
[Back to methods index](index.md)


Edit geochat title

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[InputGeoChat](../types/InputGeoChat.md) | The geochat | Yes|
|title|[string](../types/string.md) | The new title | Yes|
|address|[string](../types/string.md) | The new address | Yes|


### Return type: [geochats\_StatedMessage](../types/geochats_StatedMessage.md)

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

$geochats_StatedMessage = $MadelineProto->geochats->editChatTitle(['peer' => InputGeoChat, 'title' => 'string', 'address' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - geochats.editChatTitle
* params - `{"peer": InputGeoChat, "title": "string", "address": "string", }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/geochats.editChatTitle`

Parameters:

peer - Json encoded InputGeoChat

title - Json encoded string

address - Json encoded string




Or, if you're into Lua:

```lua
geochats_StatedMessage = geochats.editChatTitle({peer=InputGeoChat, title='string', address='string', })
```

