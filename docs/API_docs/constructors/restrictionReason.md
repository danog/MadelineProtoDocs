---
title: "restrictionReason"
description: "Restriction reason."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: restrictionReason  
[Back to constructors index](/API_docs/constructors/index.html)



Restriction reason.

See [here »](https://core.telegram.org/api/age-verification) for the full flow to use for restricted or age-gated content.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|platform|[string](/API_docs/types/string.html) | Yes|Platform identifier (ios, android, wp, all, etc.), can be concatenated with a dash as separator (`android-ios`, `ios-wp`, etc)|
|reason|[string](/API_docs/types/string.html) | Yes|Restriction reason (`porno`, `terms`, etc.). Ignore this restriction reason if it is contained in the [ignore\_restriction\_reasons »](https://core.telegram.org/api/config#ignore-restriction-reasons) client configuration parameter.|
|text|[string](/API_docs/types/string.html) | Yes|Error message to be shown to the user|



### Type: [RestrictionReason](/API_docs/types/RestrictionReason.html)


### Example:

```
$restrictionReason = ['_' => 'restrictionReason', 'platform' => 'string', 'reason' => 'string', 'text' => 'string'];
```  
