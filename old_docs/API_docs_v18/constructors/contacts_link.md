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
|my\_link|[contacts\_MyLink](../types/contacts_MyLink.md) | Yes|My link|
|foreign\_link|[contacts\_ForeignLink](../types/contacts_ForeignLink.md) | Yes|Foreign link|
|user|[User](../types/User.md) | Optional|User|



### Type: [contacts\_Link](../types/contacts_Link.md)


### Example:

```php
$contacts_link = ['_' => 'contacts.link', 'my_link' => contacts_MyLink, 'foreign_link' => contacts_ForeignLink, 'user' => User];
```  


Or, if you're into Lua:

```lua
contacts_link={_='contacts.link', my_link=contacts_MyLink, foreign_link=contacts_ForeignLink, user=User}

```


