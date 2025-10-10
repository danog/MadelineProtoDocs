---
title: "users.getSavedMusicByID"
description: "Check if the passed songs are still pinned to the user's profile, or refresh the file references of songs pinned on a user's profile [see here »](https://core.telegram.org/api/profile#music) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/users_getSavedMusicByID.html
---
# Method: users.getSavedMusicByID
[Back to methods index](index.html)



Check if the passed songs are still pinned to the user's profile, or refresh the file references of songs pinned on a user's profile [see here »](https://core.telegram.org/api/profile#music) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The ID of the user. | Optional|
|documents|Array of [MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | The songs (here, `file_reference` can be empty to refresh file references). | Yes|


### Return type: [users.SavedMusic](/API_docs/types/users.SavedMusic.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$users_SavedMusic = $MadelineProto->users->getSavedMusicByID(id: $InputUser, documents: [$InputDocument, $InputDocument], );
```

