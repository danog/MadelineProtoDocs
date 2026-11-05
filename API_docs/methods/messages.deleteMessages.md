# messages.deleteMessages

> Deletes messages by their identifiers.

[Back to methods index](index.html)



Deletes messages by their identifiers.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|revoke|[Bool](/API_docs/types/Bool.html) | Whether to delete messages for all participants of the chat | Optional|
|id|Array of [int](/API_docs/types/int.html) | Message ID list | Yes|


### Return type: [messages.AffectedMessages](/API_docs/types/messages.AffectedMessages.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_AffectedMessages = $MadelineProto->messages->deleteMessages(revoke: $Bool, id: [$int, $int], );
```
