---
title: "contacts.blockFromReplies"
description: "Stop getting notifications about [thread replies](https://core.telegram.org/api/threads) of a certain user in `@replies`"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_blockFromReplies.html
---
# Method: contacts.blockFromReplies
[Back to methods index](index.html)



Stop getting notifications about [thread replies](https://core.telegram.org/api/threads) of a certain user in `@replies`

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|delete\_message|[Bool](/API_docs/types/Bool.html) | Whether to delete the specified message as well | Optional|
|delete\_history|[Bool](/API_docs/types/Bool.html) | Whether to delete all `@replies` messages from this user as well | Optional|
|report\_spam|[Bool](/API_docs/types/Bool.html) | Whether to also report this user for spam | Optional|
|msg\_id|[int](/API_docs/types/int.html) | ID of the message in the [@replies](https://core.telegram.org/api/threads#replies) chat | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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
$Updates = $MadelineProto->contacts->blockFromReplies(delete_message: Bool, delete_history: Bool, report_spam: Bool, msg_id: int, );
```

