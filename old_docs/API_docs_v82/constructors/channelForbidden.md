---
title: channelForbidden
description: Forbidden channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelForbidden  
[Back to constructors index](index.md)



Forbidden channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|broadcast|[Bool](../types/Bool.md) | Optional|Broadcast?|
|megagroup|[Bool](../types/Bool.md) | Optional|Megagroup?|
|id|[int](../types/int.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|title|[string](../types/string.md) | Yes|Title|
|until\_date|[int](../types/int.md) | Optional|Until date|



### Type: [Chat](../types/Chat.md)


### Example:

```php
$channelForbidden = ['_' => 'channelForbidden', 'broadcast' => Bool, 'megagroup' => Bool, 'id' => int, 'access_hash' => long, 'title' => 'string', 'until_date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channelForbidden", "broadcast": Bool, "megagroup": Bool, "id": int, "access_hash": long, "title": "string", "until_date": int}
```


Or, if you're into Lua:

```lua
channelForbidden={_='channelForbidden', broadcast=Bool, megagroup=Bool, id=int, access_hash=long, title='string', until_date=int}

```


