---
title: "account.saveMusic"
description: "Adds or removes a song from the current user's profile [see here »](https://core.telegram.org/api/profile#music) for more info on the music tab of the profile page."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_saveMusic.html
---
# Method: account.saveMusic
[Back to methods index](index.html)



Adds or removes a song from the current user's profile [see here »](https://core.telegram.org/api/profile#music) for more info on the music tab of the profile page.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|unsave|[Bool](/API_docs/types/Bool.html) | If set, removes the song. | Optional|
|id|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | The song to add or remove; can be an already added song when reordering songs with `after_id`. Adding an already added song will never re-add it, only move it to the top of the song list (or after the song passed in `after_id`). | Optional|
|after\_id|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | If set, the song will be added after the passed song (must be already pinned on the profile). | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->account->saveMusic(unsave: $Bool, id: $InputDocument, after_id: $InputDocument, );
```

