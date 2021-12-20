---
title: "account.autoDownloadSettings"
description: "Media autodownload settings"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_autoDownloadSettings.html
---
# Constructor: account.autoDownloadSettings  
[Back to constructors index](index.md)



Media autodownload settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|low|[AutoDownloadSettings](../types/AutoDownloadSettings.md) | Yes|Low data usage preset|
|medium|[AutoDownloadSettings](../types/AutoDownloadSettings.md) | Yes|Medium data usage preset|
|high|[AutoDownloadSettings](../types/AutoDownloadSettings.md) | Yes|High data usage preset|



### Type: [account.AutoDownloadSettings](../types/account.AutoDownloadSettings.md)


### Example:

```php
$account_autoDownloadSettings = ['_' => 'account.autoDownloadSettings', 'low' => AutoDownloadSettings, 'medium' => AutoDownloadSettings, 'high' => AutoDownloadSettings];
```  


Or, if you're into Lua:

```lua
account_autoDownloadSettings={_='account.autoDownloadSettings', low=AutoDownloadSettings, medium=AutoDownloadSettings, high=AutoDownloadSettings}

```


