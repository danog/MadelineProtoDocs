---
title: "messages.getInlineBotResults"
description: "Query an inline bot"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getInlineBotResults.html
---
# Method: messages.getInlineBotResults
[Back to methods index](index.html)



Query an inline bot

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The bot to query | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The currently opened chat | Optional|
|geo\_point|[InputGeoPoint](/API_docs/types/InputGeoPoint.html) | The geolocation, if requested | Optional|
|query|[string](/API_docs/types/string.html) | The query | Yes|
|offset|[string](/API_docs/types/string.html) | The offset within the results, will be passed directly as-is to the bot. | Yes|


### Return type: [messages.BotResults](/API_docs/types/messages.BotResults.html)

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
$messages_BotResults = $MadelineProto->messages->getInlineBotResults(bot: InputUser, peer: InputPeer, geo_point: InputGeoPoint, query: 'string', offset: 'string', );
```

