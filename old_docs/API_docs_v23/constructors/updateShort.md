---
title: updateShort
description: Update short
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShort  
[Back to constructors index](index.md)



Update short

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|update|[Update](../types/Update.md) | Yes|Update|
|date|[int](../types/int.md) | Yes|Date|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updateShort = ['_' => 'updateShort', 'update' => Update, 'date' => int];
```  


Or, if you're into Lua:

```lua
updateShort={_='updateShort', update=Update, date=int}

```


