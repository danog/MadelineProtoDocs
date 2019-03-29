---
title: updateLangPack
description: Update lang pack
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateLangPack  
[Back to constructors index](index.md)



Update lang pack

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|difference|[LangPackDifference](../types/LangPackDifference.md) | Yes|Difference|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateLangPack = ['_' => 'updateLangPack', 'difference' => LangPackDifference];
```  


Or, if you're into Lua:

```lua
updateLangPack={_='updateLangPack', difference=LangPackDifference}

```


