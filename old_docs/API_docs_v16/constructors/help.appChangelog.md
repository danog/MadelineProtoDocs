---
title: help.appChangelog
description: help.appChangelog attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_appChangelog.html
---
# Constructor: help.appChangelog  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|message|[string](../types/string.md) | Yes|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Yes|



### Type: [help.AppChangelog](../types/help.AppChangelog.md)


### Example:

```php
$help.appChangelog = ['_' => 'help.appChangelog', 'message' => 'string', 'media' => MessageMedia, 'entities' => [MessageEntity, MessageEntity]];
```  


Or, if you're into Lua:

```lua
help.appChangelog={_='help.appChangelog', message='string', media=MessageMedia, entities={MessageEntity}}

```


