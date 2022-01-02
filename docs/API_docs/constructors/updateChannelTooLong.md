---
title: "updateChannelTooLong"
description: "There are new updates in the specified channel, the client must fetch them.  "
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelTooLong  
[Back to constructors index](index.md)



There are new updates in the specified channel, the client must fetch them.  
If the difference is too long or if the channel isn't currently in the states, start fetching from the specified pts.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](../types/long.md) | Yes|
|pts|[int](../types/int.md) | Optional|The [PTS](https://core.telegram.org/api/updates).|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelTooLong = ['_' => 'updateChannelTooLong', 'channel_id' => long, 'pts' => int];
```  


Or, if you're into Lua:

```lua
updateChannelTooLong={_='updateChannelTooLong', channel_id=long, pts=int}

```


