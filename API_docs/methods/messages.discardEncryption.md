# messages.discardEncryption

> You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling secret chats

[Back to methods index](index.html)



You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling secret chats

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|delete\_history|[Bool](/API_docs/types/Bool.html) | Whether to delete the entire chat history for the other user as well | Optional|
|chat\_id|[int](/API_docs/types/int.html) | Secret chat ID | Optional|


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

$Bool = $MadelineProto->messages->discardEncryption(delete_history: $Bool, chat_id: $int, );
```
