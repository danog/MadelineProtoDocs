---
title: contacts.myLinkRequested
description: My link requested
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contacts.myLinkRequested  
[Back to constructors index](index.md)



My link requested

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|contact|[Bool](../types/Bool.md) | Yes|Contact?|



### Type: [contacts\_MyLink](../types/contacts_MyLink.md)


### Example:

```php
$contacts_myLinkRequested = ['_' => 'contacts.myLinkRequested', 'contact' => Bool];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "contacts.myLinkRequested", "contact": Bool}
```


Or, if you're into Lua:

```lua
contacts_myLinkRequested={_='contacts.myLinkRequested', contact=Bool}

```


