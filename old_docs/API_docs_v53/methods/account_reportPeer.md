---
title: account.reportPeer
description: Report for spam
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.reportPeer  
[Back to methods index](index.md)


Report for spam

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The peer to report | Optional|
|reason|[ReportReason](../types/ReportReason.md) | Why are you reporting this peer | Yes|


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

$Bool = $MadelineProto->account->reportPeer(['peer' => InputPeer, 'reason' => ReportReason, ]);
```

Or, if you're into Lua:

```lua
Bool = account.reportPeer({peer=InputPeer, reason=ReportReason, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PEER_ID_INVALID|The provided peer id is invalid|


