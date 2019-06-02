---
title: photos.getUserPhotos
description: Get the profile photos of a user
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: photos.getUserPhotos  
[Back to methods index](index.md)


Get the profile photos of a user

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The user | Optional|
|offset|[int](../types/int.md) | Offset | Yes|
|max\_id|[long](../types/long.md) | Maximum ID of photo to return | Yes|
|limit|[int](../types/int.md) | Number of photos to return | Yes|


### Return type: [photos\_Photos](../types/photos_Photos.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$photos_Photos = $MadelineProto->photos->getUserPhotos(['user_id' => InputUser, 'offset' => int, 'max_id' => long, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
photos_Photos = photos.getUserPhotos({user_id=InputUser, offset=int, max_id=long, limit=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|MAX_ID_INVALID|The provided max ID is invalid|
|USER_ID_INVALID|The provided user ID is invalid|


