---
title: "channels.updateColor"
description: "Update the [accent color and background custom emoji »](https://core.telegram.org/api/colors) of a channel."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_updateColor.html
---
# Method: channels.updateColor
[Back to methods index](index.html)



Update the [accent color and background custom emoji »](https://core.telegram.org/api/colors) of a channel.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|for\_profile|[Bool](/API_docs/types/Bool.html) | Whether to change the accent color emoji pattern of the profile page; otherwise, the accent color and emoji pattern of messages will be changed. <br>Channels can change both message and profile palettes; supergroups can only change the profile palette, of course after reaching the [appropriate boost level](https://core.telegram.org/api/colors). | Optional|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Channel whose accent color should be changed. | Optional|
|color|[int](/API_docs/types/int.html) | [ID of the accent color palette »](https://core.telegram.org/api/colors) to use (not RGB24, see [here »](https://core.telegram.org/api/colors) for more info); if not set, the default palette is used. | Optional|
|background\_emoji\_id|[long](/API_docs/types/long.html) | Custom emoji ID used in the accent color pattern. | Optional|


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

$Updates = $MadelineProto->channels->updateColor(for_profile: $Bool, channel: $InputChannel, color: $int, background_emoji_id: $long, );
```

