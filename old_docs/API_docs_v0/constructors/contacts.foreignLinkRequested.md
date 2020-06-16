---
title: contacts.foreignLinkRequested
description: contacts.foreignLinkRequested attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_foreignLinkRequested.html
---
# Constructor: contacts.foreignLinkRequested  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|has\_phone|[Bool](../types/Bool.md) | Yes|



### Type: [contacts.ForeignLink](../types/contacts.ForeignLink.md)


### Example:

```php
$contacts.foreignLinkRequested = ['_' => 'contacts.foreignLinkRequested', 'has_phone' => Bool];
```  


Or, if you're into Lua:

```lua
contacts.foreignLinkRequested={_='contacts.foreignLinkRequested', has_phone=Bool}

```


