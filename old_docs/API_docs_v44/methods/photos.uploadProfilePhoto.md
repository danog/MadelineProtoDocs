---
title: photos.uploadProfilePhoto
description: Updates current user profile photo.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/photos_uploadProfilePhoto.html
---
# Method: photos.uploadProfilePhoto
[Back to methods index](index.md)



Updates current user profile photo.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file|[File path or InputFile](../types/InputFile.md) | File saved in parts by means of [upload.saveFilePart](../methods/upload.saveFilePart.md) method | Optional|
|video|[File path or InputFile](../types/InputFile.md) |  | Optional|
|video\_start\_ts|[double](../types/double.md) |  | Optional|


### Return type: [photos.Photo](../types/photos.Photo.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$photos.Photo = $MadelineProto->photos->uploadProfilePhoto(['file' => InputFile, 'video' => InputFile, 'video_start_ts' => double, ]);
```

Or, if you're into Lua:

```lua
photos.Photo = photos.uploadProfilePhoto({file=InputFile, video=InputFile, video_start_ts=double, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|FILE_PARTS_INVALID|The number of file parts is invalid|
|400|IMAGE_PROCESS_FAILED|Failure while processing image|
|400|PHOTO_CROP_FILE_MISSING|Photo crop file missing|
|400|PHOTO_CROP_SIZE_SMALL|Photo is too small|
|400|PHOTO_EXT_INVALID|The extension of the photo is invalid|
|-503|Timeout|Timeout while fetching data|


