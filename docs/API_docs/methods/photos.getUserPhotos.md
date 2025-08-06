---
title: "photos.getUserPhotos"
description: "Returns the list of user photos."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/photos_getUserPhotos.html
---
# Method: photos.getUserPhotos
[Back to methods index](index.html)



Returns the list of user photos.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | User ID | Optional|
|offset|[int](/API_docs/types/int.html) | Number of list elements to be skipped | Optional|
|max\_id|[long](/API_docs/types/long.html) | If a positive value was transferred, the method will return only photos with IDs less than the set one. This parameter is often useful when [refetching file references »](https://core.telegram.org/api/file_reference), as in conjuction with `limit=1` and `offset=-1` the [photo](../constructors/photo.html) object with the `id` specified in `max_id` can be fetched. | Yes|
|limit|[int](/API_docs/types/int.html) | Number of list elements to be returned | Optional|


### Return type: [photos.Photos](/API_docs/types/photos.Photos.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$photos_Photos = $MadelineProto->photos->getUserPhotos(user_id: $InputUser, offset: $int, max_id: $long, limit: $int, );
```

