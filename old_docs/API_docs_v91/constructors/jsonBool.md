---
title: jsonBool
description: Json bool
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: jsonBool  
[Back to constructors index](index.md)



Json bool

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|value|[Bool](../types/Bool.md) | Yes|Value?|



### Type: [JSONValue](../types/JSONValue.md)


### Example:

```php
$jsonBool = ['_' => 'jsonBool', 'value' => Bool];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "jsonBool", "value": Bool}
```


Or, if you're into Lua:

```lua
jsonBool={_='jsonBool', value=Bool}

```


