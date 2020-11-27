---
title: geochats.getFullChat
description: geochats.getFullChat parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/geochats_getFullChat.html
---
# Method: geochats.getFullChat
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[InputGeoChat](../types/InputGeoChat.md) | Yes|


### Return type: [messages.ChatFull](../types/messages.ChatFull.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_ChatFull = $MadelineProto->geochats->getFullChat(['peer' => InputGeoChat, ]);
```

Or, if you're into Lua:

```lua
messages_ChatFull = geochats.getFullChat({peer=InputGeoChat, })
```

