---
title: "stories.editStory"
description: "Edit an uploaded [story](https://core.telegram.org/api/stories)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_editStory.html
---
# Method: stories.editStory
[Back to methods index](index.html)



Edit an uploaded [story](https://core.telegram.org/api/stories)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the story was posted. | Optional|
|id|[int](/API_docs/types/int.html) | ID of story to edit. | Optional|
|media|[MessageMedia, Update, Message or InputMedia](/API_docs/types/InputMedia.html) | If specified, replaces the story media. | Optional|
|media\_areas|Array of [MediaArea](/API_docs/types/MediaArea.html) | [Media areas](https://core.telegram.org/api/stories#media-areas) associated to the story, see [here »](https://core.telegram.org/api/stories#media-areas) for more info. | Optional|
|caption|[string](/API_docs/types/string.html) | If specified, replaces the story caption. | Optional|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | [Message entities for styled text in the caption](https://core.telegram.org/api/entities), if allowed by the [`stories_entities` client configuration parameter »](https://core.telegram.org/api/config#stories-entities). | Optional|
|parse\_mode| [string](/API_docs/types/string.html) | Whether to parse HTML or Markdown markup in the message| Optional |
|privacy\_rules|Array of [InputPrivacyRule](/API_docs/types/InputPrivacyRule.html) | If specified, alters the [privacy settings »](https://core.telegram.org/api/privacy) of the story, changing who can or can't view the story. | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->stories->editStory(peer: $InputPeer, id: $int, media: $InputMedia, media_areas: [$MediaArea, $MediaArea], caption: 'string', entities: [$MessageEntity, $MessageEntity], parse_mode: 'string', privacy_rules: [$InputPrivacyRule, $InputPrivacyRule], );
```


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

