---
title: "inputBotInlineResultDocument"
description: "Document (media of any type except for photos)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineResultDocument  
[Back to constructors index](index.md)



Document (media of any type except for photos)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Yes|Result ID|
|type|[string](../types/string.md) | Yes|Result type (see [bot API docs](https://core.telegram.org/bots/api#inlinequeryresult))|
|title|[string](../types/string.md) | Optional|Result title|
|description|[string](../types/string.md) | Optional|Result description|
|document|[MessageMedia, Message, Update or InputDocument](../types/InputDocument.md) | Optional|Document to send|
|send\_message|[InputBotInlineMessage](../types/InputBotInlineMessage.md) | Yes|Message to send when the result is selected|



### Type: [InputBotInlineResult](../types/InputBotInlineResult.md)


### Example:

```php
$inputBotInlineResultDocument = ['_' => 'inputBotInlineResultDocument', 'id' => 'string', 'type' => 'string', 'title' => 'string', 'description' => 'string', 'document' => InputDocument, 'send_message' => InputBotInlineMessage];
```  
