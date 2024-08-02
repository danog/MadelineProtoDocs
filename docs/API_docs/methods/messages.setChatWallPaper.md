---
title: "messages.setChatWallPaper"
description: "Set a custom [wallpaper »](https://core.telegram.org/api/wallpapers) in a specific private chat with another user."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setChatWallPaper.html
---
# Method: messages.setChatWallPaper
[Back to methods index](index.html)



Set a custom [wallpaper »](https://core.telegram.org/api/wallpapers) in a specific private chat with another user.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|for\_both|[Bool](/API_docs/types/Bool.html) | Only for [Premium](https://core.telegram.org/api/premium) users, sets the specified wallpaper for both users of the chat, without requiring confirmation from the other user. | Optional|
|revert|[Bool](/API_docs/types/Bool.html) | If we don't like the new wallpaper the other user of the chat has chosen for us using the `for_both` flag, we can re-set our previous wallpaper just on our side using this flag. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The private chat where the wallpaper will be set | Optional|
|wallpaper|[InputWallPaper](/API_docs/types/InputWallPaper.html) | The [wallpaper »](https://core.telegram.org/api/wallpapers), obtained as described in the [wallpaper documentation »](https://core.telegram.org/api/wallpapers#uploading-wallpapers); must **not** be provided when installing a wallpaper obtained from a [messageActionSetChatWallPaper](../constructors/messageActionSetChatWallPaper.html) service message (`id` must be provided, instead). | Optional|
|settings|[WallPaperSettings](/API_docs/types/WallPaperSettings.html) | Wallpaper settings, obtained as described in the [wallpaper documentation »](https://core.telegram.org/api/wallpapers#uploading-wallpapers) or from [messageActionSetChatWallPaper](../constructors/messageActionSetChatWallPaper.html).`wallpaper`.`settings`. | Optional|
|id|[int](/API_docs/types/int.html) | If the wallpaper was obtained from a [messageActionSetChatWallPaper](../constructors/messageActionSetChatWallPaper.html) service message, must contain the ID of that message. | Optional|


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

$Updates = $MadelineProto->messages->setChatWallPaper(for_both: $Bool, revert: $Bool, peer: $InputPeer, wallpaper: $InputWallPaper, settings: $WallPaperSettings, id: $int, );
```

