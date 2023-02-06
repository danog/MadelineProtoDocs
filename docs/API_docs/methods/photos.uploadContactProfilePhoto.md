---
title: "photos.uploadContactProfilePhoto"
description: "photos.uploadContactProfilePhoto parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/photos_uploadContactProfilePhoto.html
---
# Method: photos.uploadContactProfilePhoto
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|suggest|[Bool](/API_docs/types/Bool.html) | Optional|
|save|[Bool](/API_docs/types/Bool.html) | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|file|[File path or InputFile](/API_docs/types/InputFile.html) | Optional|
|video|[File path or InputFile](/API_docs/types/InputFile.html) | Optional|
|video\_start\_ts|[double](/API_docs/types/double.html) | Optional|
|video\_emoji\_markup|[VideoSize](/API_docs/types/VideoSize.html) | Optional|


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

// PHP 8+ syntax, use an array on PHP 7.
$photos_Photo = $MadelineProto->photos->uploadContactProfilePhoto(suggest: Bool, save: Bool, user_id: InputUser, file: InputFile, video: InputFile, video_start_ts: double, video_emoji_markup: VideoSize, );
```

