---
title: "botInlineMediaResult"
description: "Media result"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMediaResult  
[Back to constructors index](/API_docs/constructors/index.md)



Media result

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](/API_docs/types/string.md) | Yes|Result ID|
|type|[string](/API_docs/types/string.md) | Yes|Result type (see [bot API docs](https://core.telegram.org/bots/api#inlinequeryresult))|
|photo|[Photo](/API_docs/types/Photo.md) | Optional|If type is `photo`, the photo to send|
|document|[Document](/API_docs/types/Document.md) | Optional|If type is `document`, the document to send|
|title|[string](/API_docs/types/string.md) | Optional|Result title|
|description|[string](/API_docs/types/string.md) | Optional|Description|
|send\_message|[BotInlineMessage](/API_docs/types/BotInlineMessage.md) | Yes|Depending on the `type` and on the [constructor](../types/BotInlineMessage.md), contains the caption of the media or the content of the message to be sent **instead** of the media|



### Type: [BotInlineResult](/API_docs/types/BotInlineResult.md)


### Example:

```php
$botInlineMediaResult = ['_' => 'botInlineMediaResult', 'id' => 'string', 'type' => 'string', 'photo' => Photo, 'document' => Document, 'title' => 'string', 'description' => 'string', 'send_message' => BotInlineMessage];
```  
