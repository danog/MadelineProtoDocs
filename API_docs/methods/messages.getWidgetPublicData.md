# messages.getWidgetPublicData

> messages.getWidgetPublicData parameters, return type and example

[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | Optional|


### Return type: [messages.WidgetPublicData](/API_docs/types/messages.WidgetPublicData.html)

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

$messages_WidgetPublicData = $MadelineProto->messages->getWidgetPublicData(peer: $InputPeer, msg_id: $int, hash: [$long\|string, $long\|string], );
```
