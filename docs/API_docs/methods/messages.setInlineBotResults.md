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
|next\_offset|[string](/API_docs/types/string.html) | Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don‘t support pagination. Offset length can’t exceed 64 bytes. | Optional|
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

$Bool = $MadelineProto->messages->setInlineBotResults(['gallery' => Bool, 'private' => Bool, 'query_id' => long, 'results' => [InputBotInlineResult, InputBotInlineResult], 'cache_time' => int, 'next_offset' => 'string', 'switch_pm' => InlineBotSwitchPM, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|ARTICLE_TITLE_EMPTY|The title of the article is empty|
|400|AUDIO_CONTENT_URL_EMPTY|The remote URL specified in the content field is empty|
|400|AUDIO_TITLE_EMPTY|An empty audio title was provided.|
|400|BUTTON_DATA_INVALID|The data of one or more of the buttons you provided is invalid|
|400|BUTTON_TYPE_INVALID|The type of one or more of the buttons you provided is invalid|
|400|BUTTON_URL_INVALID|Button URL invalid|
|400|DOCUMENT_INVALID|The specified document is invalid|
|400|FILE_CONTENT_TYPE_INVALID|File content-type is invalid|
|400|FILE_TITLE_EMPTY|An empty file title was specified|
|400|GIF_CONTENT_TYPE_INVALID|GIF content-type invalid|
|400|MESSAGE_EMPTY|The provided message is empty|
|400|MESSAGE_TOO_LONG|The provided message is too long|
|400|NEXT_OFFSET_INVALID|The specified offset is longer than 64 bytes.|
|400|PHOTO_CONTENT_TYPE_INVALID|Photo mime-type invalid|
|400|PHOTO_CONTENT_URL_EMPTY|Photo URL invalid|
|400|PHOTO_INVALID|Photo invalid|
|400|PHOTO_THUMB_URL_EMPTY|Photo thumbnail URL is empty|
|400|QUERY_ID_INVALID|The query ID is invalid|
|400|REPLY_MARKUP_INVALID|The provided reply markup is invalid|
|400|RESULT_ID_DUPLICATE|You provided a duplicate result ID|
|400|RESULT_TYPE_INVALID|Result type invalid|
|400|RESULTS_TOO_MUCH|Too many results were provided|
|400|SEND_MESSAGE_MEDIA_INVALID|Invalid media provided|
|400|SEND_MESSAGE_TYPE_INVALID|The message type is invalid|
|400|START_PARAM_INVALID|Start parameter invalid|
|400|STICKER_DOCUMENT_INVALID|The specified sticker document is invalid|
|400|URL_INVALID|Invalid URL provided|
|400|USER_BOT_INVALID|This method can only be called by a bot|
|400|VIDEO_TITLE_EMPTY|The specified video title is empty|
|400|WEBDOCUMENT_INVALID|Invalid webdocument URL provided|
|400|WEBDOCUMENT_MIME_INVALID|Invalid webdocument mime type provided|
|400|WEBDOCUMENT_SIZE_TOO_BIG|Webdocument is too big!|
|400|WEBDOCUMENT_URL_INVALID|The specified webdocument URL is invalid|
|403|USER_BOT_INVALID|This method can only be called by a bot|


