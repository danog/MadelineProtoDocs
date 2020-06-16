---
title: messages.report
description: Report a message in a chat for violation of telegram's Terms of Service
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_report.html
---
# Method: messages.report
[Back to methods index](index.md)



Report a message in a chat for violation of telegram's Terms of Service

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|
|id|Array of [int](../types/int.md) | IDs of messages to report | Yes|
|reason|[ReportReason](../types/ReportReason.md) | Why are these messages being reported | Yes|


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

$Bool = $MadelineProto->messages->report(['peer' => InputPeer, 'id' => [int, int], 'reason' => ReportReason, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.report({peer=InputPeer, id={int}, reason=ReportReason, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PEER_ID_INVALID|The provided peer id is invalid|


