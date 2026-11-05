# auth.exportedAuthorization

> Data for copying of authorization between data centers.

[Back to constructors index](/API_docs/constructors/index.html)



Data for copying of authorization between data centers.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|current user identifier|
|bytes|[bytes](/API_docs/types/bytes.html) | Yes|authorizes key|



### Type: [auth.ExportedAuthorization](/API_docs/types/auth.ExportedAuthorization.html)


### Example:

```
$auth_exportedAuthorization = ['_' => 'auth.exportedAuthorization', 'id' => long, 'bytes' => 'bytes'];
```
