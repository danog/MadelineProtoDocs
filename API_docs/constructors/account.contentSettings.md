# account.contentSettings

> Sensitive content settings

[Back to constructors index](/API_docs/constructors/index.html)



Sensitive content settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|sensitive\_enabled|[Bool](/API_docs/types/Bool.html) | Optional|Whether viewing of sensitive (NSFW) content is enabled|
|sensitive\_can\_change|[Bool](/API_docs/types/Bool.html) | Optional|Whether the current client can change the sensitive content settings to view NSFW content|



### Type: [account.ContentSettings](/API_docs/types/account.ContentSettings.html)


### Example:

```
$account_contentSettings = ['_' => 'account.contentSettings', 'sensitive_enabled' => Bool, 'sensitive_can_change' => Bool];
```
