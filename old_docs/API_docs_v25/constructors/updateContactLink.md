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
|my\_link|[ContactLink](../types/ContactLink.md) | Yes|My link|
|foreign\_link|[ContactLink](../types/ContactLink.md) | Yes|Foreign link|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateContactLink = ['_' => 'updateContactLink', 'user_id' => int, 'my_link' => ContactLink, 'foreign_link' => ContactLink];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateContactLink", "user_id": int, "my_link": ContactLink, "foreign_link": ContactLink}
```


Or, if you're into Lua:

```lua
updateContactLink={_='updateContactLink', user_id=int, my_link=ContactLink, foreign_link=ContactLink}

```


