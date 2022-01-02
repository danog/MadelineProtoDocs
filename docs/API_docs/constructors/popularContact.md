---
title: "popularContact"
description: "Popular contact"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: popularContact  
[Back to constructors index](index.md)



Popular contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|client\_id|[long](../types/long.md) | Yes|Contact identifier|
|importers|[int](../types/int.md) | Yes|How many people imported this contact|



### Type: [PopularContact](../types/PopularContact.md)


### Example:

```php
$popularContact = ['_' => 'popularContact', 'client_id' => long, 'importers' => int];
```  


Or, if you're into Lua:

```lua
popularContact={_='popularContact', client_id=long, importers=int}

```


