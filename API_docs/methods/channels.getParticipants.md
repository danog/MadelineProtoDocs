# channels.getParticipants

> Get the participants of a [supergroup/channel](https://core.telegram.org/api/channel)

[Back to methods index](index.html)



Get the participants of a [supergroup/channel](https://core.telegram.org/api/channel)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Channel | Optional|
|filter|[ChannelParticipantsFilter](/API_docs/types/ChannelParticipantsFilter.html) | Which participant types to fetch | Yes|
|offset|[int](/API_docs/types/int.html) | [Offset](https://core.telegram.org/api/offsets) | Optional|
|limit|[int](/API_docs/types/int.html) | [Limit](https://core.telegram.org/api/offsets) | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash](https://core.telegram.org/api/offsets) | Optional|


### Return type: [channels.ChannelParticipants](/API_docs/types/channels.ChannelParticipants.html)

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

$channels_ChannelParticipants = $MadelineProto->channels->getParticipants(channel: $InputChannel, filter: $ChannelParticipantsFilter, offset: $int, limit: $int, hash: [$long\|string, $long\|string], );
```
