---
title: restrictionReason
description: Restriction reason
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: restrictionReason  
[Back to constructors index](index.md)



Restriction reason

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|platform|[string](../types/string.md) | Yes|Platform|
|reason|[string](../types/string.md) | Yes|Reason|
|text|[string](../types/string.md) | Yes|Text|



### Type: [RestrictionReason](../types/RestrictionReason.md)


### Example:

```php
$restrictionReason = ['_' => 'restrictionReason', 'platform' => 'string', 'reason' => 'string', 'text' => 'string'];
```  


Or, if you're into Lua:

```lua
restrictionReason={_='restrictionReason', platform='string', reason='string', text='string'}

```


