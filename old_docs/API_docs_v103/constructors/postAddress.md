---
title: postAddress
description: Post address
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: postAddress  
[Back to constructors index](index.md)



Post address

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|street\_line1|[string](../types/string.md) | Yes|Street line1|
|street\_line2|[string](../types/string.md) | Yes|Street line2|
|city|[string](../types/string.md) | Yes|City|
|state|[string](../types/string.md) | Yes|State|
|country\_iso2|[string](../types/string.md) | Yes|Country iso2|
|post\_code|[string](../types/string.md) | Yes|Post code|



### Type: [PostAddress](../types/PostAddress.md)


### Example:

```php
$postAddress = ['_' => 'postAddress', 'street_line1' => 'string', 'street_line2' => 'string', 'city' => 'string', 'state' => 'string', 'country_iso2' => 'string', 'post_code' => 'string'];
```  


Or, if you're into Lua:

```lua
postAddress={_='postAddress', street_line1='string', street_line2='string', city='string', state='string', country_iso2='string', post_code='string'}

```


