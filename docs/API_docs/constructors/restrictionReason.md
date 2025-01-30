---
title: "restrictionReason"
description: "Restriction reason."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: restrictionReason  
[Back to constructors index](/API_docs/constructors/index.html)



Restriction reason.

Contains the reason why access to a certain object must be restricted. Clients are supposed to deny access to the channel if the `platform` field is equal to `all` or to the current platform (`ios`, `android`, `wp`, etc.). Platforms can be concatenated (`ios-android`, `ios-wp`), unknown platforms are to be ignored. The `text` is the error message that should be shown to the user.

The [restriction\_add\_platforms »](https://core.telegram.org/api/config#restriction-add-platforms) client configuration parameter contains an array of platform identifiers that must also be treated as our own, in additional to the one hardcoded in the client.

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
