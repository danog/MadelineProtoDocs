# messages.getBotWidgetQueryAnswer

> messages.getBotWidgetQueryAnswer parameters, return type and example

[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Optional|
|query\_type|[WidgetQueryType](/API_docs/types/WidgetQueryType.html) | Yes|
|data|[bytes](/API_docs/types/bytes.html) | Yes|


### Return type: [messages.BotWidgetQueryAnswer](/API_docs/types/messages.BotWidgetQueryAnswer.html)

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

$messages_BotWidgetQueryAnswer = $MadelineProto->messages->getBotWidgetQueryAnswer(peer: $InputPeer, msg_id: $int, query_type: $WidgetQueryType, data: 'bytes', );
```
