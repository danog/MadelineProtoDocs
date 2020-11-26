---
title: jsonObjectValue
description: JSON key: value pair
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: jsonObjectValue  
[Back to constructors index](index.md)



JSON key: value pair

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|key|[string](../types/string.md) | Yes|Key|
|value|[JSONValue](../types/JSONValue.md) | Yes|Value|



### Type: [JSONObjectValue](../types/JSONObjectValue.md)


### Example:

```php
$jsonObjectValue = ['_' => 'jsonObjectValue', 'key' => 'string', 'value' => JSONValue];
```  


Or, if you're into Lua:

```lua
jsonObjectValue={_='jsonObjectValue', key='string', value=JSONValue}

```


