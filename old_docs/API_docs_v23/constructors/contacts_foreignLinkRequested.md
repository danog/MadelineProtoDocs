---
title: contacts.foreignLinkRequested
description: Foreign link requested
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contacts.foreignLinkRequested  
[Back to constructors index](index.md)



Foreign link requested

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_phone|[Bool](../types/Bool.md) | Yes|Has phone?|



### Type: [contacts\_ForeignLink](../types/contacts_ForeignLink.md)


### Example:

```php
$contacts_foreignLinkRequested = ['_' => 'contacts.foreignLinkRequested', 'has_phone' => Bool];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "contacts.foreignLinkRequested", "has_phone": Bool}
```


Or, if you're into Lua:

```lua
contacts_foreignLinkRequested={_='contacts.foreignLinkRequested', has_phone=Bool}

```


