---
title: "ephemeralMessage"
description: "ephemeralMessage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: ephemeralMessage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|out|[Bool](/API_docs/types/Bool.html) | Optional|
|welcome\_template|[Bool](/API_docs/types/Bool.html) | Optional|
|invert\_media|[Bool](/API_docs/types/Bool.html) | Optional|
|noforwards|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[int](/API_docs/types/int.html) | Yes|
|from\_id|[Peer](/API_docs/types/Peer.html) | Yes|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Optional|
|receiver\_id|[long](/API_docs/types/long.html) | Yes|
|top\_msg\_id|[int](/API_docs/types/int.html) | Optional|
|date|[int](/API_docs/types/int.html) | Yes|
|message|[string](/API_docs/types/string.html) | Yes|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|
|parse\_mode| [string](/API_docs/types/string.html) | Whether to parse HTML or Markdown markup in the message| Optional |
|media|[MessageMedia](/API_docs/types/MessageMedia.html) | Optional|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.html) | Optional|
|reply\_to|[MessageReplyHeader](/API_docs/types/MessageReplyHeader.html) | Optional|
|rich\_message|[RichMessage](/API_docs/types/RichMessage.html) | Optional|
|chat\_instance|[long](/API_docs/types/long.html) | Optional|
|anchor\_msg\_id|[int](/API_docs/types/int.html) | Optional|



### Type: [EphemeralMessage](/API_docs/types/EphemeralMessage.html)



## Usage of parse_mode:

Set parse_mode to html to enable HTML parsing of the message.  

Set parse_mode to Markdown to enable markdown parsing of the message.  

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
$ephemeralMessage = ['_' => 'ephemeralMessage', 'out' => Bool, 'welcome_template' => Bool, 'invert_media' => Bool, 'noforwards' => Bool, 'id' => int, 'from_id' => Peer, 'peer_id' => Peer, 'receiver_id' => long, 'top_msg_id' => int, 'date' => int, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]parse_mode: 'string', , 'media' => MessageMedia, 'reply_markup' => ReplyMarkup, 'reply_to' => MessageReplyHeader, 'rich_message' => RichMessage, 'chat_instance' => long, 'anchor_msg_id' => int];
```  
