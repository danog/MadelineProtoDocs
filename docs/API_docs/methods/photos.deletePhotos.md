---
title: "photos.deletePhotos"
description: "Deletes profile photos."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/photos_deletePhotos.html
---
# Method: photos.deletePhotos
[Back to methods index](index.html)



Deletes profile photos.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [MessageMedia, Update, Message or InputPhoto](/API_docs/types/InputPhoto.html) | Input photos to delete | Yes|


### Return type: [Vector\_of\_long](/API_docs/types/long.html)

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
$Vector_of_long = $MadelineProto->photos->deletePhotos(id: [InputPhoto, InputPhoto], );
```

