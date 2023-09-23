---
title: "updateNewAuthorization"
description: "updateNewAuthorization attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewAuthorization  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|unconfirmed|[Bool](/API_docs/types/Bool.html) | Optional|
|hash|[long](/API_docs/types/long.html) | Yes|
|date|[int](/API_docs/types/int.html) | Optional|
|device|[string](/API_docs/types/string.html) | Optional|
|location|[string](/API_docs/types/string.html) | Optional|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateNewAuthorization = ['_' => 'updateNewAuthorization', 'unconfirmed' => Bool, 'hash' => long, 'date' => int, 'device' => 'string', 'location' => 'string'];
```  
