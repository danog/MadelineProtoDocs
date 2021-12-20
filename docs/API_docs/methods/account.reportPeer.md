---
title: "account.reportPeer"
description: "Report a peer for violation of telegram's Terms of Service"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_reportPeer.html
---
# Method: account.reportPeer
[Back to methods index](index.md)



Report a peer for violation of telegram's Terms of Service

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The peer to report | Optional|
|reason|[ReportReason](../types/ReportReason.md) | The reason why this peer is being reported | Yes|
|message|[string](../types/string.md) |  | Yes|


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

$Bool = $MadelineProto->account->reportPeer(['peer' => InputPeer, 'reason' => ReportReason, 'message' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = account.reportPeer({peer=InputPeer, reason=ReportReason, message='string', })
```


## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [Bool](../types/Bool.md) will be returned instead.


### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|PEER_ID_INVALID|The provided peer id is invalid|


