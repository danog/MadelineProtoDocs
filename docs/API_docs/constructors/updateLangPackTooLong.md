---
title: "updateLangPackTooLong"
description: "A language pack has changed, the client should manually fetch the changed strings using langpack.getDifference"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateLangPackTooLong  
[Back to constructors index](/API_docs/constructors/index.html)



A language pack has changed, the client should manually fetch the changed strings using [langpack.getDifference](../methods/langpack.getDifference.html)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|lang\_code|[string](/API_docs/types/string.html) | Yes|Language code|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateLangPackTooLong = ['_' => 'updateLangPackTooLong', 'lang_code' => 'string'];
```  
