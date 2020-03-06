---
title: messages.reportSpam
description: Report a new incoming chat for spam, if the [peer settings](../constructors/peerSettings.md) of the chat allow us to do that
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_reportSpam.html
---
# Method: messages.reportSpam  
[Back to methods index](index.md)


Report a new incoming chat for spam, if the [peer settings](../constructors/peerSettings.md) of the chat allow us to do that

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer to report | Optional|


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

$Bool = $MadelineProto->messages->reportSpam(['peer' => InputPeer, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.reportSpam({peer=InputPeer, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PEER_ID_INVALID|The provided peer id is invalid|


