# help.termsOfServiceUpdateEmpty

> No changes were made to telegram's terms of service

[Back to constructors index](/API_docs/constructors/index.html)



No changes were made to telegram's terms of service

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](/API_docs/types/int.html) | Yes|New TOS updates will have to be queried using [help.getTermsOfServiceUpdate](../methods/help.getTermsOfServiceUpdate.html) in `expires` seconds|



### Type: [help.TermsOfServiceUpdate](/API_docs/types/help.TermsOfServiceUpdate.html)


### Example:

```
$help_termsOfServiceUpdateEmpty = ['_' => 'help.termsOfServiceUpdateEmpty', 'expires' => int];
```
