---
title: channelAdminLogEventActionChangePhoto
description: The channel/supergroup's picture was changed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangePhoto  
[Back to constructors index](index.md)



The channel/supergroup's picture was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_photo|[Photo](../types/Photo.md) | Optional|Previous picture|
|new\_photo|[Photo](../types/Photo.md) | Optional|New picture|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionChangePhoto = ['_' => 'channelAdminLogEventActionChangePhoto', 'prev_photo' => Photo, 'new_photo' => Photo];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionChangePhoto={_='channelAdminLogEventActionChangePhoto', prev_photo=Photo, new_photo=Photo}

```


