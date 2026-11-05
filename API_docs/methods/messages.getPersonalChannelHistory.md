# messages.getPersonalChannelHistory

> messages.getPersonalChannelHistory parameters, return type and example

[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|limit|[int](/API_docs/types/int.html) | Optional|
|max\_id|[int](/API_docs/types/int.html) | Optional|
|min\_id|[int](/API_docs/types/int.html) | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | Optional|


### Return type: [messages.Messages](/API_docs/types/messages.Messages.html)

### Can users use this method: **NO**


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

$messages_Messages = $MadelineProto->messages->getPersonalChannelHistory(user_id: $InputUser, limit: $int, max_id: $int, min_id: $int, hash: [$long\|string, $long\|string], );
```
