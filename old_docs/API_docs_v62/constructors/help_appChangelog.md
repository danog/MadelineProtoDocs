---
title: help.appChangelog
description: App changelog
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.appChangelog  
[Back to constructors index](index.md)



App changelog

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[string](../types/string.md) | Yes|Message|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|Media|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Yes|Entities|



### Type: [help\_AppChangelog](../types/help_AppChangelog.md)


### Example:

```php
$help_appChangelog = ['_' => 'help.appChangelog', 'message' => 'string', 'media' => MessageMedia, 'entities' => [MessageEntity, MessageEntity]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "help.appChangelog", "message": "string", "media": MessageMedia, "entities": [MessageEntity]}
```


Or, if you're into Lua:

```lua
help_appChangelog={_='help.appChangelog', message='string', media=MessageMedia, entities={MessageEntity}}

```


