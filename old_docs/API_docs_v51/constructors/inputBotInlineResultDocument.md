---
title: inputBotInlineResultDocument
description: inputBotInlineResultDocument attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineResultDocument  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[string](../types/string.md) | Yes|
|type|[string](../types/string.md) | Yes|
|title|[string](../types/string.md) | Optional|
|description|[string](../types/string.md) | Optional|
|document|[MessageMedia, Message, Update or InputDocument](../types/InputDocument.md) | Optional|
|send\_message|[InputBotInlineMessage](../types/InputBotInlineMessage.md) | Yes|



### Type: [InputBotInlineResult](../types/InputBotInlineResult.md)


### Example:

```php
$inputBotInlineResultDocument = ['_' => 'inputBotInlineResultDocument', 'id' => 'string', 'type' => 'string', 'title' => 'string', 'description' => 'string', 'document' => InputDocument, 'send_message' => InputBotInlineMessage];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputBotInlineResultDocument", "id": "string", "type": "string", "title": "string", "description": "string", "document": InputDocument, "send_message": InputBotInlineMessage}
```


Or, if you're into Lua:

```lua
inputBotInlineResultDocument={_='inputBotInlineResultDocument', id='string', type='string', title='string', description='string', document=InputDocument, send_message=InputBotInlineMessage}

```


