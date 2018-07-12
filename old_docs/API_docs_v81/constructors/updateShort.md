---
title: updateShort
description: updateShort attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShort  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|update|[Update](../types/Update.md) | Yes|
|date|[int](../types/int.md) | Yes|



### Type: [Updates](../types/Updates.md)


### Example:

```
$updateShort = ['_' => 'updateShort', 'update' => Update, 'date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateShort", "update": Update, "date": int}
```


Or, if you're into Lua:  


```
updateShort={_='updateShort', update=Update, date=int}

```


