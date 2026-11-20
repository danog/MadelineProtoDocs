# privacyValueAllowUsers

> Allow only certain users

[Back to constructors index](/API_docs/constructors/index.html)



Allow only certain users

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [long](/API_docs/types/long.html) | Yes|Allowed users|



### Type: [PrivacyRule](/API_docs/types/PrivacyRule.html)


### Example:

```
$privacyValueAllowUsers = ['_' => 'privacyValueAllowUsers', 'users' => [long, long]];
```
