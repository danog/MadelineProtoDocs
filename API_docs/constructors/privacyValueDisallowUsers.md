# privacyValueDisallowUsers

> Disallow only certain users

[Back to constructors index](/API_docs/constructors/index.html)



Disallow only certain users

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [long](/API_docs/types/long.html) | Yes|Disallowed users|



### Type: [PrivacyRule](/API_docs/types/PrivacyRule.html)


### Example:

```
$privacyValueDisallowUsers = ['_' => 'privacyValueDisallowUsers', 'users' => [long, long]];
```
