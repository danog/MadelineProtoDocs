---
title: "channels.createChannel"
description: "Create a [supergroup/channel](https://core.telegram.org/api/channel)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_createChannel.html
---
# Method: channels.createChannel
[Back to methods index](index.html)



Create a [supergroup/channel](https://core.telegram.org/api/channel).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|broadcast|[Bool](/API_docs/types/Bool.html) | Whether to create a [channel](https://core.telegram.org/api/channel) | Optional|
|megagroup|[Bool](/API_docs/types/Bool.html) | Whether to create a [supergroup](https://core.telegram.org/api/channel) | Optional|
|for\_import|[Bool](/API_docs/types/Bool.html) | Whether the supergroup is being created to import messages from a foreign chat service using [messages.initHistoryImport](../methods/messages.initHistoryImport.html) | Optional|
|title|[string](/API_docs/types/string.html) | Channel title | Yes|
|about|[string](/API_docs/types/string.html) | Channel description | Yes|
|geo\_point|[InputGeoPoint](/API_docs/types/InputGeoPoint.html) | Geogroup location | Optional|
|address|[string](/API_docs/types/string.html) | Geogroup address | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Updates = $MadelineProto->channels->createChannel(broadcast: Bool, megagroup: Bool, for_import: Bool, title: 'string', about: 'string', geo_point: InputGeoPoint, address: 'string', );
```

