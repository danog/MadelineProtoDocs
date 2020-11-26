---
title: messages.saveGif
description: Add GIF to saved gifs list
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_saveGif.html
---
# Method: messages.saveGif
[Back to methods index](index.md)



Add GIF to saved gifs list

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[MessageMedia, Update, Message or InputDocument](../types/InputDocument.md) | GIF to save | Optional|
|unsave|[Bool](../types/Bool.md) | Whether to remove GIF from saved gifs list | Yes|


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

$Bool = $MadelineProto->messages->saveGif(['id' => InputDocument, 'unsave' => Bool, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.saveGif({id=InputDocument, unsave=Bool, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|GIF_ID_INVALID|The provided GIF ID is invalid|


