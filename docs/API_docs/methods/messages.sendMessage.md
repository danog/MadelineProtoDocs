---
title: "messages.sendMessage"
description: "Sends a message to a chat"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendMessage.html
---
# Method: messages.sendMessage
[Back to methods index](index.html)



Sends a message to a chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|no\_webpage|[Bool](/API_docs/types/Bool.html) | Set this flag to disable generation of the webpage preview | Optional|
|silent|[Bool](/API_docs/types/Bool.html) | Send this message silently (no notifications for the receivers) | Optional|
|background|[Bool](/API_docs/types/Bool.html) | Send this message as background message | Optional|
|clear\_draft|[Bool](/API_docs/types/Bool.html) | Clear the draft field | Optional|
|noforwards|[Bool](/API_docs/types/Bool.html) | Only for bots, disallows forwarding and saving of the messages, even if the destination chat doesn't have [content protection](https://telegram.org/blog/protected-content-delete-by-date-and-more) enabled | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The destination where the message will be sent | Optional|
|reply\_to\_msg\_id|[int](/API_docs/types/int.html) | The message ID to which this message will reply to | Optional|
|message|[string](/API_docs/types/string.html) | The message | Yes|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.html) | Reply markup for sending bot buttons | Optional|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Message [entities](https://core.telegram.org/api/entities) for sending styled text | Optional|
|parse\_mode| [string](/API_docs/types/string.html) | Whether to parse HTML or Markdown markup in the message| Optional |
|schedule\_date|[int](/API_docs/types/int.html) | Scheduled message date for [scheduled messages](https://core.telegram.org/api/scheduled-messages) | Optional|
|send\_as|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Send this message as the specified peer | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

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
$Updates = $MadelineProto->messages->sendMessage(no_webpage: Bool, silent: Bool, background: Bool, clear_draft: Bool, noforwards: Bool, peer: InputPeer, reply_to_msg_id: int, message: 'string', reply_markup: ReplyMarkup, entities: [MessageEntity, MessageEntity], parse_mode: 'string', schedule_date: int, send_as: InputPeer, );
```


## Usage of reply_markup

You can provide bot API reply_markup objects here.  



## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [Updates](../types/Updates.html) will be returned instead.



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
