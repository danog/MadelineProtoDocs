---
title: "messages.report"
description: "Report a message in a chat for violation of telegram's Terms of Service"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_report.html
---
# Method: messages.report
[Back to methods index](index.html)



Report a message in a chat for violation of telegram's Terms of Service

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer | Optional|
|id|Array of [int](/API_docs/types/int.html) | IDs of messages to report | Yes|
|option|[bytes](/API_docs/types/bytes.html) |  | Yes|
|message|[string](/API_docs/types/string.html) | Comment for report moderation | Optional|


### Return type: [ReportResult](/API_docs/types/ReportResult.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$ReportResult = $MadelineProto->messages->report(peer: $InputPeer, id: [$int, $int], option: 'bytes', message: 'string', );
```


## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [ReportResult](../types/ReportResult.html) will be returned instead.


