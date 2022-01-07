---
title: "updatePrivacy"
description: "Privacy rules were changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePrivacy  
[Back to constructors index](index.md)



Privacy rules were changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|key|[PrivacyKey](../types/PrivacyKey.md) | Yes|Peers to which the privacy rules apply|
|rules|Array of [PrivacyRule](../types/PrivacyRule.md) | Yes|New privacy rules|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePrivacy = ['_' => 'updatePrivacy', 'key' => PrivacyKey, 'rules' => [PrivacyRule, PrivacyRule]];
```  
