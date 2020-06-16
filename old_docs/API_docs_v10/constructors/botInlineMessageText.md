---
title: botInlineMessageText
description: Send a simple text message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMessageText  
[Back to constructors index](index.md)



Send a simple text message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|no\_webpage|[Bool](../types/Bool.md) | Optional|Disable webpage preview|
|message|[string](../types/string.md) | Yes|The message|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|[Message entities for styled text](https://core.telegram.org/api/entities)|



### Type: [BotInlineMessage](../types/BotInlineMessage.md)


### Example:

```php
$botInlineMessageText = ['_' => 'botInlineMessageText', 'no_webpage' => Bool, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]];
```  


Or, if you're into Lua:

```lua
botInlineMessageText={_='botInlineMessageText', no_webpage=Bool, message='string', entities={MessageEntity}}

```


