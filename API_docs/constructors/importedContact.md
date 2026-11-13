# importedContact

> Successfully imported contact.

[Back to constructors index](/API_docs/constructors/index.html)



Successfully imported contact.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User identifier|
|client\_id|[long](/API_docs/types/long.html) | Yes|The contact's client identifier (passed to one of the [InputContact](../types/InputContact.html) constructors)|



### Type: [ImportedContact](/API_docs/types/ImportedContact.html)


### Example:

```
$importedContact = ['_' => 'importedContact', 'user_id' => long, 'client_id' => long];
```
