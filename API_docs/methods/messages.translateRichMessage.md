# messages.translateRichMessage

> messages.translateRichMessage parameters, return type and example

[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|id|Array of [int](/API_docs/types/int.html) | Optional|
|text|Array of [InputRichMessage](/API_docs/types/InputRichMessage.html) | Optional|
|to\_lang|[string](/API_docs/types/string.html) | Optional|
|tone|[string](/API_docs/types/string.html) | Optional|


### Return type: [messages.TranslatedRichMessage](/API_docs/types/messages.TranslatedRichMessage.html)

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

$messages_TranslatedRichMessage = $MadelineProto->messages->translateRichMessage(peer: $InputPeer, id: [$int, $int], text: [$InputRichMessage, $InputRichMessage], to_lang: 'string', tone: 'string', );
```
