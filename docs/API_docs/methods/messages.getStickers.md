---
title: "messages.getStickers"
description: "Get stickers by emoji"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getStickers.html
---
# Method: messages.getStickers
[Back to methods index](index.md)



Get stickers by emoji

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|emoticon|[string](../types/string.md) | The emoji | Yes|
|hash|[long](../types/long.md) |  | Yes|


### Return type: [messages.Stickers](../types/messages.Stickers.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Stickers = $MadelineProto->messages->getStickers(['emoticon' => 'string', 'hash' => long, ]);
```

Or, if you're into Lua:

```lua
messages_Stickers = messages.getStickers({emoticon='string', hash=long, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|EMOTICON_EMPTY|The emoji is empty|


