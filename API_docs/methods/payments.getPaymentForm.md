# payments.getPaymentForm

> Get a payment form

[Back to methods index](index.html)



Get a payment form

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|invoice|[InputInvoice](/API_docs/types/InputInvoice.html) | Invoice | Yes|
|theme\_params|[DataJSON](/API_docs/types/DataJSON.html) | [Theme parameters »](https://core.telegram.org/api/bots/webapps#theme-parameters) | Optional|


### Return type: [payments.PaymentForm](/API_docs/types/payments.PaymentForm.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_PaymentForm = $MadelineProto->payments->getPaymentForm(invoice: $InputInvoice, theme_params: $DataJSON, );
```
