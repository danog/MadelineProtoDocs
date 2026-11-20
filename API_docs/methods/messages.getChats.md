# messages.getChats

> Returns chat basic info on their IDs.

[Back to methods index](index.html)



Returns chat basic info on their IDs.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [long](/API_docs/types/long.html) | List of chat IDs | Yes|


### Return type: [messages.Chats](/API_docs/types/messages.Chats.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Chats = $MadelineProto->messages->getChats(id: [$long, $long], );
```
