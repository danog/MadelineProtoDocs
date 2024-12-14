---
title: "photos.uploadContactProfilePhoto"
description: "Upload a custom profile picture for a contact, or suggest a new profile picture to a contact."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/photos_uploadContactProfilePhoto.html
---
# Method: photos.uploadContactProfilePhoto
[Back to methods index](index.html)



Upload a custom profile picture for a contact, or suggest a new profile picture to a contact.

The `file`, `video` and `video_emoji_markup` flags are mutually exclusive.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|suggest|[Bool](/API_docs/types/Bool.html) | If set, will send a [messageActionSuggestProfilePhoto](../constructors/messageActionSuggestProfilePhoto.html) service message to `user_id`, suggesting them to use the specified profile picture; otherwise, will set a personal profile picture for the user (only visible to the current user). | Optional|
|save|[Bool](/API_docs/types/Bool.html) | If set, removes a previously set personal profile picture (does not affect suggested profile pictures, to remove them simply deleted the [messageActionSuggestProfilePhoto](../constructors/messageActionSuggestProfilePhoto.html) service message with [messages.deleteMessages](../methods/messages.deleteMessages.html)). | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The contact | Optional|
|file|[File path or InputFile](/API_docs/types/InputFile.html) | Profile photo | Optional|
|video|[File path or InputFile](/API_docs/types/InputFile.html) | [Animated profile picture](https://core.telegram.org/api/files#animated-profile-pictures) video | Optional|
|video\_start\_ts|[double](/API_docs/types/double.html) | Floating point UNIX timestamp in seconds, indicating the frame of the video/sticker that should be used as static preview; can only be used if `video` or `video_emoji_markup` is set. | Optional|
|video\_emoji\_markup|[VideoSize](/API_docs/types/VideoSize.html) | Animated sticker profile picture, must contain either a [videoSizeEmojiMarkup](../constructors/videoSizeEmojiMarkup.html) or a [videoSizeStickerMarkup](../constructors/videoSizeStickerMarkup.html) constructor. | Optional|


### Return type: [photos.Photo](/API_docs/types/photos.Photo.html)

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

$photos_Photo = $MadelineProto->photos->uploadContactProfilePhoto(suggest: $Bool, save: $Bool, user_id: $InputUser, file: $InputFile, video: $InputFile, video_start_ts: $double, video_emoji_markup: $VideoSize, );
```

