---
title: "updateLangPack"
description: "Language pack updated"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateLangPack  
[Back to constructors index](index.md)



Language pack updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|difference|[LangPackDifference](../types/LangPackDifference.md) | Yes|Changed strings|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateLangPack = ['_' => 'updateLangPack', 'difference' => LangPackDifference];
```  


Or, if you're into Lua:

```lua
updateLangPack={_='updateLangPack', difference=LangPackDifference}

```


