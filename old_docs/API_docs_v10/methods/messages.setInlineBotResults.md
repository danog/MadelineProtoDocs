---
title: messages.setInlineBotResults
description: Answer an inline query, for bots only
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setInlineBotResults.html
---
# Method: messages.setInlineBotResults
[Back to methods index](index.md)



Answer an inline query, for bots only

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|gallery|[Bool](../types/Bool.md) | Set this flag if the results are composed of media files | Optional|
|private|[Bool](../types/Bool.md) | Set this flag if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query | Optional|
|query\_id|[long](../types/long.md) | Unique identifier for the answered query | Yes|
|results|Array of [InputBotInlineResult](../types/InputBotInlineResult.md) | Vector of results for the inline query | Yes|
|cache\_time|[int](../types/int.md) | The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300. | Yes|
|next\_offset|[string](../types/string.md) | Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don‘t support pagination. Offset length can’t exceed 64 bytes. | Optional|


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

$Bool = $MadelineProto->messages->setInlineBotResults(['gallery' => Bool, 'private' => Bool, 'query_id' => long, 'results' => [InputBotInlineResult, InputBotInlineResult], 'cache_time' => int, 'next_offset' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = messages.setInlineBotResults({gallery=Bool, private=Bool, query_id=long, results={InputBotInlineResult}, cache_time=int, next_offset='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|ARTICLE_TITLE_EMPTY|The title of the article is empty|
|400|BUTTON_DATA_INVALID|The data of one or more of the buttons you provided is invalid|
|400|BUTTON_TYPE_INVALID|The type of one or more of the buttons you provided is invalid|
|400|BUTTON_URL_INVALID|Button URL invalid|
|400|GIF_CONTENT_TYPE_INVALID|GIF content-type invalid|
|400|MESSAGE_EMPTY|The provided message is empty|
|400|MESSAGE_TOO_LONG|The provided message is too long|
|400|PHOTO_CONTENT_TYPE_INVALID|Photo mime-type invalid|
|400|PHOTO_CONTENT_URL_EMPTY|Photo URL invalid|
|400|PHOTO_INVALID|Photo invalid|
|400|PHOTO_THUMB_URL_EMPTY|Photo thumbnail URL is empty|
|400|QUERY_ID_INVALID|The query ID is invalid|
|400|REPLY_MARKUP_INVALID|The provided reply markup is invalid|
|400|RESULT_TYPE_INVALID|Result type invalid|
|400|RESULTS_TOO_MUCH|Too many results were provided|
|400|SEND_MESSAGE_MEDIA_INVALID|Invalid media provided|
|400|SEND_MESSAGE_TYPE_INVALID|The message type is invalid|
|400|START_PARAM_INVALID|Start parameter invalid|
|400|WEBDOCUMENT_INVALID|Invalid webdocument URL provided|
|400|WEBDOCUMENT_MIME_INVALID|Invalid webdocument mime type provided|
|400|WEBDOCUMENT_SIZE_TOO_BIG|Webdocument is too big!|
|403|USER_BOT_INVALID|This method can only be called by a bot|


