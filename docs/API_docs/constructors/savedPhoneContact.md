---
title: savedPhoneContact
description: savedPhoneContact attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: savedPhoneContact  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|phone|[string](../types/string.md) | Yes|
|first\_name|[string](../types/string.md) | Yes|
|last\_name|[string](../types/string.md) | Yes|
|date|[int](../types/int.md) | Yes|



### Type: [SavedContact](../types/SavedContact.md)


### Example:

```
$savedPhoneContact = ['_' => 'savedPhoneContact', 'phone' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "savedPhoneContact", "phone": "string", "first_name": "string", "last_name": "string", "date": int}
```


Or, if you're into Lua:  


```
savedPhoneContact={_='savedPhoneContact', phone='string', first_name='string', last_name='string', date=int}

```


