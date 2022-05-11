---
title: "photos.updateProfilePhoto"
description: "Installs a previously uploaded photo as a profile photo."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/photos_updateProfilePhoto.html
---
# Method: photos.updateProfilePhoto
[Back to methods index](index.html)



Installs a previously uploaded photo as a profile photo.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[MessageMedia, Update, Message or InputPhoto](/API_docs/types/InputPhoto.html) | Input photo | Optional|


### Return type: [photos.Photo](/API_docs/types/photos.Photo.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$photos_Photo = $MadelineProto->photos->updateProfilePhoto(id: InputPhoto, );
```

