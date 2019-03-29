---
title: messages.sendMessage
description: Send a message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.sendMessage  
[Back to methods index](index.md)


Send a message

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|no\_webpage|[Bool](../types/Bool.md) | Disable webpage preview? | Optional|
|silent|[Bool](../types/Bool.md) | Disable notifications? | Optional|
|background|[Bool](../types/Bool.md) | Disable background notifications? | Optional|
|clear\_draft|[Bool](../types/Bool.md) | Clear the message draft of this chat? | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat where to send this message | Optional|
|reply\_to\_msg\_id|[int](../types/int.md) | Reply to message by ID | Optional|
|message|[string](../types/string.md) | The message to send | Yes|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Keyboards to send | Optional|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Entities to send (for styled text) | Optional|
|parse\_mode| [string](../types/string.md) | Whether to parse HTML or Markdown markup in the message| Optional |


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->sendMessage(['no_webpage' => Bool, 'silent' => Bool, 'background' => Bool, 'clear_draft' => Bool, 'peer' => InputPeer, 'reply_to_msg_id' => int, 'message' => 'string', 'reply_markup' => ReplyMarkup, 'entities' => [MessageEntity, MessageEntity], 'parse_mode' => 'string', ]);
```

Or, if you're into Lua:

```lua
Updates = messages.sendMessage({no_webpage=Bool, silent=Bool, background=Bool, clear_draft=Bool, peer=InputPeer, reply_to_msg_id=int, message='string', reply_markup=ReplyMarkup, entities={MessageEntity}, parse_mode='string', })
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
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>
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
### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|BUTTON_DATA_INVALID|The provided button data is invalid|
|BUTTON_TYPE_INVALID|The type of one of the buttons you provided is invalid|
|BUTTON_URL_INVALID|Button URL invalid|
|CHANNEL_INVALID|The provided channel is invalid|
|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|CHAT_ID_INVALID|The provided chat id is invalid|
|ENTITY_MENTION_USER_INVALID|You can't use this entity|
|INPUT_USER_DEACTIVATED|The specified user was deleted|
|MESSAGE_EMPTY|The provided message is empty|
|MESSAGE_TOO_LONG|The provided message is too long|
|PEER_ID_INVALID|The provided peer id is invalid|
|REPLY_MARKUP_INVALID|The provided reply markup is invalid|
|USER_BANNED_IN_CHANNEL|You're banned from sending messages in supergroups/channels|
|USER_IS_BLOCKED|User is blocked|
|USER_IS_BOT|Bots can't send messages to other bots|
|YOU_BLOCKED_USER|You blocked this user|
|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|NEED_MEMBER_INVALID|The provided member is invalid|
|RANDOM_ID_DUPLICATE|You provided a random ID that was already used|
|CHAT_WRITE_FORBIDDEN|You can't write in this chat|
|tanti SALUTI da peppe lg .|Ciao da un pony|
|Timeout|A timeout occurred while fetching data from the bot|


