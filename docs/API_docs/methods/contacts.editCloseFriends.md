---
title: "contacts.editCloseFriends"
description: "Edit the [close friends list, see here »](https://core.telegram.org/api/privacy) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_editCloseFriends.html
---
# Method: contacts.editCloseFriends
[Back to methods index](index.html)



Edit the [close friends list, see here »](https://core.telegram.org/api/privacy) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [long](/API_docs/types/long.html) | Full list of user IDs of close friends, see [here](https://core.telegram.org/api/privacy) for more info. | Yes|


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

$Bool = $MadelineProto->contacts->editCloseFriends(id: [$long, $long], );
```

