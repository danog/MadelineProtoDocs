---
title: "updateReadChannelOutbox"
description: "Outgoing messages in a channel/supergroup were read"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadChannelOutbox  
[Back to constructors index](index.md)



Outgoing messages in a [channel/supergroup](https://core.telegram.org/api/channel) were read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](../types/long.md) | Yes|
|max\_id|[int](../types/int.md) | Yes|Position up to which all outgoing messages are read.|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadChannelOutbox = ['_' => 'updateReadChannelOutbox', 'channel_id' => long, 'max_id' => int];
```  
