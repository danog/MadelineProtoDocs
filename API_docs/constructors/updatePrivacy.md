# updatePrivacy

> Privacy rules were changed

[Back to constructors index](/API_docs/constructors/index.html)



Privacy rules were changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|key|[PrivacyKey](/API_docs/types/PrivacyKey.html) | Yes|Peers to which the privacy rules apply|
|rules|Array of [PrivacyRule](/API_docs/types/PrivacyRule.html) | Yes|New privacy rules|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePrivacy = ['_' => 'updatePrivacy', 'key' => PrivacyKey, 'rules' => [PrivacyRule, PrivacyRule]];
```
