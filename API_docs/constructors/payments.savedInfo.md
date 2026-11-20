# payments.savedInfo

> Saved server-side order information

[Back to constructors index](/API_docs/constructors/index.html)



Saved server-side order information

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_saved\_credentials|[Bool](/API_docs/types/Bool.html) | Optional|Whether the user has some saved payment credentials|
|saved\_info|[PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.html) | Optional|Saved server-side order information|



### Type: [payments.SavedInfo](/API_docs/types/payments.SavedInfo.html)


### Example:

```
$payments_savedInfo = ['_' => 'payments.savedInfo', 'has_saved_credentials' => Bool, 'saved_info' => PaymentRequestedInfo];
```
