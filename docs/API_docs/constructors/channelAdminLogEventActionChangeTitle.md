---
title: "channelAdminLogEventActionChangeTitle"
description: "Channel/supergroup title was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeTitle  
[Back to constructors index](index.md)



Channel/supergroup title was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[string](../types/string.md) | Yes|Previous title|
|new\_value|[string](../types/string.md) | Yes|New title|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionChangeTitle = ['_' => 'channelAdminLogEventActionChangeTitle', 'prev_value' => 'string', 'new_value' => 'string'];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionChangeTitle={_='channelAdminLogEventActionChangeTitle', prev_value='string', new_value='string'}

```


