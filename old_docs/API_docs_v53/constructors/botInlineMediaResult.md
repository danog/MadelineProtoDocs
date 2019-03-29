---
title: botInlineMediaResult
description: Bot inline media result
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMediaResult  
[Back to constructors index](index.md)



Bot inline media result

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Yes|ID|
|type|[string](../types/string.md) | Yes|Type|
|photo|[Photo](../types/Photo.md) | Optional|Photo|
|document|[Document](../types/Document.md) | Optional|Document|
|title|[string](../types/string.md) | Optional|Title|
|description|[string](../types/string.md) | Optional|Description|
|send\_message|[BotInlineMessage](../types/BotInlineMessage.md) | Yes|Send message|



### Type: [BotInlineResult](../types/BotInlineResult.md)


### Example:

```php
$botInlineMediaResult = ['_' => 'botInlineMediaResult', 'id' => 'string', 'type' => 'string', 'photo' => Photo, 'document' => Document, 'title' => 'string', 'description' => 'string', 'send_message' => BotInlineMessage];
```  


Or, if you're into Lua:

```lua
botInlineMediaResult={_='botInlineMediaResult', id='string', type='string', photo=Photo, document=Document, title='string', description='string', send_message=BotInlineMessage}

```


