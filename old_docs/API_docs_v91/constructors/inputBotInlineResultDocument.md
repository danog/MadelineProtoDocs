---
title: inputBotInlineResultDocument
description: Bot inline result document
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineResultDocument  
[Back to constructors index](index.md)



Bot inline result document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Yes|ID|
|type|[string](../types/string.md) | Yes|Type|
|title|[string](../types/string.md) | Optional|Title|
|description|[string](../types/string.md) | Optional|Description|
|document|[MessageMedia, Message, Update or InputDocument](../types/InputDocument.md) | Optional|Document|
|send\_message|[InputBotInlineMessage](../types/InputBotInlineMessage.md) | Yes|Message to send|



### Type: [InputBotInlineResult](../types/InputBotInlineResult.md)


### Example:

```php
$inputBotInlineResultDocument = ['_' => 'inputBotInlineResultDocument', 'id' => 'string', 'type' => 'string', 'title' => 'string', 'description' => 'string', 'document' => InputDocument, 'send_message' => InputBotInlineMessage];
```  


Or, if you're into Lua:

```lua
inputBotInlineResultDocument={_='inputBotInlineResultDocument', id='string', type='string', title='string', description='string', document=InputDocument, send_message=InputBotInlineMessage}

```


