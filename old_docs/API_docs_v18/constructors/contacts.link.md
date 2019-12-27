---
title: contacts.link
description: Link
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contacts.link  
[Back to constructors index](index.md)



Link

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|my\_link|[contacts.MyLink](../constructors/contacts.MyLink.md) | Yes|My link|
|foreign\_link|[contacts.ForeignLink](../constructors/contacts.ForeignLink.md) | Yes|Foreign link|
|user|[User](../types/User.md) | Optional|User|



### Type: [contacts.Link](../types/contacts.Link.md)


### Example:

```php
$contacts.link = ['_' => 'contacts.link', 'my_link' => contacts.MyLink, 'foreign_link' => contacts.ForeignLink, 'user' => User];
```  


Or, if you're into Lua:

```lua
contacts.link={_='contacts.link', my_link=contacts.MyLink, foreign_link=contacts.ForeignLink, user=User}

```


