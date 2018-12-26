---
title: messageActionBotAllowed
description: Message action bot allowed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionBotAllowed  
[Back to constructors index](index.md)



Message action bot allowed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|domain|[string](../types/string.md) | Yes|Domain|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionBotAllowed = ['_' => 'messageActionBotAllowed', 'domain' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageActionBotAllowed", "domain": "string"}
```


Or, if you're into Lua:

```lua
messageActionBotAllowed={_='messageActionBotAllowed', domain='string'}

```


