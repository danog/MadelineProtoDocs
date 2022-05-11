---
title: "channels.editAdmin"
description: "Modify the admin rights of a user in a [supergroup/channel](https://core.telegram.org/api/channel)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_editAdmin.html
---
# Method: channels.editAdmin
[Back to methods index](index.html)



Modify the admin rights of a user in a [supergroup/channel](https://core.telegram.org/api/channel).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | The [supergroup/channel](https://core.telegram.org/api/channel). | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The ID of the user whose admin rights should be modified | Optional|
|admin\_rights|[ChatAdminRights](/API_docs/types/ChatAdminRights.html) | The admin rights | Yes|
|rank|[string](/API_docs/types/string.html) | Indicates the role (rank) of the admin in the group: just an arbitrary string | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Updates = $MadelineProto->channels->editAdmin(channel: InputChannel, user_id: InputUser, admin_rights: ChatAdminRights, rank: 'string', );
```

