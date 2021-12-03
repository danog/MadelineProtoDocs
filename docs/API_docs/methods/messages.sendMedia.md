---
title: messages.sendMedia
description: Send a media
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendMedia.html
---
# Method: messages.sendMedia
[Back to methods index](index.md)



Send a media

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](../types/Bool.md) | Send message silently (no notification should be triggered) | Optional|
|background|[Bool](../types/Bool.md) | Send message in background | Optional|
|clear\_draft|[Bool](../types/Bool.md) | Clear the draft | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Destination | Optional|
|reply\_to\_msg\_id|[int](../types/int.md) | Message ID to which this message should reply to | Optional|
|media|[MessageMedia, Update, Message or InputMedia](../types/InputMedia.md) | Attached media | Optional|
|message|[string](../types/string.md) | Caption | Yes|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Reply markup for bot keyboards | Optional|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Message [entities](https://core.telegram.org/api/entities) for styled text | Optional|
|parse\_mode| [string](../types/string.md) | Whether to parse HTML or Markdown markup in the message| Optional |
|schedule\_date|[int](../types/int.md) | Scheduled message date for [scheduled messages](https://core.telegram.org/api/scheduled-messages) | Optional|
|send\_as|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) |  | Optional|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->sendMedia(['silent' => Bool, 'background' => Bool, 'clear_draft' => Bool, 'peer' => InputPeer, 'reply_to_msg_id' => int, 'media' => InputMedia, 'message' => 'string', 'reply_markup' => ReplyMarkup, 'entities' => [MessageEntity, MessageEntity], 'parse_mode' => 'string', 'schedule_date' => int, 'send_as' => InputPeer, ]);
```

Or, if you're into Lua:

```lua
Updates = messages.sendMedia({silent=Bool, background=Bool, clear_draft=Bool, peer=InputPeer, reply_to_msg_id=int, media=InputMedia, message='string', reply_markup=ReplyMarkup, entities={MessageEntity}, parseMode='string', schedule_date=int, send_as=InputPeer, })
```


## Usage of reply_markup

You can provide bot API reply_markup objects here.  



## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [Updates](../types/Updates.md) will be returned instead.



## Usage of parseMode:

Set parseMode to html to enable HTML parsing of the message.  

Set parseMode to Markdown to enable markown AND html parsing of the message.  

The following tags are currently supported:

```html
<br>a newline
<b><i>bold works ok, internal tags are stripped</i> </b>
<strong>bold</strong>
<em>italic</em>
<i>italic</i>
<u>underline</u>
<s>strikethrough</s>
<del>strikethrough</del>
<strike>strikethrough</strike>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>
<blockquote>pre-formatted fixed-width code block</blockquote>
<a href="https://github.com">URL</a>
<a href="mention:@danogentili">Mention by username</a>
<a href="mention:186785362">Mention by user id</a>
<pre language="json">Pre tags can have a language attribute</pre>
```

You can also use normal markdown, note that to create mentions you must use the `mention:` syntax like in html:  

```markdown
[Mention by username](mention:@danogentili)
[Mention by user id](mention:186785362)
```

MadelineProto supports all html entities supported by [html_entity_decode](http://php.net/manual/en/function.html-entity-decode.php).
### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|420|SLOWMODE_WAIT_X|Slowmode is enabled in this chat: wait X seconds before sending another message to this chat.|
|400|BOT_PAYMENTS_DISABLED|Please enable bot payments in botfather before calling this method.|
|400|BROADCAST_PUBLIC_VOTERS_FORBIDDEN|You can't forward polls with public voters|
|400|BUTTON_DATA_INVALID|The data of one or more of the buttons you provided is invalid|
|400|BUTTON_TYPE_INVALID|The type of one or more of the buttons you provided is invalid|
|400|BUTTON_URL_INVALID|Button URL invalid|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_RESTRICTED|You can't send messages in this chat, you were restricted|
|400|CURRENCY_TOTAL_AMOUNT_INVALID|The total amount of all prices is invalid|
|400|EMOTICON_INVALID|The specified emoji is invalid|
|400|EXTERNAL_URL_INVALID|External URL invalid|
|400|FILE_PART_LENGTH_INVALID|The length of a file part is invalid|
|400|FILE_PARTS_INVALID|The number of file parts is invalid|
|400|FILE_REFERENCE_EMPTY|An empty [file reference](https://core.telegram.org/api/file_reference) was specified|
|400|FILE_REFERENCE_EXPIRED|File reference expired, it must be refetched as described in https://core.telegram.org/api/file_reference|
|400|GAME_BOT_INVALID|Bots can't send another bot's game.|
|400|IMAGE_PROCESS_FAILED|Failure while processing image|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|
|400|MD5_CHECKSUM_INVALID|The MD5 checksums do not match|
|400|MEDIA_CAPTION_TOO_LONG|The caption is too long|
|400|MEDIA_EMPTY|The provided media object is invalid|
|400|MEDIA_INVALID|Media invalid|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PAYMENT_PROVIDER_INVALID|The specified payment provider is invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|PHOTO_EXT_INVALID|The extension of the photo is invalid|
|400|PHOTO_INVALID_DIMENSIONS|The photo dimensions are invalid|
|400|PHOTO_SAVE_FILE_INVALID|Internal issues, try again later|
|400|POLL_ANSWER_INVALID|One of the poll answers is not acceptable|
|400|POLL_ANSWERS_INVALID|Invalid poll answers were provided|
|400|POLL_OPTION_DUPLICATE|Duplicate poll options provided|
|400|POLL_OPTION_INVALID|Invalid poll option provided|
|400|POLL_QUESTION_INVALID|One of the poll questions is not acceptable|
|400|QUIZ_CORRECT_ANSWER_INVALID|An invalid value was provided to the correct_answers field|
|400|QUIZ_CORRECT_ANSWERS_EMPTY|No correct quiz answer was specified|
|400|QUIZ_CORRECT_ANSWERS_TOO_MUCH|You specified too many correct answers in a quiz, quizes can only have one right answer!|
|400|QUIZ_MULTIPLE_INVALID|Quizes can't have the multiple_choice flag set!|
|400|REPLY_MARKUP_BUY_EMPTY|Reply markup for buy button empty|
|400|REPLY_MARKUP_INVALID|The provided reply markup is invalid|
|400|SCHEDULE_BOT_NOT_ALLOWED|Bots cannot schedule messages|
|400|SCHEDULE_DATE_TOO_LATE|You can't schedule a message this far in the future|
|400|SCHEDULE_TOO_MUCH|There are too many scheduled messages|
|400|SEND_AS_PEER_INVALID|You can't send messages as the specified peer|
|400|TTL_MEDIA_INVALID|Invalid media Time To Live was provided|
|400|USER_BANNED_IN_CHANNEL|You're banned from sending messages in supergroups/channels|
|400|USER_IS_BLOCKED|You were blocked by this user|
|400|USER_IS_BOT|Bots can't send messages to other bots|
|400|VIDEO_CONTENT_TYPE_INVALID|The video's content type is invalid|
|400|WEBPAGE_CURL_FAILED|Failure while fetching the webpage with cURL|
|400|WEBPAGE_MEDIA_EMPTY|Webpage media empty|
|400|YOU_BLOCKED_USER|You blocked this user|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|403|CHAT_SEND_GIFS_FORBIDDEN|You can't send gifs in this chat|
|403|CHAT_SEND_MEDIA_FORBIDDEN|You can't send media in this chat|
|403|CHAT_SEND_POLL_FORBIDDEN|You can't send polls in this chat|
|403|CHAT_SEND_STICKERS_FORBIDDEN|You can't send stickers in this chat.|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|
|403|USER_IS_BLOCKED|You were blocked by this user|
|-504|memory limit exit|Internal error|
|-503|Timeout|Timeout while fetching data|


