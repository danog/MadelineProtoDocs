---
title: "inputBotInlineMessageID64"
description: "inputBotInlineMessageID64 attributes, type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageID64  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|dc\_id|[int](../types/int.md) | Yes|
|owner\_id|[long](../types/long.md) | Yes|
|id|[int](../types/int.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|



### Type: [InputBotInlineMessageID](../types/InputBotInlineMessageID.md)


### Example:

```php
$inputBotInlineMessageID64 = ['_' => 'inputBotInlineMessageID64', 'dc_id' => int, 'owner_id' => long, 'id' => int, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputBotInlineMessageID64={_='inputBotInlineMessageID64', dc_id=int, owner_id=long, id=int, access_hash=long}

```


