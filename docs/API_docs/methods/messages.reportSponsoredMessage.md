---
title: "messages.reportSponsoredMessage"
description: "Report a [sponsored message »](https://core.telegram.org/api/sponsored-messages), see [here »](https://core.telegram.org/api/sponsored-messages#reporting-sponsored-messages) for more info on the full flow."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_reportSponsoredMessage.html
---
# Method: messages.reportSponsoredMessage
[Back to methods index](index.html)



Report a [sponsored message »](https://core.telegram.org/api/sponsored-messages), see [here »](https://core.telegram.org/api/sponsored-messages#reporting-sponsored-messages) for more info on the full flow.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|random\_id|[bytes](/API_docs/types/bytes.html) | The ad's unique ID. | Yes|
|option|[bytes](/API_docs/types/bytes.html) | Chosen report option, initially an empty string, see [here »](https://core.telegram.org/api/sponsored-messages#reporting-sponsored-messages) for more info on the full flow. | Yes|


### Return type: [channels.SponsoredMessageReportResult](/API_docs/types/channels.SponsoredMessageReportResult.html)

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

$channels_SponsoredMessageReportResult = $MadelineProto->messages->reportSponsoredMessage(random_id: 'bytes', option: 'bytes', );
```

