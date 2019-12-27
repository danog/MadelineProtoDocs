---
title: inputBotInlineMessageText
description: Simple text message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageText  
[Back to constructors index](index.md)



Simple text message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|no\_webpage|[Bool](../types/Bool.md) | Optional|Disable webpage preview|
|message|[string](../types/string.md) | Yes|Message|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Entities|



### Type: [InputBotInlineMessage](../types/InputBotInlineMessage.md)


### Example:

```php
$inputBotInlineMessageText = ['_' => 'inputBotInlineMessageText', 'no_webpage' => Bool, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]];
```  


Or, if you're into Lua:

```lua
inputBotInlineMessageText={_='inputBotInlineMessageText', no_webpage=Bool, message='string', entities={MessageEntity}}

```


