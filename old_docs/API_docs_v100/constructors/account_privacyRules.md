---
title: account.privacyRules
description: Privacy rules
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.privacyRules  
[Back to constructors index](index.md)



Privacy rules

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|rules|Array of [PrivacyRule](../types/PrivacyRule.md) | Yes|Rules|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats allowed?|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [account\_PrivacyRules](../types/account_PrivacyRules.md)


### Example:

```php
$account_privacyRules = ['_' => 'account.privacyRules', 'rules' => [PrivacyRule, PrivacyRule], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
account_privacyRules={_='account.privacyRules', rules={PrivacyRule}, chats={Chat}, users={User}}

```


