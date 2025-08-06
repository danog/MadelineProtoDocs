---
title: "channels.createForumTopic"
description: "Create a [forum topic](https://core.telegram.org/api/forum); requires [`manage_topics` rights](https://core.telegram.org/api/rights)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_createForumTopic.html
---
# Method: channels.createForumTopic
[Back to methods index](index.html)



Create a [forum topic](https://core.telegram.org/api/forum); requires [`manage_topics` rights](https://core.telegram.org/api/rights).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | [The forum](https://core.telegram.org/api/forum) | Optional|
|title|[string](/API_docs/types/string.html) | Topic title (maximum UTF-8 length: 128) | Optional|
|icon\_color|[int](/API_docs/types/int.html) | If no custom emoji icon is specified, specifies the color of the fallback topic icon (RGB), one of `0x6FB9F0`, `0xFFD67E`, `0xCB86DB`, `0x8EEE98`, `0xFF93B2`, or `0xFB6F5F`. | Optional|
|icon\_emoji\_id|[long](/API_docs/types/long.html) | ID of the [custom emoji](https://core.telegram.org/api/custom-emoji) used as topic icon. [Telegram Premium](https://core.telegram.org/api/premium) users can use any custom emoji, other users can only use the custom emojis contained in the [inputStickerSetEmojiDefaultTopicIcons](../constructors/inputStickerSetEmojiDefaultTopicIcons.html) emoji pack. | Optional|
|send\_as|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Create the topic as the specified peer | Optional|


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

$Updates = $MadelineProto->channels->createForumTopic(channel: $InputChannel, title: 'string', icon_color: $int, icon_emoji_id: $long, send_as: $InputPeer, );
```

