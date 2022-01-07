---
title: "savedPhoneContact"
description: "Saved contact"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: savedPhoneContact  
[Back to constructors index](/API_docs/constructors/index.md)



Saved contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone|[string](/API_docs/types/string.md) | Yes|Phone number|
|first\_name|[string](/API_docs/types/string.md) | Yes|First name|
|last\_name|[string](/API_docs/types/string.md) | Yes|Last name|
|date|[int](/API_docs/types/int.md) | Yes|Date added|



### Type: [SavedContact](/API_docs/types/SavedContact.md)


### Example:

```php
$savedPhoneContact = ['_' => 'savedPhoneContact', 'phone' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'date' => int];
```  
