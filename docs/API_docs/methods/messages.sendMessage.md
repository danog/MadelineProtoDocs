---
title: messages.sendMessage
description: Sends a message to a chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendMessage.html
---
# Method: messages.sendMessage  
[Back to methods index](index.md)


Sends a message to a chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|no\_webpage|[Bool](../types/Bool.md) | Set this flag to disable generation of the webpage preview | Optional|
|silent|[Bool](../types/Bool.md) | Send this message silently (no notifications for the receivers) | Optional|
|background|[Bool](../types/Bool.md) | Send this message as background message | Optional|
|clear\_draft|[Bool](../types/Bool.md) | Clear the draft field | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The destination where the message will be sent | Optional|
|reply\_to\_msg\_id|[int](../types/int.md) | The message ID to which this message will reply to | Optional|
|message|[string](../types/string.md) | The message | Yes|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Reply markup for sending bot buttons | Optional|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Entities to send (for styled text) | Optional|
|parse\_mode| [string](../types/string.md) | Whether to parse HTML or Markdown markup in the message| Optional |
|schedule\_date|[int](../types/int.md) | Scheduled message date for scheduled messages | Optional|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->sendMessage(['no_webpage' => Bool, 'silent' => Bool, 'background' => Bool, 'clear_draft' => Bool, 'peer' => InputPeer, 'reply_to_msg_id' => int, 'message' => 'string', 'reply_markup' => ReplyMarkup, 'entities' => [MessageEntity, MessageEntity], 'parse_mode' => 'string', 'schedule_date' => int, ]);
```

Or, if you're into Lua:

```lua
Updates = messages.sendMessage({no_webpage=Bool, silent=Bool, background=Bool, clear_draft=Bool, peer=InputPeer, reply_to_msg_id=int, message='string', reply_markup=ReplyMarkup, entities={MessageEntity}, parseMode='string', schedule_date=int, })
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
|400|BOT_DOMAIN_INVALID|Bot domain invalid|
|400|BOT_INVALID|This is not a valid bot|
|400|BUTTON_DATA_INVALID|The data of one or more of the buttons you provided is invalid|
|400|BUTTON_TYPE_INVALID|The type of one or more of the buttons you provided is invalid|
|400|BUTTON_URL_INVALID|Button URL invalid|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|CHAT_RESTRICTED|You can't send messages in this chat, you were restricted|
|400|ENCRYPTION_DECLINED|The secret chat was declined|
|400|ENTITY_MENTION_USER_INVALID|You mentioned an invalid user|
|400|FROM_MESSAGE_BOT_DISABLED|Bots can't use fromMessage min constructors|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|
|400|MESSAGE_EMPTY|The provided message is empty|
|400|MESSAGE_TOO_LONG|The provided message is too long|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|PINNED_DIALOGS_TOO_MUCH|Too many pinned dialogs|
|400|REPLY_MARKUP_INVALID|The provided reply markup is invalid|
|400|SCHEDULE_BOT_NOT_ALLOWED|Bots cannot schedule messages|
|400|SCHEDULE_TOO_MUCH|There are too many scheduled messages|
|400|USER_BANNED_IN_CHANNEL|You're banned from sending messages in supergroups/channels|
|400|USER_IS_BLOCKED|You were blocked by this user|
|400|USER_IS_BOT|Bots can't send messages to other bots|
|400|YOU_BLOCKED_USER|You blocked this user|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|AUTH_KEY_PERM_EMPTY|The temporary auth key must be binded to the permanent auth key to use these methods.|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|
|420|SLOWMODE_WAIT_X|Slowmode is enabled in this chat: you must wait for the specified number of seconds before sending another message to the chat.|
|-503|Timeout|Timeout while fetching data|


