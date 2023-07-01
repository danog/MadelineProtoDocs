---
title: "decryptedMessage"
description: "Contents of an encrypted message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessage\_45  
[Back to constructors index](/API_docs/constructors/index.html)



Contents of an encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ttl|[int](/API_docs/types/int.html) | Yes|Message lifetime. Has higher priority than [decryptedMessageActionSetMessageTTL](../constructors/decryptedMessageActionSetMessageTTL.html).<br>Parameter added in Layer 17.|
|message|[string](/API_docs/types/string.html) | Yes|Message text|
|media|[DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.html) | Optional|Media content|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|Message [entities](https://core.telegram.org/api/entities) for styled text (parameter added in layer 45)|
|parse\_mode| [string](/API_docs/types/string.html) | Whether to parse HTML or Markdown markup in the message| Optional |
|via\_bot\_name|[string](/API_docs/types/string.html) | Optional|Specifies the ID of the inline bot that generated the message (parameter added in layer 45)|
|reply\_to\_random\_id|[long](/API_docs/types/long.html) | Optional|Random message ID of the message this message replies to (parameter added in layer 45)|



### Type: [DecryptedMessage](/API_docs/types/DecryptedMessage.html)



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
<a href="tg://user?id=186785362">Mention by user id</a>
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
[Mention by user id](tg://user?id=186785362)
[👍](emoji:5368324170671202286)
[👍](tg://emoji?id=5368324170671202286)
```

MadelineProto supports all html entities supported by [html_entity_decode](http://php.net/manual/en/function.html-entity-decode.php).
### Example:

```
$decryptedMessage_45 = ['_' => 'decryptedMessage', 'ttl' => int, 'message' => 'string', 'media' => DecryptedMessageMedia, 'entities' => [MessageEntity, MessageEntity]parse_mode: 'string', , 'via_bot_name' => 'string', 'reply_to_random_id' => long];
```  
