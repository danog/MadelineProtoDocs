---
title: "botInlineResult"
description: "Generic result"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineResult  
[Back to constructors index](/API_docs/constructors/index.html)



Generic result

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](/API_docs/types/string.html) | Yes|Result ID|
|type|[string](/API_docs/types/string.html) | Yes|Result type (see [bot API docs](https://core.telegram.org/bots/api#inlinequeryresult))|
|title|[string](/API_docs/types/string.html) | Optional|Result title|
|description|[string](/API_docs/types/string.html) | Optional|Result description|
|url|[string](/API_docs/types/string.html) | Optional|URL of article or webpage|
|thumb|[WebDocument](/API_docs/types/WebDocument.html) | Optional|Thumbnail for the result|
|content|[WebDocument](/API_docs/types/WebDocument.html) | Optional|Content of the result|
|send\_message|[BotInlineMessage](/API_docs/types/BotInlineMessage.html) | Yes|Message to send|



### Type: [BotInlineResult](/API_docs/types/BotInlineResult.html)


### Example:

```
$botInlineResult = ['_' => 'botInlineResult', 'id' => 'string', 'type' => 'string', 'title' => 'string', 'description' => 'string', 'url' => 'string', 'thumb' => WebDocument, 'content' => WebDocument, 'send_message' => BotInlineMessage];
```  
