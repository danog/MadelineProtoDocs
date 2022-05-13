---
title: "auth.exportedAuthorization"
description: "Data for copying of authorization between data centers."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_exportedAuthorization.html
---
# Constructor: auth.exportedAuthorization  
[Back to constructors index](/API_docs/constructors/index.html)



Data for copying of authorization between data centers.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|current user identifier|
|bytes|[bytes](/API_docs/types/bytes.html) | Yes|authorizes key|



### Type: [auth.ExportedAuthorization](/API_docs/types/auth.ExportedAuthorization.html)


### Example:

```
$auth_exportedAuthorization = ['_' => 'auth.exportedAuthorization', 'id' => long, 'bytes' => 'bytes'];
```  
