---
title: "inputAppEvent"
description: "Event that occured in the application."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputAppEvent  
[Back to constructors index](index.md)



Event that occured in the application.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|time|[double](../types/double.md) | Yes|Client's exact timestamp for the event|
|type|[string](../types/string.md) | Yes|Type of event|
|peer|[long](../types/long.md) | Yes|Arbitrary numeric value for more convenient selection of certain event types, or events referring to a certain object|
|data|[JSONValue](../types/JSONValue.md) | Yes|Details of the event|



### Type: [InputAppEvent](../types/InputAppEvent.md)


### Example:

```php
$inputAppEvent = ['_' => 'inputAppEvent', 'time' => double, 'type' => 'string', 'peer' => long, 'data' => JSONValue];
```  


Or, if you're into Lua:

```lua
inputAppEvent={_='inputAppEvent', time=double, type='string', peer=long, data=JSONValue}

```


