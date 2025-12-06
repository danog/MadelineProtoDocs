---
title: "passkey"
description: "passkey attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: passkey  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[string](/API_docs/types/string.html) | Yes|
|name|[string](/API_docs/types/string.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|software\_emoji\_id|[long](/API_docs/types/long.html) | Optional|
|last\_usage\_date|[int](/API_docs/types/int.html) | Optional|



### Type: [Passkey](/API_docs/types/Passkey.html)


### Example:

```
$passkey = ['_' => 'passkey', 'id' => 'string', 'name' => 'string', 'date' => int, 'software_emoji_id' => long, 'last_usage_date' => int];
```  
