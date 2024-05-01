---
title: "inputBotInlineResultDocument"
description: "Document (media of any type except for photos)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineResultDocument  
[Back to constructors index](/API_docs/constructors/index.html)



Document (media of any type except for photos)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](/API_docs/types/string.html) | Yes|Result ID|
|type|[string](/API_docs/types/string.html) | Yes|Result type (see [bot API docs](https://core.telegram.org/bots/api#inlinequeryresult))|
|title|[string](/API_docs/types/string.html) | Optional|Result title|
|description|[string](/API_docs/types/string.html) | Optional|Result description|
|document|[MessageMedia, Message, Update or InputDocument](/API_docs/types/InputDocument.html) | Optional|Document to send|
|send\_message|[InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.html) | Yes|Message to send when the result is selected|



### Type: [InputBotInlineResult](/API_docs/types/InputBotInlineResult.html)


### Example:

```
$inputBotInlineResultDocument = ['_' => 'inputBotInlineResultDocument', 'id' => 'string', 'type' => 'string', 'title' => 'string', 'description' => 'string', 'document' => InputDocument, 'send_message' => InputBotInlineMessage];
```  
