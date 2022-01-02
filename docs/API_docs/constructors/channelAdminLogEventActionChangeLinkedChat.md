---
title: "channelAdminLogEventActionChangeLinkedChat"
description: "The linked chat was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeLinkedChat  
[Back to constructors index](index.md)



The linked chat was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[long](../types/long.md) | Yes|
|new\_value|[long](../types/long.md) | Yes|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionChangeLinkedChat = ['_' => 'channelAdminLogEventActionChangeLinkedChat', 'prev_value' => long, 'new_value' => long];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionChangeLinkedChat={_='channelAdminLogEventActionChangeLinkedChat', prev_value=long, new_value=long}

```


