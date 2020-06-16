---
title: contacts.link
description: contacts.link attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/contacts_link.html
---
# Constructor: contacts.link  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|my\_link|[ContactLink](../types/ContactLink.md) | Yes|
|foreign\_link|[ContactLink](../types/ContactLink.md) | Yes|
|user|[User](../types/User.md) | Optional|



### Type: [contacts.Link](../types/contacts.Link.md)


### Example:

```php
$contacts.link = ['_' => 'contacts.link', 'my_link' => ContactLink, 'foreign_link' => ContactLink, 'user' => User];
```  


Or, if you're into Lua:

```lua
contacts.link={_='contacts.link', my_link=ContactLink, foreign_link=ContactLink, user=User}

```


