# messageActionSuggestedPostSuccess

> A suggested post » was successfully posted, and payment for it was successfully received.

[Back to constructors index](/API_docs/constructors/index.html)



A [suggested post »](https://core.telegram.org/api/suggested-posts) was successfully posted, and payment for it was successfully received.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|price|[StarsAmount](/API_docs/types/StarsAmount.html) | Yes|The price.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionSuggestedPostSuccess = ['_' => 'messageActionSuggestedPostSuccess', 'price' => StarsAmount];
```
