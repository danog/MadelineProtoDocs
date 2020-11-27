---
title: geochats.editChatTitle
description: geochats.editChatTitle parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/geochats_editChatTitle.html
---
# Method: geochats.editChatTitle
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[InputGeoChat](../types/InputGeoChat.md) | Yes|
|title|[string](../types/string.md) | Yes|
|address|[string](../types/string.md) | Yes|


### Return type: [geochats.StatedMessage](../types/geochats.StatedMessage.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$geochats_StatedMessage = $MadelineProto->geochats->editChatTitle(['peer' => InputGeoChat, 'title' => 'string', 'address' => 'string', ]);
```

Or, if you're into Lua:

```lua
geochats_StatedMessage = geochats.editChatTitle({peer=InputGeoChat, title='string', address='string', })
```

