---
title: "channels.convertToGigagroup"
description: "Convert a [supergroup](https://core.telegram.org/api/channel) to a [gigagroup](https://core.telegram.org/api/channel), when requested by [channel suggestions](https://core.telegram.org/api/config#channel-suggestions)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_convertToGigagroup.html
---
# Method: channels.convertToGigagroup
[Back to methods index](index.html)



Convert a [supergroup](https://core.telegram.org/api/channel) to a [gigagroup](https://core.telegram.org/api/channel), when requested by [channel suggestions](https://core.telegram.org/api/config#channel-suggestions).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | The [supergroup](https://core.telegram.org/api/channel) to convert | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->channels->convertToGigagroup(channel: $InputChannel, );
```

