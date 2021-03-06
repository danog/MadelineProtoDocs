---
title: updateChannelMessageForwards
description: The forward counter of a message in a channel has changed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelMessageForwards  
[Back to constructors index](index.md)



The forward counter of a message in a channel has changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|id|[int](../types/int.md) | Yes|ID of the message|
|forwards|[int](../types/int.md) | Yes|New forward counter|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelMessageForwards = ['_' => 'updateChannelMessageForwards', 'channel_id' => int, 'id' => int, 'forwards' => int];
```  


Or, if you're into Lua:

```lua
updateChannelMessageForwards={_='updateChannelMessageForwards', channel_id=int, id=int, forwards=int}

```


