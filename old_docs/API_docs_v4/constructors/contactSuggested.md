---
title: contactSuggested
description: contactSuggested attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contactSuggested  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[int](../types/int.md) | Yes|
|mutual\_contacts|[int](../types/int.md) | Yes|



### Type: [ContactSuggested](../types/ContactSuggested.md)


### Example:

```php
$contactSuggested = ['_' => 'contactSuggested', 'user_id' => int, 'mutual_contacts' => int];
```  


Or, if you're into Lua:

```lua
contactSuggested={_='contactSuggested', user_id=int, mutual_contacts=int}

```


