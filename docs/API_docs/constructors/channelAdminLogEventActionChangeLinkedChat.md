---
title: channelAdminLogEventActionChangeLinkedChat
description: Linked chat was changed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeLinkedChat  
[Back to constructors index](index.md)



Linked chat was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[int](../types/int.md) | Yes|Old linked chat|
|new\_value|[int](../types/int.md) | Yes|New linked chat|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionChangeLinkedChat = ['_' => 'channelAdminLogEventActionChangeLinkedChat', 'prev_value' => int, 'new_value' => int];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionChangeLinkedChat={_='channelAdminLogEventActionChangeLinkedChat', prev_value=int, new_value=int}

```


