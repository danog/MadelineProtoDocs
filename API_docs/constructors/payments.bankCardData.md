# payments.bankCardData

> Credit card info, provided by the card's bank(s)

[Back to constructors index](/API_docs/constructors/index.html)



Credit card info, provided by the card's bank(s)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Yes|Credit card title|
|open\_urls|Array of [BankCardOpenUrl](/API_docs/types/BankCardOpenUrl.html) | Yes|Info URL(s) provided by the card's bank(s)|



### Type: [payments.BankCardData](/API_docs/types/payments.BankCardData.html)


### Example:

```
$payments_bankCardData = ['_' => 'payments.bankCardData', 'title' => 'string', 'open_urls' => [BankCardOpenUrl, BankCardOpenUrl]];
```
