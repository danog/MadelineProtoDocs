---
title: account.autoDownloadSettings
description: Autodownload settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.autoDownloadSettings  
[Back to constructors index](index.md)



Autodownload settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|low|[AutoDownloadSettings](../types/AutoDownloadSettings.md) | Yes|Low preset?|
|medium|[AutoDownloadSettings](../types/AutoDownloadSettings.md) | Yes|Medium preset?|
|high|[AutoDownloadSettings](../types/AutoDownloadSettings.md) | Yes|High preset?|



### Type: [account\_AutoDownloadSettings](../types/account_AutoDownloadSettings.md)


### Example:

```php
$account_autoDownloadSettings = ['_' => 'account.autoDownloadSettings', 'low' => AutoDownloadSettings, 'medium' => AutoDownloadSettings, 'high' => AutoDownloadSettings];
```  


Or, if you're into Lua:

```lua
account_autoDownloadSettings={_='account.autoDownloadSettings', low=AutoDownloadSettings, medium=AutoDownloadSettings, high=AutoDownloadSettings}

```


