# inputPrivacyValueAllowUsers

> Allow only certain users

[Back to constructors index](/API_docs/constructors/index.html)



Allow only certain users

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Yes|Allowed users|



### Type: [InputPrivacyRule](/API_docs/types/InputPrivacyRule.html)


### Example:

```
$inputPrivacyValueAllowUsers = ['_' => 'inputPrivacyValueAllowUsers', 'users' => [InputUser, InputUser]];
```
