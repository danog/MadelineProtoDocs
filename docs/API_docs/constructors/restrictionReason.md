---
title: "restrictionReason"
description: "Restriction reason."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: restrictionReason  
[Back to constructors index](index.md)



Restriction reason.

Contains the reason why access to a certain object must be restricted. Clients are supposed to deny access to the channel if the `platform` field is equal to `all` or to the current platform (`ios`, `android`, `wp`, etc.). Platforms can be concatenated (`ios-android`, `ios-wp`), unknown platforms are to be ignored. The `text` is the error message that should be shown to the user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|platform|[string](../types/string.md) | Yes|Platform identifier (ios, android, wp, all, etc.), can be concatenated with a dash as separator (`android-ios`, `ios-wp`, etc)|
|reason|[string](../types/string.md) | Yes|Restriction reason (`porno`, `terms`, etc.)|
|text|[string](../types/string.md) | Yes|Error message to be shown to the user|



### Type: [RestrictionReason](../types/RestrictionReason.md)


### Example:

```php
$restrictionReason = ['_' => 'restrictionReason', 'platform' => 'string', 'reason' => 'string', 'text' => 'string'];
```  
