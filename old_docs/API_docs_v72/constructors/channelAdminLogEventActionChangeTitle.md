---
title: channelAdminLogEventActionChangeTitle
description: channelAdminLogEventActionChangeTitle attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeTitle  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|prev\_value|[string](../types/string.md) | Yes|
|new\_value|[string](../types/string.md) | Yes|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionChangeTitle = ['_' => 'channelAdminLogEventActionChangeTitle', 'prev_value' => 'string', 'new_value' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channelAdminLogEventActionChangeTitle", "prev_value": "string", "new_value": "string"}
```


Or, if you're into Lua:

```lua
channelAdminLogEventActionChangeTitle={_='channelAdminLogEventActionChangeTitle', prev_value='string', new_value='string'}

```


