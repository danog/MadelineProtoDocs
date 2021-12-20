---
title: "messages.setChatTheme"
description: "messages.setChatTheme parameters, return type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setChatTheme.html
---
# Method: messages.setChatTheme
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|
|emoticon|[string](../types/string.md) | Yes|


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

$Updates = $MadelineProto->messages->setChatTheme(['peer' => InputPeer, 'emoticon' => 'string', ]);
```

Or, if you're into Lua:

```lua
Updates = messages.setChatTheme({peer=InputPeer, emoticon='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|EMOJI_INVALID|The specified theme emoji is valid|
|400|EMOJI_NOT_MODIFIED|The theme wasn't changed|


