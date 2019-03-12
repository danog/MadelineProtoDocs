---
title: photos.deletePhotos
description: Delete profile photos
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: photos.deletePhotos  
[Back to methods index](index.md)


Delete profile photos

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [MessageMedia, Update, Message or InputPhoto](../types/InputPhoto.md) | The profile photos to delete | Yes|


### Return type: [Vector\_of\_long](../types/long.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_long = $MadelineProto->photos->deletePhotos(['id' => [InputPhoto, InputPhoto], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/photos.deletePhotos`

Parameters:

id - Json encoded  array of InputPhoto




Or, if you're into Lua:

```lua
Vector_of_long = photos.deletePhotos({id={InputPhoto}, })
```

