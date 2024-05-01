---
title: "stories.sendStory"
description: "Uploads a [Telegram Story](https://core.telegram.org/api/stories)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stories_sendStory.html
---
# Method: stories.sendStory
[Back to methods index](index.html)



Uploads a [Telegram Story](https://core.telegram.org/api/stories).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|pinned|[Bool](/API_docs/types/Bool.html) | Whether to add the story to the profile automatically upon expiration. If not set, the story will only be added to the archive, see [here »](https://core.telegram.org/api/stories) for more info. | Optional|
|noforwards|[Bool](/API_docs/types/Bool.html) | If set, disables forwards, screenshots, and downloads. | Optional|
|fwd\_modified|[Bool](/API_docs/types/Bool.html) | Set this flag when reposting stories with `fwd_from_id`+`fwd_from_id`, if the `media` was modified before reposting. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer to send the story as. | Optional|
|media|[MessageMedia, Update, Message or InputMedia](/API_docs/types/InputMedia.html) | The story media. | Optional|
|media\_areas|Array of [MediaArea](/API_docs/types/MediaArea.html) | [Media areas](https://core.telegram.org/api/stories#media-areas) associated to the story, see [here »](https://core.telegram.org/api/stories#media-areas) for more info. | Optional|
|caption|[string](/API_docs/types/string.html) | Story caption. | Optional|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | [Message entities for styled text](https://core.telegram.org/api/entities), if allowed by the [`stories_entities` client configuration parameter »](https://core.telegram.org/api/config#stories-entities). | Optional|
|parse\_mode| [string](/API_docs/types/string.html) | Whether to parse HTML or Markdown markup in the message| Optional |
|privacy\_rules|Array of [InputPrivacyRule](/API_docs/types/InputPrivacyRule.html) | [Privacy rules](https://core.telegram.org/api/privacy) for the story, indicating who can or can't view the story. | Yes|
|period|[int](/API_docs/types/int.html) | Period after which the story is moved to archive (and to the profile if `pinned` is set), in seconds; must be one of `6 * 3600`, `12 * 3600`, `86400`, or `2 * 86400` for Telegram Premium users, and `86400` otherwise. | Optional|
|fwd\_from\_id|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | If set, indicates that this story is a repost of story with ID `fwd_from_story` posted by the peer in `fwd_from_id`. | Optional|
|fwd\_from\_story|[int](/API_docs/types/int.html) | If set, indicates that this story is a repost of story with ID `fwd_from_story` posted by the peer in `fwd_from_id`. | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->stories->sendStory(pinned: $Bool, noforwards: $Bool, fwd_modified: $Bool, peer: $InputPeer, media: $InputMedia, media_areas: [$MediaArea, $MediaArea], caption: 'string', entities: [$MessageEntity, $MessageEntity], parse_mode: 'string', privacy_rules: [$InputPrivacyRule, $InputPrivacyRule], period: $int, fwd_from_id: $InputPeer, fwd_from_story: $int, );
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

