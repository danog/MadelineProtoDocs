---
title: "updateShort"
description: "Shortened constructor containing info on one update not requiring auxiliary data"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShort  
[Back to constructors index](index.md)



Shortened constructor containing info on one update not requiring auxiliary data

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|update|[Update](../types/Update.md) | Yes|Update|
|date|[int](../types/int.md) | Yes|Date of event|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updateShort = ['_' => 'updateShort', 'update' => Update, 'date' => int];
```  


Or, if you're into Lua:

```lua
updateShort={_='updateShort', update=Update, date=int}

```


