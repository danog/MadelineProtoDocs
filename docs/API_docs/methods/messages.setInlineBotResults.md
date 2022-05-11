---
title: "messages.setInlineBotResults"
description: "Answer an inline query, for bots only"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setInlineBotResults.html
---
# Method: messages.setInlineBotResults
[Back to methods index](index.html)



Answer an inline query, for bots only

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|gallery|[Bool](/API_docs/types/Bool.html) | Set this flag if the results are composed of media files | Optional|
|private|[Bool](/API_docs/types/Bool.html) | Set this flag if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query | Optional|
|query\_id|[long](/API_docs/types/long.html) | Unique identifier for the answered query | Yes|
|results|Array of [InputBotInlineResult](/API_docs/types/InputBotInlineResult.html) | Vector of results for the inline query | Yes|
|cache\_time|[int](/API_docs/types/int.html) | The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300. | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes. | Optional|
|switch\_pm|[InlineBotSwitchPM](/API_docs/types/InlineBotSwitchPM.html) | If passed, clients will display a button with specified text that switches the user to a private chat with the bot and sends the bot a start message with a certain parameter. | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->messages->setInlineBotResults(gallery: Bool, private: Bool, query_id: long, results: [InputBotInlineResult, InputBotInlineResult], cache_time: int, next_offset: 'string', switch_pm: InlineBotSwitchPM, );
```

