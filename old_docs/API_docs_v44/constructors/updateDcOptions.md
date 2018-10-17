---
title: updateDcOptions
description: updateDcOptions attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDcOptions  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|dc\_options|Array of [DcOption](../types/DcOption.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDcOptions = ['_' => 'updateDcOptions', 'dc_options' => [DcOption, DcOption]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateDcOptions", "dc_options": [DcOption]}
```


Or, if you're into Lua:

```lua
updateDcOptions={_='updateDcOptions', dc_options={DcOption}}

```


