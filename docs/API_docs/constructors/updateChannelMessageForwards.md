---
title: "updateChannelMessageForwards"
description: "The forward counter of a message in a channel has changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelMessageForwards  
[Back to constructors index](index.md)



The forward counter of a message in a channel has changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](../types/long.md) | Yes|
|id|[int](../types/int.md) | Yes|ID of the message|
|forwards|[int](../types/int.md) | Yes|New forward counter|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelMessageForwards = ['_' => 'updateChannelMessageForwards', 'channel_id' => long, 'id' => int, 'forwards' => int];
```  
