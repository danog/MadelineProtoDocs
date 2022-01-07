---
title: "inputBotInlineResultPhoto"
description: "Photo"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineResultPhoto  
[Back to constructors index](/API_docs/constructors/index.md)



Photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](/API_docs/types/string.md) | Yes|Result ID|
|type|[string](/API_docs/types/string.md) | Yes|Result type (see [bot API docs](https://core.telegram.org/bots/api#inlinequeryresult))|
|photo|[MessageMedia, Message, Update or InputPhoto](/API_docs/types/InputPhoto.md) | Optional|Photo to send|
|send\_message|[InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.md) | Yes|Message to send when the result is selected|



### Type: [InputBotInlineResult](/API_docs/types/InputBotInlineResult.md)


### Example:

```php
$inputBotInlineResultPhoto = ['_' => 'inputBotInlineResultPhoto', 'id' => 'string', 'type' => 'string', 'photo' => InputPhoto, 'send_message' => InputBotInlineMessage];
```  
