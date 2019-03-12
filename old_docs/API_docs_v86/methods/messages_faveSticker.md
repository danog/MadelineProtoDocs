---
title: messages.faveSticker
description: Add a sticker to favorites
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.faveSticker  
[Back to methods index](index.md)


Add a sticker to favorites

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[MessageMedia, Update, Message or InputDocument](../types/InputDocument.md) | The sticker to add to favorites | Optional|
|unfave|[Bool](../types/Bool.md) | Remove it from favorites? | Yes|


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

$Bool = $MadelineProto->messages->faveSticker(['id' => InputDocument, 'unfave' => Bool, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.faveSticker
* params - `{"id": InputDocument, "unfave": Bool, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.faveSticker`

Parameters:

id - Json encoded InputDocument

unfave - Json encoded Bool




Or, if you're into Lua:

```lua
Bool = messages.faveSticker({id=InputDocument, unfave=Bool, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|STICKER_ID_INVALID|The provided sticker ID is invalid|


