---
title: "messages.sendMedia"
description: "Send a media"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendMedia.html
---
# Method: messages.sendMedia
[Back to methods index](index.html)



Send a media

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](/API_docs/types/Bool.html) | Send message silently (no notification should be triggered) | Optional|
|background|[Bool](/API_docs/types/Bool.html) | Send message in background | Optional|
|clear\_draft|[Bool](/API_docs/types/Bool.html) | Clear the draft | Optional|
|noforwards|[Bool](/API_docs/types/Bool.html) | Only for bots, disallows forwarding and saving of the messages, even if the destination chat doesn't have [content protection](https://telegram.org/blog/protected-content-delete-by-date-and-more) enabled | Optional|
|update\_stickersets\_order|[Bool](/API_docs/types/Bool.html) | Whether to move used stickersets to top, [see here for more info on this flag »](https://core.telegram.org/api/stickers#recent-stickersets) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Destination | Optional|
|reply\_to\_msg\_id|[int](/API_docs/types/int.html) | Message ID to which this message should reply to | Optional|
|top\_msg\_id|[int](/API_docs/types/int.html) | This field must contain the topic ID **only** when replying to messages in [forum topics](https://core.telegram.org/api/forum#forum-topics) different from the "General" topic (i.e. `reply_to_msg_id` is set and `reply_to_msg_id != topicID` and `topicID != 1`). <br>If the replied-to message is deleted before the method finishes execution, the value in this field will be used to send the message to the correct topic, instead of the "General" topic. | Optional|
|media|[MessageMedia, Update, Message or InputMedia](/API_docs/types/InputMedia.html) | Attached media | Optional|
|message|[string](/API_docs/types/string.html) | Caption | Yes|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.html) | Reply markup for bot keyboards | Optional|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Message [entities](https://core.telegram.org/api/entities) for styled text | Optional|
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

$Updates = $MadelineProto->messages->sendMedia(silent: Bool, background: Bool, clear_draft: Bool, noforwards: Bool, update_stickersets_order: Bool, peer: InputPeer, reply_to_msg_id: int, top_msg_id: int, media: InputMedia, message: 'string', reply_markup: ReplyMarkup, entities: [MessageEntity, MessageEntity], parse_mode: 'string', schedule_date: int, send_as: InputPeer, );
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
Custom emoji: <emoji id="5368324170671202286">👍</emoji>
Custom emoji: <tg-emoji emoji-id="5368324170671202286">👍</tg-emoji>
<pre language="json">Pre tags can have a language attribute</pre>
<spoiler>Spoiler</spoiler>
<tg-spoiler>Spoiler</tg-spoiler>
```

You can also use normal markdown, note that to create mentions you must use the `mention:` syntax like in html:  

```markdown
[Mention by username](mention:@danogentili)
[Mention by user id](mention:186785362)
[👍](emoji:5368324170671202286)
[👍](tg://emoji?id=5368324170671202286)
```

MadelineProto supports all html entities supported by [html_entity_decode](http://php.net/manual/en/function.html-entity-decode.php).
