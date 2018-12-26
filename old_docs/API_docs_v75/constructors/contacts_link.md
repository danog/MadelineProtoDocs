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
|my\_link|[ContactLink](../types/ContactLink.md) | Yes|My link|
|foreign\_link|[ContactLink](../types/ContactLink.md) | Yes|Foreign link|
|user|[User](../types/User.md) | Optional|User|



### Type: [contacts\_Link](../types/contacts_Link.md)


### Example:

```php
$contacts_link = ['_' => 'contacts.link', 'my_link' => ContactLink, 'foreign_link' => ContactLink, 'user' => User];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "contacts.link", "my_link": ContactLink, "foreign_link": ContactLink, "user": User}
```


Or, if you're into Lua:

```lua
contacts_link={_='contacts.link', my_link=ContactLink, foreign_link=ContactLink, user=User}

```


