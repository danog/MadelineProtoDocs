---
title: "savedPhoneContact"
description: "Saved contact"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: savedPhoneContact  
[Back to constructors index](/API_docs/constructors/index.html)



Saved contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone|[string](/API_docs/types/string.html) | Yes|Phone number|
|first\_name|[string](/API_docs/types/string.html) | Yes|First name|
|last\_name|[string](/API_docs/types/string.html) | Yes|Last name|
|date|[int](/API_docs/types/int.html) | Yes|Date added|



### Type: [SavedContact](/API_docs/types/SavedContact.html)


### Example:

```
$savedPhoneContact = ['_' => 'savedPhoneContact', 'phone' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'date' => int];
```  
