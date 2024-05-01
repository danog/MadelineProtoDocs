---
title: "account.autoDownloadSettings"
description: "Media autodownload settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_autoDownloadSettings.html
---
# Constructor: account.autoDownloadSettings  
[Back to constructors index](/API_docs/constructors/index.html)



Media autodownload settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|low|[AutoDownloadSettings](/API_docs/types/AutoDownloadSettings.html) | Yes|Low data usage preset|
|medium|[AutoDownloadSettings](/API_docs/types/AutoDownloadSettings.html) | Yes|Medium data usage preset|
|high|[AutoDownloadSettings](/API_docs/types/AutoDownloadSettings.html) | Yes|High data usage preset|



### Type: [account.AutoDownloadSettings](/API_docs/types/account.AutoDownloadSettings.html)


### Example:

```
$account_autoDownloadSettings = ['_' => 'account.autoDownloadSettings', 'low' => AutoDownloadSettings, 'medium' => AutoDownloadSettings, 'high' => AutoDownloadSettings];
```  
