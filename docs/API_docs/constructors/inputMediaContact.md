---
title: "inputMediaContact"
description: "Phone book contact"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaContact  
[Back to constructors index](/API_docs/constructors/index.html)



Phone book contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_number|[string](/API_docs/types/string.html) | Yes|Phone number|
|first\_name|[string](/API_docs/types/string.html) | Yes|Contact's first name|
|last\_name|[string](/API_docs/types/string.html) | Yes|Contact's last name|
|vcard|[string](/API_docs/types/string.html) | Yes|Contact vcard|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaContact = ['_' => 'inputMediaContact', 'phone_number' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'vcard' => 'string'];
```  
