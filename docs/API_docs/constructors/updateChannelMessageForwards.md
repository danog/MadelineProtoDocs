---
title: updateChannelMessageForwards
description: updateChannelMessageForwards attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelMessageForwards  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel\_id|[int](../types/int.md) | Yes|
|id|[int](../types/int.md) | Yes|
|forwards|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelMessageForwards = ['_' => 'updateChannelMessageForwards', 'channel_id' => int, 'id' => int, 'forwards' => int];
```  


Or, if you're into Lua:

```lua
updateChannelMessageForwards={_='updateChannelMessageForwards', channel_id=int, id=int, forwards=int}

```


