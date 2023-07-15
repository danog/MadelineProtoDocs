---
title: "updateShortChatMessage"
description: "Shortened constructor containing info on one new incoming text message from a chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortChatMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Shortened constructor containing info on one new incoming text message from a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](/API_docs/types/Bool.html) | Optional|Whether the message is outgoing|
|mentioned|[Bool](/API_docs/types/Bool.html) | Optional|Whether we were mentioned in this message|
|media\_unread|[Bool](/API_docs/types/Bool.html) | Optional|Whether the message contains some **unread** mentions|
|silent|[Bool](/API_docs/types/Bool.html) | Optional|If true, the message is a silent message, no notifications should be triggered|
|id|[int](/API_docs/types/int.html) | Yes|ID of the message|
|from\_id|[long](/API_docs/types/long.html) | Yes|ID of the sender of the message|
|chat\_id|[long](/API_docs/types/long.html) | Yes|ID of the chat where the message was sent|
|message|[string](/API_docs/types/string.html) | Yes|Message|
|pts|[int](/API_docs/types/int.html) | Yes|[PTS](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.html) | Yes|[PTS count](https://core.telegram.org/api/updates)|
|date|[int](/API_docs/types/int.html) | Yes|[date](https://core.telegram.org/api/updates)|
|fwd\_from|[MessageFwdHeader](/API_docs/types/MessageFwdHeader.html) | Optional|Info about a forwarded message|
|via\_bot\_id|[long](/API_docs/types/long.html) | Optional|Info about the inline bot used to generate this message|
|reply\_to|[MessageReplyHeader](/API_docs/types/MessageReplyHeader.html) | Optional|Reply (thread) information|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|[Entities](https://core.telegram.org/api/entities) for styled text|
|parse\_mode| [string](/API_docs/types/string.html) | Whether to parse HTML or Markdown markup in the message| Optional |
|ttl\_period|[int](/API_docs/types/int.html) | Optional|Time To Live of the message, once updateShortChatMessage.date+updateShortChatMessage.ttl\_period === time(), the message will be deleted on the server, and must be deleted locally as well.|



### Type: [Updates](/API_docs/types/Updates.html)



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

You can also use normal markdown ([bot API MarkdownV2 syntax](https://core.telegram.org/bots/api#markdownv2-style)), note that to create mentions you can also use the `mention:` syntax like in html:  

```markdown
*bold \*text*
_italic \*text_
__underline__
~strikethrough~
||spoiler||
*bold _italic bold ~italic bold strikethrough ||italic bold strikethrough spoiler||~ __underline italic bold___ bold*
[inline URL](http://www.example.com/)
[inline mention of a user](tg://user?id=123456789)
![👍](tg://emoji?id=5368324170671202286)
\`inline fixed-width code\`
\`\`\`
pre-formatted fixed-width code block
\`\`\`
\`\`\`php
pre-formatted fixed-width code block written in the PHP programming language
\`\`\`

[Mention by username](mention:@danogentili)
[Mention by user id](mention:186785362)
[Mention by user id](tg://user?id=186785362)
[👍](emoji:5368324170671202286)
[👍](tg://emoji?id=5368324170671202286)
```

### Example:

```
$updateShortChatMessage = ['_' => 'updateShortChatMessage', 'out' => Bool, 'mentioned' => Bool, 'media_unread' => Bool, 'silent' => Bool, 'id' => int, 'from_id' => long, 'chat_id' => long, 'message' => 'string', 'pts' => int, 'pts_count' => int, 'date' => int, 'fwd_from' => MessageFwdHeader, 'via_bot_id' => long, 'reply_to' => MessageReplyHeader, 'entities' => [MessageEntity, MessageEntity]parse_mode: 'string', , 'ttl_period' => int];
```  
