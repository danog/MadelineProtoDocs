# messages.composeMessageWithAI

> messages.composeMessageWithAI parameters, return type and example

[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|proofread|[Bool](/API_docs/types/Bool.html) | Optional|
|emojify|[Bool](/API_docs/types/Bool.html) | Optional|
|text|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|
|translate\_to\_lang|[string](/API_docs/types/string.html) | Optional|
|tone|[InputAiComposeTone](/API_docs/types/InputAiComposeTone.html) | Optional|


### Return type: [messages.ComposedMessageWithAI](/API_docs/types/messages.ComposedMessageWithAI.html)

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

$messages_ComposedMessageWithAI = $MadelineProto->messages->composeMessageWithAI(proofread: $Bool, emojify: $Bool, text: $TextWithEntities, translate_to_lang: 'string', tone: $InputAiComposeTone, );
```
