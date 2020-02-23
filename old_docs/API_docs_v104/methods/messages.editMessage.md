---
title: messages.editMessage
description: Edit message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_editMessage.html
---
# Method: messages.editMessage  
[Back to methods index](index.md)


Edit message

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|no\_webpage|[Bool](../types/Bool.md) | Disable webpage preview | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Where was the message sent | Optional|
|id|[int](../types/int.md) | ID of the message to edit | Yes|
|message|[string](../types/string.md) | New message | Optional|
|media|[MessageMedia, Update, Message or InputMedia](../types/InputMedia.md) | New attached media | Optional|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Reply markup for inline keyboards | Optional|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | The new entities (for styled text) | Optional|
|parse\_mode| [string](../types/string.md) | Whether to parse HTML or Markdown markup in the message| Optional |


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

$Updates = $MadelineProto->messages->editMessage(['no_webpage' => Bool, 'peer' => InputPeer, 'id' => int, 'message' => 'string', 'media' => InputMedia, 'reply_markup' => ReplyMarkup, 'entities' => [MessageEntity, MessageEntity], 'parse_mode' => 'string', ]);
```

Or, if you're into Lua:

```lua
Updates = messages.editMessage({no_webpage=Bool, peer=InputPeer, id=int, message='string', media=InputMedia, reply_markup=ReplyMarkup, entities={MessageEntity}, parseMode='string', })
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
|400|BUTTON_DATA_INVALID|The data of one or more of the buttons you provided is invalid|
|400|BUTTON_TYPE_INVALID|The type of one or more of the buttons you provided is invalid|
|400|BUTTON_URL_INVALID|Button URL invalid|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|
|400|MEDIA_PREV_INVALID|Previous media invalid|
|400|MESSAGE_EDIT_TIME_EXPIRED|You can't edit this message anymore, too much time has passed since its creation.|
|400|MESSAGE_EMPTY|The provided message is empty|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|
|400|MESSAGE_NOT_MODIFIED|The message text has not changed|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|REPLY_MARKUP_INVALID|The provided reply markup is invalid|
|400|SCHEDULE_DATE_INVALID|Invalid schedule date provided|
|400|USER_BANNED_IN_CHANNEL|You're banned from sending messages in supergroups/channels|
|403|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|
|403|INLINE_BOT_REQUIRED|Only the inline bot can edit message|
|403|MESSAGE_AUTHOR_REQUIRED|Message author required|


