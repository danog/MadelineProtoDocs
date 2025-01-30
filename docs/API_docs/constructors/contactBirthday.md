---
title: "contactBirthday"
description: "Birthday information of a contact."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contactBirthday  
[Back to constructors index](/API_docs/constructors/index.html)



Birthday information of a contact.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|contact\_id|[long](/API_docs/types/long.html) | Yes|User ID.|
|birthday|[Birthday](/API_docs/types/Birthday.html) | Yes|Birthday information.|



### Type: [ContactBirthday](/API_docs/types/ContactBirthday.html)


### Example:

```
$contactBirthday = ['_' => 'contactBirthday', 'contact_id' => long, 'birthday' => Birthday];
```  
