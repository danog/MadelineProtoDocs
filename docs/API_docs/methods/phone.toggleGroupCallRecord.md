---
title: "phone.toggleGroupCallRecord"
description: "phone.toggleGroupCallRecord parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_toggleGroupCallRecord.html
---
# Method: phone.toggleGroupCallRecord
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|start|[Bool](../types/Bool.md) | Optional|
|video|[Bool](../types/Bool.md) | Optional|
|call|[InputGroupCall](../types/InputGroupCall.md) | Yes|
|title|[string](../types/string.md) | Optional|
|video\_portrait|[Bool](../types/Bool.md) | Optional|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->phone->toggleGroupCallRecord(['start' => Bool, 'video' => Bool, 'call' => InputGroupCall, 'title' => 'string', 'video_portrait' => Bool, ]);
```

Or, if you're into Lua:

```lua
Updates = phone.toggleGroupCallRecord({start=Bool, video=Bool, call=InputGroupCall, title='string', video_portrait=Bool, })
```

