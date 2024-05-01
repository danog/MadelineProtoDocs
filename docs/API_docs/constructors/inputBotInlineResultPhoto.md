---
title: "inputBotInlineResultPhoto"
description: "Photo"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineResultPhoto  
[Back to constructors index](/API_docs/constructors/index.html)



Photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](/API_docs/types/string.html) | Yes|Result ID|
|type|[string](/API_docs/types/string.html) | Yes|Result type (see [bot API docs](https://core.telegram.org/bots/api#inlinequeryresult))|
|photo|[MessageMedia, Message, Update or InputPhoto](/API_docs/types/InputPhoto.html) | Optional|Photo to send|
|send\_message|[InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.html) | Yes|Message to send when the result is selected|



### Type: [InputBotInlineResult](/API_docs/types/InputBotInlineResult.html)


### Example:

```
$inputBotInlineResultPhoto = ['_' => 'inputBotInlineResultPhoto', 'id' => 'string', 'type' => 'string', 'photo' => InputPhoto, 'send_message' => InputBotInlineMessage];
```  
