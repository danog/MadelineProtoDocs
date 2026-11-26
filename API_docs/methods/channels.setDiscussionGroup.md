# channels.setDiscussionGroup

> Associate a group to a channel as [discussion group](https://core.telegram.org/api/discussion) for that channel

[Back to methods index](index.html)



Associate a group to a channel as [discussion group](https://core.telegram.org/api/discussion) for that channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|broadcast|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Channel | Optional|
|group|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | [Discussion group](https://core.telegram.org/api/discussion) to associate to the channel | Optional|


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

$Bool = $MadelineProto->channels->setDiscussionGroup(broadcast: $InputChannel, group: $InputChannel, );
```
