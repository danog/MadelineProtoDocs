---
title: "smsjobs.status"
description: "smsjobs.status attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/smsjobs_status.html
---
# Constructor: smsjobs.status  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|allow\_international|[Bool](/API_docs/types/Bool.html) | Optional|
|recent\_sent|[int](/API_docs/types/int.html) | Yes|
|recent\_since|[int](/API_docs/types/int.html) | Yes|
|recent\_remains|[int](/API_docs/types/int.html) | Yes|
|total\_sent|[int](/API_docs/types/int.html) | Yes|
|total\_since|[int](/API_docs/types/int.html) | Yes|
|last\_gift\_slug|[string](/API_docs/types/string.html) | Optional|
|terms\_url|[string](/API_docs/types/string.html) | Yes|



### Type: [smsjobs.Status](/API_docs/types/smsjobs.Status.html)


### Example:

```
$smsjobs_status = ['_' => 'smsjobs.status', 'allow_international' => Bool, 'recent_sent' => int, 'recent_since' => int, 'recent_remains' => int, 'total_sent' => int, 'total_since' => int, 'last_gift_slug' => 'string', 'terms_url' => 'string'];
```  
