---
title: updateChannelMessageViews
description: Update channel message views
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelMessageViews  
[Back to constructors index](index.md)



Update channel message views

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|id|[int](../types/int.md) | Yes|ID|
|views|[int](../types/int.md) | Yes|Views|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelMessageViews = ['_' => 'updateChannelMessageViews', 'channel_id' => int, 'id' => int, 'views' => int];
```  


Or, if you're into Lua:

```lua
updateChannelMessageViews={_='updateChannelMessageViews', channel_id=int, id=int, views=int}

```


