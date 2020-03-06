---
title: jsonObject
description: JSON object value
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: jsonObject  
[Back to constructors index](index.md)



JSON object value

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|value|Array of [JSONObjectValue](../types/JSONObjectValue.md) | Yes|Value|



### Type: [JSONValue](../types/JSONValue.md)


### Example:

```php
$jsonObject = ['_' => 'jsonObject', 'value' => [JSONObjectValue, JSONObjectValue]];
```  


Or, if you're into Lua:

```lua
jsonObject={_='jsonObject', value={JSONObjectValue}}

```


