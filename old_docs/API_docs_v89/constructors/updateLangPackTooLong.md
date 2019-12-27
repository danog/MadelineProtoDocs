---
title: updateLangPackTooLong
description: A language pack has changed, the client should manually fetch the changed strings using [langpack.getDifference](../methods/langpack.getDifference.md)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateLangPackTooLong  
[Back to constructors index](index.md)



A language pack has changed, the client should manually fetch the changed strings using [langpack.getDifference](../methods/langpack.getDifference.md)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|lang\_code|[string](../types/string.md) | Yes|Language code|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateLangPackTooLong = ['_' => 'updateLangPackTooLong', 'lang_code' => 'string'];
```  


Or, if you're into Lua:

```lua
updateLangPackTooLong={_='updateLangPackTooLong', lang_code='string'}

```


