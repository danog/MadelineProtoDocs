---
title: jsonArray
description: JSON array
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: jsonArray  
[Back to constructors index](index.md)



JSON array

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|value|Array of [JSONValue](../types/JSONValue.md) | Yes|JSON values|



### Type: [JSONValue](../types/JSONValue.md)


### Example:

```php
$jsonArray = ['_' => 'jsonArray', 'value' => [JSONValue, JSONValue]];
```  


Or, if you're into Lua:

```lua
jsonArray={_='jsonArray', value={JSONValue}}

```


