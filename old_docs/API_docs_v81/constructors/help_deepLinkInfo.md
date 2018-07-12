---
title: help.deepLinkInfo
description: help_deepLinkInfo attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.deepLinkInfo  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|update\_app|[Bool](../types/Bool.md) | Optional|
|message|[string](../types/string.md) | Yes|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|



### Type: [help\_DeepLinkInfo](../types/help_DeepLinkInfo.md)


### Example:

```
$help_deepLinkInfo = ['_' => 'help.deepLinkInfo', 'update_app' => Bool, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "help.deepLinkInfo", "update_app": Bool, "message": "string", "entities": [MessageEntity]}
```


Or, if you're into Lua:  


```
help_deepLinkInfo={_='help.deepLinkInfo', update_app=Bool, message='string', entities={MessageEntity}}

```


