# payments.paymentVerificationNeeded

> Payment was not successful, additional verification is needed

[Back to constructors index](/API_docs/constructors/index.html)



Payment was not successful, additional verification is needed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.html) | Yes|URL for additional payment credentials verification|



### Type: [payments.PaymentResult](/API_docs/types/payments.PaymentResult.html)


### Example:

```
$payments_paymentVerificationNeeded = ['_' => 'payments.paymentVerificationNeeded', 'url' => 'string'];
```
