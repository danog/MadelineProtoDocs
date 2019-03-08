---
title: updatePrivacy
description: Update privacy
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePrivacy  
[Back to constructors index](index.md)



Update privacy

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|key|[PrivacyKey](../types/PrivacyKey.md) | Yes|Key|
|rules|Array of [PrivacyRule](../types/PrivacyRule.md) | Yes|Rules|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePrivacy = ['_' => 'updatePrivacy', 'key' => PrivacyKey, 'rules' => [PrivacyRule, PrivacyRule]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updatePrivacy", "key": PrivacyKey, "rules": [PrivacyRule]}
```


Or, if you're into Lua:

```lua
updatePrivacy={_='updatePrivacy', key=PrivacyKey, rules={PrivacyRule}}

```


