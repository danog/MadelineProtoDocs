---
title: "storyItem"
description: "Represents a story."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyItem  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [story](https://core.telegram.org/api/stories).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](/API_docs/types/Bool.html) | Optional|Whether this story is pinned on the user's profile|
|public|[Bool](/API_docs/types/Bool.html) | Optional|Whether this story is public and can be viewed by everyone|
|close\_friends|[Bool](/API_docs/types/Bool.html) | Optional|Whether this story can only be viewed by [our close friends, see here »](https://core.telegram.org/api/privacy) for more info|
|min|[Bool](/API_docs/types/Bool.html) | Optional|Full information about this story was omitted for space and performance reasons; use [stories.getStoriesByID](../methods/stories.getStoriesByID.html) to fetch full info about this story when and if needed.|
|noforwards|[Bool](/API_docs/types/Bool.html) | Optional|Whether this story is [protected](https://telegram.org/blog/protected-content-delete-by-date-and-more) and thus cannot be forwarded; clients should also prevent users from saving attached media (i.e. videos should only be streamed, photos should be kept in RAM, et cetera).|
|edited|[Bool](/API_docs/types/Bool.html) | Optional|Indicates whether the story was edited.|
|contacts|[Bool](/API_docs/types/Bool.html) | Optional|Whether this story can only be viewed by our contacts|
|selected\_contacts|[Bool](/API_docs/types/Bool.html) | Optional|Whether this story can only be viewed by a select list of our contacts|
|out|[Bool](/API_docs/types/Bool.html) | Optional|indicates whether we sent this story.|
|id|[int](/API_docs/types/int.html) | Yes|ID of the story.|
|date|[int](/API_docs/types/int.html) | Yes|When was the story posted.|
|from\_id|[Peer](/API_docs/types/Peer.html) | Optional|Sender of the story.|
|fwd\_from|[StoryFwdHeader](/API_docs/types/StoryFwdHeader.html) | Optional|For [reposted stories »](https://core.telegram.org/api/stories#reposting-stories), contains info about the original story.|
|expire\_date|[int](/API_docs/types/int.html) | Yes|When does the story expire.|
|caption|[string](/API_docs/types/string.html) | Optional|Story caption.|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|[Message entities for styled text](https://core.telegram.org/api/entities)|
|parse\_mode| [string](/API_docs/types/string.html) | Whether to parse HTML or Markdown markup in the message| Optional |
|media|[MessageMedia](/API_docs/types/MessageMedia.html) | Optional|Story media.|
|media\_areas|Array of [MediaArea](/API_docs/types/MediaArea.html) | Optional|List of media areas, see [here »](https://core.telegram.org/api/stories#media-areas) for more info on media areas.|
|privacy|Array of [PrivacyRule](/API_docs/types/PrivacyRule.html) | Optional|[Privacy rules](https://core.telegram.org/api/privacy) indicating who can and can't view this story|
|views|[StoryViews](/API_docs/types/StoryViews.html) | Optional|View date and reaction information|
|sent\_reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|The reaction we sent.|
|albums|Array of [int](/API_docs/types/int.html) | Optional|[Albums](https://core.telegram.org/api/stories#story-albums) this story is part of.|



### Type: [StoryItem](/API_docs/types/StoryItem.html)



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
$storyItem = ['_' => 'storyItem', 'pinned' => Bool, 'public' => Bool, 'close_friends' => Bool, 'min' => Bool, 'noforwards' => Bool, 'edited' => Bool, 'contacts' => Bool, 'selected_contacts' => Bool, 'out' => Bool, 'id' => int, 'date' => int, 'from_id' => Peer, 'fwd_from' => StoryFwdHeader, 'expire_date' => int, 'caption' => 'string', 'entities' => [MessageEntity, MessageEntity]parse_mode: 'string', , 'media' => MessageMedia, 'media_areas' => [MediaArea, MediaArea], 'privacy' => [PrivacyRule, PrivacyRule], 'views' => StoryViews, 'sent_reaction' => Reaction, 'albums' => [int, int]];
```  
