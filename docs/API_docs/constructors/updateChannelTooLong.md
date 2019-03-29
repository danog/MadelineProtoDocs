---
title: updateChannelTooLong
description: Update channel too long
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelTooLong  
[Back to constructors index](index.md)



Update channel too long

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|pts|[int](../types/int.md) | Optional|Pts|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelTooLong = ['_' => 'updateChannelTooLong', 'channel_id' => int, 'pts' => int];
```  


Or, if you're into Lua:

```lua
updateChannelTooLong={_='updateChannelTooLong', channel_id=int, pts=int}

```


