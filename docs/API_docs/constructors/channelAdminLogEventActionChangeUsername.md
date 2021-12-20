---
title: "channelAdminLogEventActionChangeUsername"
description: "Channel/supergroup username was changed"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeUsername  
[Back to constructors index](index.md)



Channel/supergroup username was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[string](../types/string.md) | Yes|Old username|
|new\_value|[string](../types/string.md) | Yes|New username|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionChangeUsername = ['_' => 'channelAdminLogEventActionChangeUsername', 'prev_value' => 'string', 'new_value' => 'string'];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionChangeUsername={_='channelAdminLogEventActionChangeUsername', prev_value='string', new_value='string'}

```


