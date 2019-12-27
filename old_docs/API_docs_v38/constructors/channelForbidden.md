---
title: channelForbidden
description: Indicates a channel/supergroup we can't access because we were banned, or for some other reason.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelForbidden  
[Back to constructors index](index.md)



Indicates a channel/supergroup we can't access because we were banned, or for some other reason.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|Channel ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|title|[string](../types/string.md) | Yes|Title|



### Type: [Chat](../types/Chat.md)


### Example:

```php
$channelForbidden = ['_' => 'channelForbidden', 'id' => int, 'access_hash' => long, 'title' => 'string'];
```  


Or, if you're into Lua:

```lua
channelForbidden={_='channelForbidden', id=int, access_hash=long, title='string'}

```


