---
title: updateChannel
description: A new channel is available
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannel  
[Back to constructors index](index.md)



A new channel is available

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannel = ['_' => 'updateChannel', 'channel_id' => int];
```  


Or, if you're into Lua:

```lua
updateChannel={_='updateChannel', channel_id=int}

```


