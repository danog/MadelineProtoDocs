---
title: messages.saveGif
description: Save a GIF
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.saveGif  
[Back to methods index](index.md)


Save a GIF

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[MessageMedia, Update, Message or InputDocument](../types/InputDocument.md) | The GIF to save | Optional|
|unsave|[Bool](../types/Bool.md) | Remove the gif? | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->saveGif(['id' => InputDocument, 'unsave' => Bool, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.saveGif({id=InputDocument, unsave=Bool, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|GIF_ID_INVALID|The provided GIF ID is invalid|


