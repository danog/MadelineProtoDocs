---
title: photos.getUserPhotos
description: Returns the list of user photos.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: photos.getUserPhotos  
[Back to methods index](index.md)


Returns the list of user photos.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | User ID | Optional|
|offset|[int](../types/int.md) | Number of list elements to be skipped | Yes|
|max\_id|[long](../types/long.md) | If a positive value was transferred, the method will return only photos with IDs less than the set one | Yes|
|limit|[int](../types/int.md) | Number of list elements to be returned | Yes|


### Return type: [photos.Photos](../types/photos.Photos.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$photos.Photos = $MadelineProto->photos->getUserPhotos(['user_id' => InputUser, 'offset' => int, 'max_id' => long, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
photos.Photos = photos.getUserPhotos({user_id=InputUser, offset=int, max_id=long, limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MAX_ID_INVALID|The provided max ID is invalid|
|400|USER_ID_INVALID|The provided user ID is invalid|


