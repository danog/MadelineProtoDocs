# account.autoDownloadSettings

> Media autodownload settings

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
