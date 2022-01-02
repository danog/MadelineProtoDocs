---
title: "messageActionChannelMigrateFrom"
description: "Indicates the channel was migrated from the specified chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChannelMigrateFrom  
[Back to constructors index](index.md)



Indicates the channel was [migrated](https://core.telegram.org/api/channel) from the specified chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](../types/string.md) | Yes|The old chat tite|
|chat\_id|[long](../types/long.md) | Yes|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionChannelMigrateFrom = ['_' => 'messageActionChannelMigrateFrom', 'title' => 'string', 'chat_id' => long];
```  


Or, if you're into Lua:

```lua
messageActionChannelMigrateFrom={_='messageActionChannelMigrateFrom', title='string', chat_id=long}

```


