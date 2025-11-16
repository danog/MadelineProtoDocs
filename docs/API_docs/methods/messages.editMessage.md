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
|invert\_media|[Bool](/API_docs/types/Bool.html) | If set, any eventual webpage preview will be shown on top of the message instead of at the bottom. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Where was the message sent | Optional|
|id|[int](/API_docs/types/int.html) | ID of the message to edit | Optional|
|message|[string](/API_docs/types/string.html) | New message | Optional|
|media|[MessageMedia, Update, Message or InputMedia](/API_docs/types/InputMedia.html) | New attached media | Optional|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.html) | Reply markup for inline keyboards | Optional|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | [Message entities for styled text](https://core.telegram.org/api/entities) | Optional|
|parse\_mode| [string](/API_docs/types/string.html) | Whether to parse HTML or Markdown markup in the message| Optional |
|schedule\_date|[int](/API_docs/types/int.html) | Scheduled message date for [scheduled messages](https://core.telegram.org/api/scheduled-messages) | Optional|
|schedule\_repeat\_period|[int](/API_docs/types/int.html) |  | Optional|
|quick\_reply\_shortcut\_id|[int](/API_docs/types/int.html) | If specified, edits a [quick reply shortcut message, instead »](https://core.telegram.org/api/business#quick-reply-shortcuts). | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->editMessage(no_webpage: $Bool, invert_media: $Bool, peer: $InputPeer, id: $int, message: 'string', media: $InputMedia, reply_markup: $ReplyMarkup, entities: [$MessageEntity, $MessageEntity], parse_mode: 'string', schedule_date: $int, schedule_repeat_period: $int, quick_reply_shortcut_id: $int, );
```


## Usage of reply_markup

You can provide bot API reply_markup objects here.  



## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [Updates](../types/Updates.html) will be returned instead.



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

