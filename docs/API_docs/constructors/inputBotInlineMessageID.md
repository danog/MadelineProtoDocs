---
title: "inputBotInlineMessageID"
description: "Represents a sent inline message from the perspective of a bot"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageID  
[Back to constructors index](index.md)



Represents a sent inline message from the perspective of a bot

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dc\_id|[int](../types/int.md) | Yes|DC ID to use when working with this inline message|
|id|[long](../types/long.md) | Yes|ID of message|
|access\_hash|[long](../types/long.md) | Yes|Access hash of message|



### Type: [InputBotInlineMessageID](../types/InputBotInlineMessageID.md)


### Example:

```php
$inputBotInlineMessageID = ['_' => 'inputBotInlineMessageID', 'dc_id' => int, 'id' => long, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputBotInlineMessageID={_='inputBotInlineMessageID', dc_id=int, id=long, access_hash=long}

```


