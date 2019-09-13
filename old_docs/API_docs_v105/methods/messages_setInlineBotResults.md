---
title: messages.setInlineBotResults
description: Bots only: set the results of an inline query
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.setInlineBotResults  
[Back to methods index](index.md)


Bots only: set the results of an inline query

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|gallery|[Bool](../types/Bool.md) | Is this a gallery? | Optional|
|private|[Bool](../types/Bool.md) | Is this result private (not cached)? | Optional|
|query\_id|[long](../types/long.md) | Query ID | Yes|
|results|Array of [InputBotInlineResult](../types/InputBotInlineResult.md) | Results | Yes|
|cache\_time|[int](../types/int.md) | Cache time | Yes|
|next\_offset|[string](../types/string.md) | The next offset | Optional|
|switch\_pm|[InlineBotSwitchPM](../types/InlineBotSwitchPM.md) | Switch to PM? | Optional|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->setInlineBotResults(['gallery' => Bool, 'private' => Bool, 'query_id' => long, 'results' => [InputBotInlineResult, InputBotInlineResult], 'cache_time' => int, 'next_offset' => 'string', 'switch_pm' => InlineBotSwitchPM, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.setInlineBotResults({gallery=Bool, private=Bool, query_id=long, results={InputBotInlineResult}, cache_time=int, next_offset='string', switch_pm=InlineBotSwitchPM, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|ARTICLE_TITLE_EMPTY|The title of the article is empty|
|400|BUTTON_DATA_INVALID|The data of one or more of the buttons you provided is invalid|
|400|BUTTON_TYPE_INVALID|The type of one or more of the buttons you provided is invalid|
|400|BUTTON_URL_INVALID|Button URL invalid|
|400|MESSAGE_EMPTY|The provided message is empty|
|400|MESSAGE_TOO_LONG|The provided message is too long|
|400|PHOTO_INVALID|Photo invalid|
|400|PHOTO_THUMB_URL_EMPTY|Photo thumbnail URL is empty|
|400|QUERY_ID_INVALID|The query ID is invalid|
|400|REPLY_MARKUP_INVALID|The provided reply markup is invalid|
|400|RESULT_TYPE_INVALID|Result type invalid|
|400|SEND_MESSAGE_TYPE_INVALID|The message type is invalid|
|400|START_PARAM_INVALID|Start parameter invalid|
|403|USER_BOT_INVALID|This method can only be called by a bot|


