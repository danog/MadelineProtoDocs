---
title: "photos.uploadProfilePhoto"
description: "Updates current user profile photo."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/photos_uploadProfilePhoto.html
---
# Method: photos.uploadProfilePhoto
[Back to methods index](index.html)



Updates current user profile photo.

The `file`, `video` and `video_emoji_markup` flags are mutually exclusive.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|fallback|[Bool](/API_docs/types/Bool.html) | If set, the chosen profile photo will be shown to users that can't display your main profile photo due to your privacy settings. | Optional|
|bot|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Can contain info of a bot we own, to change the profile photo of that bot, instead of the current user. | Optional|
|file|[File path or InputFile](/API_docs/types/InputFile.html) | Profile photo | Optional|
|video|[File path or InputFile](/API_docs/types/InputFile.html) | [Animated profile picture](https://core.telegram.org/api/files#animated-profile-pictures) video | Optional|
|video\_start\_ts|[double](/API_docs/types/double.html) | Floating point UNIX timestamp in seconds, indicating the frame of the video/sticker that should be used as static preview; can only be used if `video` or `video_emoji_markup` is set. | Optional|
|video\_emoji\_markup|[VideoSize](/API_docs/types/VideoSize.html) | Animated sticker profile picture, must contain either a [videoSizeEmojiMarkup](../constructors/videoSizeEmojiMarkup.html) or a [videoSizeStickerMarkup](../constructors/videoSizeStickerMarkup.html) constructor. | Optional|


### Return type: [photos.Photo](/API_docs/types/photos.Photo.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$photos_Photo = $MadelineProto->photos->uploadProfilePhoto(fallback: Bool, bot: InputUser, file: InputFile, video: InputFile, video_start_ts: double, video_emoji_markup: VideoSize, );
```

