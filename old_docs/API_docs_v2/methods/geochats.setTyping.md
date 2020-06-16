---
title: geochats.setTyping
description: geochats.setTyping parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/geochats_setTyping.html
---
# Method: geochats.setTyping
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[InputGeoChat](../types/InputGeoChat.md) | Yes|
|typing|[Bool](../types/Bool.md) | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->geochats->setTyping(['peer' => InputGeoChat, 'typing' => Bool, ]);
```

Or, if you're into Lua:

```lua
Bool = geochats.setTyping({peer=InputGeoChat, typing=Bool, })
```

