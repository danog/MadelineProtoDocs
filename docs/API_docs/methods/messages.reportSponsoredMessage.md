---
title: "messages.reportSponsoredMessage"
description: "messages.reportSponsoredMessage parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_reportSponsoredMessage.html
---
# Method: messages.reportSponsoredMessage
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|option|[bytes](/API_docs/types/bytes.html) | Yes|


### Return type: [channels.SponsoredMessageReportResult](/API_docs/types/channels.SponsoredMessageReportResult.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$channels_SponsoredMessageReportResult = $MadelineProto->messages->reportSponsoredMessage(peer: $InputPeer, option: 'bytes', );
```

