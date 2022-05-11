---
title: "messages.editMessage"
description: "Edit message"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_editMessage.html
---
# Method: messages.editMessage
[Back to methods index](index.html)



Edit message

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|no\_webpage|[Bool](/API_docs/types/Bool.html) | Disable webpage preview | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Where was the message sent | Optional|
|id|[int](/API_docs/types/int.html) | ID of the message to edit | Yes|
|message|[string](/API_docs/types/string.html) | New message | Optional|
|media|[MessageMedia, Update, Message or InputMedia](/API_docs/types/InputMedia.html) | New attached media | Optional|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.html) | Reply markup for inline keyboards | Optional|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | [Message entities for styled text](https://core.telegram.org/api/entities) | Optional|
|parse\_mode| [string](/API_docs/types/string.html) | Whether to parse HTML or Markdown markup in the message| Optional |
|schedule\_date|[int](/API_docs/types/int.html) | Scheduled message date for [scheduled messages](https://core.telegram.org/api/scheduled-messages) | Optional|


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
$Updates = $MadelineProto->messages->editMessage(no_webpage: Bool, peer: InputPeer, id: int, message: 'string', media: InputMedia, reply_markup: ReplyMarkup, entities: [MessageEntity, MessageEntity], parse_mode: 'string', schedule_date: int, );
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
