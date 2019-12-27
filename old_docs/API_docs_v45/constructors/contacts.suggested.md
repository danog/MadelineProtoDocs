---
title: contacts.suggested
description: Suggested
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_suggested.html
---
# Constructor: contacts.suggested  
[Back to constructors index](index.md)



Suggested

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|results|Array of [ContactSuggested](../types/ContactSuggested.md) | Yes|Results|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [contacts.Suggested](../types/contacts.Suggested.md)


### Example:

```php
$contacts.suggested = ['_' => 'contacts.suggested', 'results' => [ContactSuggested, ContactSuggested], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
contacts.suggested={_='contacts.suggested', results={ContactSuggested}, users={User}}

```


