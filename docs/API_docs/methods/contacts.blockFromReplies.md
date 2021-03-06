---
title: contacts.blockFromReplies
description: Stop getting notifications about [thread replies](https://core.telegram.org/api/threads) of a certain user in `@replies`
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_blockFromReplies.html
---
# Method: contacts.blockFromReplies
[Back to methods index](index.md)



Stop getting notifications about [thread replies](https://core.telegram.org/api/threads) of a certain user in `@replies`

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|delete\_message|[Bool](../types/Bool.md) | Whether to delete the specified message as well | Optional|
|delete\_history|[Bool](../types/Bool.md) | Whether to delete all `@replies` messages from this user as well | Optional|
|report\_spam|[Bool](../types/Bool.md) | Whether to also report this user for spam | Optional|
|msg\_id|[int](../types/int.md) | ID of the message in the [@replies](https://core.telegram.org/api/threads#replies) chat | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->contacts->blockFromReplies(['delete_message' => Bool, 'delete_history' => Bool, 'report_spam' => Bool, 'msg_id' => int, ]);
```

Or, if you're into Lua:

```lua
Updates = contacts.blockFromReplies({delete_message=Bool, delete_history=Bool, report_spam=Bool, msg_id=int, })
```

