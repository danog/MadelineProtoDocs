---
title: "help.deepLinkInfo"
description: "Deep link info, see the here for more details"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_deepLinkInfo.html
---
# Constructor: help.deepLinkInfo  
[Back to constructors index](/API_docs/constructors/index.html)



Deep link info, see [the here for more details](https://core.telegram.org/api/links#unsupported-links)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|update\_app|[Bool](/API_docs/types/Bool.html) | Optional|An update of the app is required to parse this link|
|message|[string](/API_docs/types/string.html) | Yes|Message to show to the user|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|[Message entities for styled text](https://core.telegram.org/api/entities)|
|parse\_mode| [string](/API_docs/types/string.html) | Whether to parse HTML or Markdown markup in the message| Optional |



### Type: [help.DeepLinkInfo](/API_docs/types/help.DeepLinkInfo.html)



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
$help_deepLinkInfo = ['_' => 'help.deepLinkInfo', 'update_app' => Bool, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]parse_mode: 'string', ];
```  
