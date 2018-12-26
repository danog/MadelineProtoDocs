---
title: simpleDataBlock
description: Simple data block
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: simpleDataBlock  
[Back to constructors index](index.md)



Simple data block

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|raw\_data|[string](../types/string.md) | Yes|Raw data|



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


