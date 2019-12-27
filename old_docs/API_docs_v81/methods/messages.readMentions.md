---
title: messages.readMentions
description: Mark mentions as read
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_readMentions.html
---
# Method: messages.readMentions  
[Back to methods index](index.md)


Mark mentions as read

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Dialog | Optional|


### Return type: [messages.AffectedHistory](../types/messages.AffectedHistory.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.AffectedHistory = $MadelineProto->messages->readMentions(['peer' => InputPeer, ]);
```

Or, if you're into Lua:

```lua
messages.AffectedHistory = messages.readMentions({peer=InputPeer, })
```

