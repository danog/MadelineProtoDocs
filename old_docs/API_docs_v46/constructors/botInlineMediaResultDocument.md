---
title: botInlineMediaResultDocument
description: Bot inline media result document
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMediaResultDocument  
[Back to constructors index](index.md)



Bot inline media result document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Yes|ID|
|type|[string](../types/string.md) | Yes|Type|
|document|[Document](../types/Document.md) | Optional|Document|
|send\_message|[BotInlineMessage](../types/BotInlineMessage.md) | Yes|Send message|



### Type: [BotInlineResult](../types/BotInlineResult.md)


### Example:

```php
$botInlineMediaResultDocument = ['_' => 'botInlineMediaResultDocument', 'id' => 'string', 'type' => 'string', 'document' => Document, 'send_message' => BotInlineMessage];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "botInlineMediaResultDocument", "id": "string", "type": "string", "document": Document, "send_message": BotInlineMessage}
```


Or, if you're into Lua:

```lua
botInlineMediaResultDocument={_='botInlineMediaResultDocument', id='string', type='string', document=Document, send_message=BotInlineMessage}

```


