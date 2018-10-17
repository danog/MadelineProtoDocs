---
title: simpleDataBlock
description: simpleDataBlock attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: simpleDataBlock  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|raw\_data|[string](../types/string.md) | Yes|



### Type: [DecryptedDataBlock](../types/DecryptedDataBlock.md)


### Example:

```php
$simpleDataBlock = ['_' => 'simpleDataBlock', 'raw_data' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "simpleDataBlock", "raw_data": "string"}
```


Or, if you're into Lua:

```lua
simpleDataBlock={_='simpleDataBlock', raw_data='string'}

```


