---
title: "inputMediaContact"
description: "Phonebook contact"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaContact  
[Back to constructors index](/API_docs/constructors/index.md)



Phonebook contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_number|[string](/API_docs/types/string.md) | Yes|Phone number|
|first\_name|[string](/API_docs/types/string.md) | Yes|Contact's first name|
|last\_name|[string](/API_docs/types/string.md) | Yes|Contact's last name|
|vcard|[string](/API_docs/types/string.md) | Yes|Contact vcard|



### Type: [InputMedia](/API_docs/types/InputMedia.md)


### Example:

```php
$inputMediaContact = ['_' => 'inputMediaContact', 'phone_number' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'vcard' => 'string'];
```  
