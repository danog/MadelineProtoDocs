---
title: "inputBotInlineResult"
description: "An inline bot result"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineResult  
[Back to constructors index](/API_docs/constructors/index.md)



An inline bot result

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](/API_docs/types/string.md) | Yes|ID of result|
|type|[string](/API_docs/types/string.md) | Yes|Result type (see [bot API docs](https://core.telegram.org/bots/api#inlinequeryresult))|
|title|[string](/API_docs/types/string.md) | Optional|Result title|
|description|[string](/API_docs/types/string.md) | Optional|Result description|
|url|[string](/API_docs/types/string.md) | Optional|URL of result|
|thumb|[InputWebDocument](/API_docs/types/InputWebDocument.md) | Optional|Thumbnail for result|
|content|[InputWebDocument](/API_docs/types/InputWebDocument.md) | Optional|Result contents|
|send\_message|[InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.md) | Yes|Message to send when the result is selected|



### Type: [InputBotInlineResult](/API_docs/types/InputBotInlineResult.md)


### Example:

```php
$inputBotInlineResult = ['_' => 'inputBotInlineResult', 'id' => 'string', 'type' => 'string', 'title' => 'string', 'description' => 'string', 'url' => 'string', 'thumb' => InputWebDocument, 'content' => InputWebDocument, 'send_message' => InputBotInlineMessage];
```  
