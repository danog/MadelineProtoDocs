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
|prev\_photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|Previous photo|
|new\_photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|New photo|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionChangePhoto = ['_' => 'channelAdminLogEventActionChangePhoto', 'prev_photo' => ChatPhoto, 'new_photo' => ChatPhoto];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionChangePhoto={_='channelAdminLogEventActionChangePhoto', prev_photo=ChatPhoto, new_photo=ChatPhoto}

```


