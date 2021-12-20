---
title: "account.contentSettings"
description: "Sensitive content settings"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_contentSettings.html
---
# Constructor: account.contentSettings  
[Back to constructors index](index.md)



Sensitive content settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|sensitive\_enabled|[Bool](../types/Bool.md) | Optional|Whether viewing of sensitive (NSFW) content is enabled|
|sensitive\_can\_change|[Bool](../types/Bool.md) | Optional|Whether the current client can change the sensitive content settings to view NSFW content|



### Type: [account.ContentSettings](../types/account.ContentSettings.md)


### Example:

```php
$account_contentSettings = ['_' => 'account.contentSettings', 'sensitive_enabled' => Bool, 'sensitive_can_change' => Bool];
```  


Or, if you're into Lua:

```lua
account_contentSettings={_='account.contentSettings', sensitive_enabled=Bool, sensitive_can_change=Bool}

```


