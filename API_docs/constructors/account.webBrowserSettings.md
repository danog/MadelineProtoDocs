# account.webBrowserSettings

> account.webBrowserSettings attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|open\_external\_browser|[Bool](/API_docs/types/Bool.html) | Optional|
|display\_close\_button|[Bool](/API_docs/types/Bool.html) | Optional|
|external\_exceptions|Array of [WebDomainException](/API_docs/types/WebDomainException.html) | Yes|
|inapp\_exceptions|Array of [WebDomainException](/API_docs/types/WebDomainException.html) | Yes|
|hash|[long](/API_docs/types/long.html) | Yes|



### Type: [account.WebBrowserSettings](/API_docs/types/account.WebBrowserSettings.html)


### Example:

```
$account_webBrowserSettings = ['_' => 'account.webBrowserSettings', 'open_external_browser' => Bool, 'display_close_button' => Bool, 'external_exceptions' => [WebDomainException, WebDomainException], 'inapp_exceptions' => [WebDomainException, WebDomainException], 'hash' => long];
```
