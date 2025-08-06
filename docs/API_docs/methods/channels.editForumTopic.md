---
title: "channels.editForumTopic"
description: "Edit [forum topic](https://core.telegram.org/api/forum); requires [`manage_topics` rights](https://core.telegram.org/api/rights)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_editForumTopic.html
---
# Method: channels.editForumTopic
[Back to methods index](index.html)



Edit [forum topic](https://core.telegram.org/api/forum); requires [`manage_topics` rights](https://core.telegram.org/api/rights).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Supergroup | Optional|
|topic\_id|[int](/API_docs/types/int.html) | Topic ID | Optional|
|title|[string](/API_docs/types/string.html) | If present, will update the topic title (maximum UTF-8 length: 128). | Optional|
|icon\_emoji\_id|[long](/API_docs/types/long.html) | If present, updates the [custom emoji](https://core.telegram.org/api/custom-emoji) used as topic icon. [Telegram Premium](https://core.telegram.org/api/premium) users can use any custom emoji, other users can only use the custom emojis contained in the [inputStickerSetEmojiDefaultTopicIcons](../constructors/inputStickerSetEmojiDefaultTopicIcons.html) emoji pack. Pass 0 to switch to the fallback topic icon. | Optional|
|closed|[Bool](/API_docs/types/Bool.html) | If present, will update the open/closed status of the topic. | Optional|
|hidden|[Bool](/API_docs/types/Bool.html) | If present, will hide/unhide the topic (only valid for the "General" topic, `id=1`). | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->channels->editForumTopic(channel: $InputChannel, topic_id: $int, title: 'string', icon_emoji_id: $long, closed: $Bool, hidden: $Bool, );
```

