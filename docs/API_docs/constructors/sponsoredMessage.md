---
title: "sponsoredMessage"
description: "A sponsored message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sponsoredMessage  
[Back to constructors index](/API_docs/constructors/index.html)



A [sponsored message](https://core.telegram.org/api/sponsored-messages).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|recommended|[Bool](/API_docs/types/Bool.html) | Optional|Whether the message needs to be labeled as "recommended" instead of "sponsored"|
|can\_report|[Bool](/API_docs/types/Bool.html) | Optional|Whether this message can be [reported as specified here »](https://core.telegram.org/api/sponsored-messages#reporting-sponsored-messages).|
|random\_id|[bytes](/API_docs/types/bytes.html) | Yes|Message ID|
|url|[string](/API_docs/types/string.html) | Yes|Contains the URL to open when the user clicks on the sponsored message.|
|title|[string](/API_docs/types/string.html) | Yes|Contains the title of the sponsored message.|
|message|[string](/API_docs/types/string.html) | Yes|Sponsored message|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|[Message entities for styled text](https://core.telegram.org/api/entities) in `message`.|
|parse\_mode| [string](/API_docs/types/string.html) | Whether to parse HTML or Markdown markup in the message| Optional |
|photo|[Photo](/API_docs/types/Photo.html) | Optional|If set, contains a custom profile photo bubble that should be displayed for the sponsored message, like for messages sent in groups.|
|media|[MessageMedia](/API_docs/types/MessageMedia.html) | Optional|If set, contains some media.|
|color|[PeerColor](/API_docs/types/PeerColor.html) | Optional|If set, the sponsored message should use the [message accent color »](https://core.telegram.org/api/colors) specified in `color`.|
|button\_text|[string](/API_docs/types/string.html) | Yes|Label of the sponsored message button.|
|sponsor\_info|[string](/API_docs/types/string.html) | Optional|If set, contains additional information about the sponsor to be shown along with the message.|
|additional\_info|[string](/API_docs/types/string.html) | Optional|If set, contains additional information about the sponsored message to be shown along with the message.|
|min\_display\_duration|[int](/API_docs/types/int.html) | Optional|
|max\_display\_duration|[int](/API_docs/types/int.html) | Optional|



### Type: [SponsoredMessage](/API_docs/types/SponsoredMessage.html)



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
$sponsoredMessage = ['_' => 'sponsoredMessage', 'recommended' => Bool, 'can_report' => Bool, 'random_id' => 'bytes', 'url' => 'string', 'title' => 'string', 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]parse_mode: 'string', , 'photo' => Photo, 'media' => MessageMedia, 'color' => PeerColor, 'button_text' => 'string', 'sponsor_info' => 'string', 'additional_info' => 'string', 'min_display_duration' => int, 'max_display_duration' => int];
```  
