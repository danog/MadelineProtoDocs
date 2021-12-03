---
title: photos.getUserPhotos
description: Returns the list of user photos.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/photos_getUserPhotos.html
---
# Method: photos.getUserPhotos
[Back to methods index](index.md)



Returns the list of user photos.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | User ID | Optional|
|offset|[int](../types/int.md) | Number of list elements to be skipped | Yes|
|max\_id|[int](../types/int.md) |  | Yes|
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

$photos_Photos = $MadelineProto->photos->getUserPhotos(['user_id' => InputUser, 'offset' => int, 'max_id' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
photos_Photos = photos.getUserPhotos({user_id=InputUser, offset=int, max_id=int, limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|MAX_ID_INVALID|The provided max ID is invalid|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|USER_ID_INVALID|The provided user ID is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|-503|Timeout|Timeout while fetching data|


