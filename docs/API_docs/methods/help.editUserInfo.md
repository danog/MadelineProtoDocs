---
title: help.editUserInfo
description: Internal use
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_editUserInfo.html
---
# Method: help.editUserInfo
[Back to methods index](index.md)



Internal use

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | User | Optional|
|message|[string](../types/string.md) | Message | Yes|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | [Message entities for styled text](https://core.telegram.org/api/entities) | Yes|
|parse\_mode| [string](../types/string.md) | Whether to parse HTML or Markdown markup in the message| Optional |


### Return type: [help.UserInfo](../types/help.UserInfo.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_UserInfo = $MadelineProto->help->editUserInfo(['user_id' => InputUser, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity], 'parse_mode' => 'string', ]);
```

Or, if you're into Lua:

```lua
help_UserInfo = help.editUserInfo({user_id=InputUser, message='string', entities={MessageEntity}, parseMode='string', })
```


## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [help.UserInfo](../types/help.UserInfo.md) will be returned instead.



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
<pre language="json">Pre tags can have a language attribute</pre>
```

You can also use normal markdown, note that to create mentions you must use the `mention:` syntax like in html:  

```markdown
[Mention by username](mention:@danogentili)
[Mention by user id](mention:186785362)
```

MadelineProto supports all html entities supported by [html_entity_decode](http://php.net/manual/en/function.html-entity-decode.php).
