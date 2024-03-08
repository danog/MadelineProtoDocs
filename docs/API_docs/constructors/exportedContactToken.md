---
title: "exportedContactToken"
description: "Describes a temporary profile link."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: exportedContactToken  
[Back to constructors index](/API_docs/constructors/index.html)



Describes a [temporary profile link](https://core.telegram.org/api/links#temporary-profile-links).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.html) | Yes|The [temporary profile link](https://core.telegram.org/api/links#temporary-profile-links).|
|expires|[int](/API_docs/types/int.html) | Yes|Its expiration date|



### Type: [ExportedContactToken](/API_docs/types/ExportedContactToken.html)


### Example:

```
$exportedContactToken = ['_' => 'exportedContactToken', 'url' => 'string', 'expires' => int];
```  
