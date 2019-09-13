---
title: messageEntityTextUrl
description: Message entity text URL
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityTextUrl  
[Back to constructors index](index.md)



Message entity text URL

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|length|[int](../types/int.md) | Yes|Length|
|url|[string](../types/string.md) | Yes|URL|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityTextUrl = ['_' => 'messageEntityTextUrl', 'offset' => int, 'length' => int, 'url' => 'string'];
```  


Or, if you're into Lua:

```lua
messageEntityTextUrl={_='messageEntityTextUrl', offset=int, length=int, url='string'}

```


