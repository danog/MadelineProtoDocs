# channels.readMessageContents

> Mark [channel/supergroup](https://core.telegram.org/api/channel) message contents as read, emitting an [updateChannelReadMessagesContents](../constructors/updateChannelReadMessagesContents.html).

[Back to methods index](index.html)



Mark [channel/supergroup](https://core.telegram.org/api/channel) message contents as read, emitting an [updateChannelReadMessagesContents](../constructors/updateChannelReadMessagesContents.html).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | [Channel/supergroup](https://core.telegram.org/api/channel) | Optional|
|id|Array of [int](/API_docs/types/int.html) | IDs of messages whose contents should be marked as read | Yes|


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

$Bool = $MadelineProto->channels->readMessageContents(channel: $InputChannel, id: [$int, $int], );
```
