---
title: secureValueErrorTranslationFiles
description: Secure value error translation files
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorTranslationFiles  
[Back to constructors index](index.md)



Secure value error translation files

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|Type|
|file\_hash|Array of [bytes](../types/bytes.md) | Yes|File hash|
|text|[string](../types/string.md) | Yes|Text|



### Type: [SecureValueError](../types/SecureValueError.md)


### Example:

```php
$secureValueErrorTranslationFiles = ['_' => 'secureValueErrorTranslationFiles', 'type' => SecureValueType, 'file_hash' => ['bytes', 'bytes'], 'text' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureValueErrorTranslationFiles", "type": SecureValueType, "file_hash": [{"_": "bytes", "bytes":"base64 encoded bytes"}], "text": "string"}
```


Or, if you're into Lua:

```lua
secureValueErrorTranslationFiles={_='secureValueErrorTranslationFiles', type=SecureValueType, file_hash={'bytes'}, text='string'}

```


