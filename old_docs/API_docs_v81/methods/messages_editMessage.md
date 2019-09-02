---
title: messages.editMessage
description: Edit a message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.editMessage  
[Back to methods index](index.md)


Edit a message

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|no\_webpage|[Bool](../types/Bool.md) | Disable webpage preview | Optional|
|stop\_geo\_live|[Bool](../types/Bool.md) | Stop live location | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat | Optional|
|id|[int](../types/int.md) | The message ID | Yes|
|message|[string](../types/string.md) | The new message | Optional|
|media|[MessageMedia, Update, Message or InputMedia](../types/InputMedia.md) | The media to substitute | Optional|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | The new keyboard | Optional|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | The new entities (for styled text) | Optional|
|parse\_mode| [string](../types/string.md) | Whether to parse HTML or Markdown markup in the message| Optional |
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | The new location | Optional|


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

$Updates = $MadelineProto->messages->editMessage(['no_webpage' => Bool, 'stop_geo_live' => Bool, 'peer' => InputPeer, 'id' => int, 'message' => 'string', 'media' => InputMedia, 'reply_markup' => ReplyMarkup, 'entities' => [MessageEntity, MessageEntity], 'parse_mode' => 'string', 'geo_point' => InputGeoPoint, ]);
```

Or, if you're into Lua:

```lua
Updates = messages.editMessage({no_webpage=Bool, stop_geo_live=Bool, peer=InputPeer, id=int, message='string', media=InputMedia, reply_markup=ReplyMarkup, entities={MessageEntity}, parse_mode='string', geo_point=InputGeoPoint, })
```


## Usage of reply_markup

You can provide bot API reply_markup objects here.  



## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [Updates](../types/Updates.md) will be returned instead.



## Usage of parse_mode:

Set parse_mode to html to enable HTML parsing of the message.  

Set parse_mode to Markdown to enable markown AND html parsing of the message.  

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
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|
|400|MESSAGE_EDIT_TIME_EXPIRED|You can't edit this message anymore, too much time has passed since its creation.|
|400|MESSAGE_EMPTY|The provided message is empty|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|
|400|MESSAGE_NOT_MODIFIED|The message text has not changed|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|USER_BANNED_IN_CHANNEL|You're banned from sending messages in supergroups/channels|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|
|403|MESSAGE_AUTHOR_REQUIRED|Message author required|


