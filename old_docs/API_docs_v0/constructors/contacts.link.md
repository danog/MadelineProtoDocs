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
|my\_link|[contacts.MyLink](../constructors/contacts.MyLink.md) | Yes|
|foreign\_link|[contacts.ForeignLink](../constructors/contacts.ForeignLink.md) | Yes|
|user|[User](../types/User.md) | Optional|



### Type: [contacts.Link](../types/contacts.Link.md)


### Example:

```php
$contacts_link = ['_' => 'contacts.link', 'my_link' => contacts.MyLink, 'foreign_link' => contacts.ForeignLink, 'user' => User];
```  


Or, if you're into Lua:

```lua
contacts_link={_='contacts.link', my_link=contacts.MyLink, foreign_link=contacts.ForeignLink, user=User}

```


