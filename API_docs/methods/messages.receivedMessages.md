# messages.receivedMessages

> Confirms receipt of messages by a client, cancels PUSH-notification sending.

[Back to methods index](index.html)



Confirms receipt of messages by a client, cancels PUSH-notification sending.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|max\_id|[int](/API_docs/types/int.html) | Maximum message ID available in a client. | Optional|


### Return type: [Vector\_of\_ReceivedNotifyMessage](/API_docs/types/ReceivedNotifyMessage.html)

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

$Vector_of_ReceivedNotifyMessage = $MadelineProto->messages->receivedMessages(max_id: $int, );
```
