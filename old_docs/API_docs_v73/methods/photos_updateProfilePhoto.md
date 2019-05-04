---
title: photos.updateProfilePhoto
description: Change the profile photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: photos.updateProfilePhoto  
[Back to methods index](index.md)


Change the profile photo

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[MessageMedia, Update, Message or InputPhoto](../types/InputPhoto.md) | The photo to use | Optional|


### Return type: [UserProfilePhoto](../types/UserProfilePhoto.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$UserProfilePhoto = $MadelineProto->photos->updateProfilePhoto(['id' => InputPhoto, ]);
```

Or, if you're into Lua:

```lua
UserProfilePhoto = photos.updateProfilePhoto({id=InputPhoto, })
```

