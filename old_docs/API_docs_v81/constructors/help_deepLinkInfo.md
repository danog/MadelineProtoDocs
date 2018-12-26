---
title: help.deepLinkInfo
description: Deep link info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.deepLinkInfo  
[Back to constructors index](index.md)



Deep link info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|update\_app|[Bool](../types/Bool.md) | Optional|Update app?|
|message|[string](../types/string.md) | Yes|Message|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Entities|



### Type: [help\_DeepLinkInfo](../types/help_DeepLinkInfo.md)


### Example:

```php
$help_deepLinkInfo = ['_' => 'help.deepLinkInfo', 'update_app' => Bool, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "help.deepLinkInfo", "update_app": Bool, "message": "string", "entities": [MessageEntity]}
```


Or, if you're into Lua:

```lua
help_deepLinkInfo={_='help.deepLinkInfo', update_app=Bool, message='string', entities={MessageEntity}}

```


