# account.getNotifyExceptions

> Returns list of chats with non-default notification settings

[Back to methods index](index.html)



Returns list of chats with non-default notification settings

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|compare\_sound|[Bool](/API_docs/types/Bool.html) | If set, chats with non-default sound will be returned | Optional|
|compare\_stories|[Bool](/API_docs/types/Bool.html) | If set, chats with non-default notification settings for stories will be returned | Optional|
|peer|[InputNotifyPeer](/API_docs/types/InputNotifyPeer.html) | If specified, only chats of the specified category will be returned | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->account->getNotifyExceptions(compare_sound: $Bool, compare_stories: $Bool, peer: $InputNotifyPeer, );
```
