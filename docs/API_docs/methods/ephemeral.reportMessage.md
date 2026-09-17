---
title: "ephemeral.reportMessage"
description: "ephemeral.reportMessage parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/ephemeral_reportMessage.html
---
# Method: ephemeral.reportMessage
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|id|[int](/API_docs/types/int.html) | Optional|
|option|[bytes](/API_docs/types/bytes.html) | Yes|
|message|[string](/API_docs/types/string.html) | Optional|


### Return type: [ReportResult](/API_docs/types/ReportResult.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$ReportResult = $MadelineProto->ephemeral->reportMessage(peer: $InputPeer, id: $int, option: 'bytes', message: 'string', );
```


## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [ReportResult](../types/ReportResult.html) will be returned instead.


