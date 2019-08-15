---
title: inputAppEvent
description: App event
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputAppEvent  
[Back to constructors index](index.md)



App event

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|time|[double](../types/double.md) | Yes|Time|
|type|[string](../types/string.md) | Yes|Type|
|peer|[long](../types/long.md) | Yes|Peer|
|data|[JSONValue](../types/JSONValue.md) | Yes|Data|



### Type: [InputAppEvent](../types/InputAppEvent.md)


### Example:

```php
$inputAppEvent = ['_' => 'inputAppEvent', 'time' => double, 'type' => 'string', 'peer' => long, 'data' => JSONValue];
```  


Or, if you're into Lua:

```lua
inputAppEvent={_='inputAppEvent', time=double, type='string', peer=long, data=JSONValue}

```


