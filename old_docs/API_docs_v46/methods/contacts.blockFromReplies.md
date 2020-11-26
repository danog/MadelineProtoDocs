---
title: contacts.blockFromReplies
description: contacts.blockFromReplies parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_blockFromReplies.html
---
# Method: contacts.blockFromReplies
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|delete\_message|[Bool](../types/Bool.md) | Optional|
|delete\_history|[Bool](../types/Bool.md) | Optional|
|report\_spam|[Bool](../types/Bool.md) | Optional|
|msg\_id|[int](../types/int.md) | Yes|


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

