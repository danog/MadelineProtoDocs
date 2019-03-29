---
title: updateContactLink
description: Update contact link
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateContactLink  
[Back to constructors index](index.md)



Update contact link

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|my\_link|[contacts\_MyLink](../types/contacts_MyLink.md) | Yes|My link|
|foreign\_link|[contacts\_ForeignLink](../types/contacts_ForeignLink.md) | Yes|Foreign link|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateContactLink = ['_' => 'updateContactLink', 'user_id' => int, 'my_link' => contacts_MyLink, 'foreign_link' => contacts_ForeignLink];
```  


Or, if you're into Lua:

```lua
updateContactLink={_='updateContactLink', user_id=int, my_link=contacts_MyLink, foreign_link=contacts_ForeignLink}

```


