---
title: photos.updateProfilePhoto
description: Installs a previously uploaded photo as a profile photo.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/photos_updateProfilePhoto.html
---
# Method: photos.updateProfilePhoto
[Back to methods index](index.md)



Installs a previously uploaded photo as a profile photo.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[MessageMedia, Update, Message or InputPhoto](../types/InputPhoto.md) | Input photo | Optional|
|crop|[InputPhotoCrop](../types/InputPhotoCrop.md) |  | Yes|


### Return type: [UserProfilePhoto](../types/UserProfilePhoto.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$UserProfilePhoto = $MadelineProto->photos->updateProfilePhoto(['id' => InputPhoto, 'crop' => InputPhotoCrop, ]);
```

Or, if you're into Lua:

```lua
UserProfilePhoto = photos.updateProfilePhoto({id=InputPhoto, crop=InputPhotoCrop, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|FILE_PARTS_INVALID|The number of file parts is invalid|
|400|IMAGE_PROCESS_FAILED|Failure while processing image|
|400|LOCATION_INVALID|The provided location is invalid|
|400|PHOTO_CROP_SIZE_SMALL|Photo is too small|
|400|PHOTO_EXT_INVALID|The extension of the photo is invalid|
|400|PHOTO_ID_INVALID|Photo ID invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|-500|No workers running|Internal error|


