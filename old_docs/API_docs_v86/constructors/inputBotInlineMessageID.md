---
title: inputBotInlineMessageID
description: Bot inline message ID
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageID  
[Back to constructors index](index.md)



Bot inline message ID

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dc\_id|[int](../types/int.md) | Yes|DC ID|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputBotInlineMessageID](../types/InputBotInlineMessageID.md)


### Example:

```php
$inputBotInlineMessageID = ['_' => 'inputBotInlineMessageID', 'dc_id' => int, 'id' => long, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputBotInlineMessageID", "dc_id": int, "id": long, "access_hash": long}
```


Or, if you're into Lua:

```lua
inputBotInlineMessageID={_='inputBotInlineMessageID', dc_id=int, id=long, access_hash=long}

```


