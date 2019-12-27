---
title: photos.deletePhotos
description: Deletes profile photos.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: photos.deletePhotos  
[Back to methods index](index.md)


Deletes profile photos.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [MessageMedia, Update, Message or InputPhoto](../types/InputPhoto.md) | The profile photos to delete | Yes|


### Return type: [Vector\_of\_long](../types/long.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_long = $MadelineProto->photos->deletePhotos(['id' => [InputPhoto, InputPhoto], ]);
```

Or, if you're into Lua:

```lua
Vector_of_long = photos.deletePhotos({id={InputPhoto}, })
```

