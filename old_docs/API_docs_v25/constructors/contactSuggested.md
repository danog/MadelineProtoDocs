---
title: contactSuggested
description: Contact suggested
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contactSuggested  
[Back to constructors index](index.md)



Contact suggested

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|mutual\_contacts|[int](../types/int.md) | Yes|Mutual contacts|



### Type: [ContactSuggested](../types/ContactSuggested.md)


### Example:

```php
$contactSuggested = ['_' => 'contactSuggested', 'user_id' => int, 'mutual_contacts' => int];
```  


Or, if you're into Lua:

```lua
contactSuggested={_='contactSuggested', user_id=int, mutual_contacts=int}

```


