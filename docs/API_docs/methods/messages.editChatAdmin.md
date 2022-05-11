---
title: "messages.editChatAdmin"
description: "Make a user admin in a [basic group](https://core.telegram.org/api/channel#basic-groups)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_editChatAdmin.html
---
# Method: messages.editChatAdmin
[Back to methods index](index.html)



Make a user admin in a [basic group](https://core.telegram.org/api/channel#basic-groups).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) |  | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The user to make admin | Optional|
|is\_admin|[Bool](/API_docs/types/Bool.html) | Whether to make them admin | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->messages->editChatAdmin(chat_id: InputPeer, user_id: InputUser, is_admin: Bool, );
```

