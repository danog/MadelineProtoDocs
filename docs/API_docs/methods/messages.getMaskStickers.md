---
title: "messages.getMaskStickers"
description: "Get installed mask stickers"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getMaskStickers.html
---
# Method: messages.getMaskStickers
[Back to methods index](index.md)



Get installed mask stickers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|[long](../types/long.md) |  | Yes|


### Return type: [messages.AllStickers](../types/messages.AllStickers.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_AllStickers = $MadelineProto->messages->getMaskStickers(['hash' => long, ]);
```

Or, if you're into Lua:

```lua
messages_AllStickers = messages.getMaskStickers({hash=long, })
```

