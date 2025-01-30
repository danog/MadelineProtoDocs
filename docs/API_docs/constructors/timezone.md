---
title: "timezone"
description: "Timezone information."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: timezone  
[Back to constructors index](/API_docs/constructors/index.html)



Timezone information.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](/API_docs/types/string.html) | Yes|Unique timezone ID.|
|name|[string](/API_docs/types/string.html) | Yes|Human-readable and localized timezone name.|
|utc\_offset|[int](/API_docs/types/int.html) | Yes|UTC offset in seconds, which may be displayed in hh:mm format by the client together with the human-readable name (i.e. `$name UTC -01:00`).|



### Type: [Timezone](/API_docs/types/Timezone.html)


### Example:

```
$timezone = ['_' => 'timezone', 'id' => 'string', 'name' => 'string', 'utc_offset' => int];
```  
