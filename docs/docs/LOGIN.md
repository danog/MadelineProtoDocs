---
title: "Login"
description: "There are many ways you can login with MadelineProto."
nav_order: 5
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Login

There are many ways you can login with MadelineProto.

* [Getting permission to use the telegram API](#getting-permission-to-use-the-telegram-api)
* [Automatic](#automatic)
* [Manual (user)](#manual-user)
  * [API ID](#api-id)
* [Manual (bot)](#manual-bot)
* [QR code login (user)](#qr-code-user)

## Getting permission to use the telegram API

Before you start using MadelineProto with the Telegram API, you have to understand that Telegram strictly controls userbots created on their platform.  

If you use MadelineProto or any other Telegram client, **including official clients**, for flooding, spamming, botting channels, you **will be banned forever**.  

Due to excessive abuse of the Telegram API, **all phone numbers** that sign up or log in using **even official or approved by telegram** API clients like MadelineProto are automatically put **under observation**, and __may__ get banned **even if you did nothing wrong**, simply because some internal flags are triggered in the **telegram servers**.  

To avoid this, you must let telegram know that you will use your account with a userbot:  
When or before you first sign up or login you have to **send an email with the phone number to [recover@telegram.org](mailto:recover@telegram.org)**; explaining **what will your userbot do**.  
**DO NOT LIE**, just tell them **what will you do with the userbot** you intend to create, asking them to not ban your account.  

If your account does get banned, write to [recover@telegram.org](mailto:recover@telegram.org) asking to unban it.  

**DO NOT ABUSE OF THIS OR ANY OTHER API FOR FLOODING; SPAMMING; BOTTING**; the consequences will fall not only on you, but on all other users of this and other libraries, and even normal users.  

There were cases when several **normal user accounts that did nothing wrong** were banned when telegram deployed a new spambot detection system: this is bad for the community, and it is bad for Telegram, so please do not abuse.  


## Automatic

```php
$MadelineProto->start();
```

This will start an interactive login prompt via console (if running via CLI), or a login web UI (if running in the browser).  
You will get to choose if login as user, or as bot.

When using the [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html), use the static `startAndLoop` method, instead:

```php
MyEventHandler::startAndLoop('session.madeline', $settings);
```

No explicit `$MadelineProto` instance is required or allowed when using the event handler.


## Manual (user)

Before logging in, you must obtain an [API ID](https://docs.madelineproto.xyz/docs/SETTINGS.html) (if you're using the [automatic mode you don't have to do this](#automatic)).  
You can do that by logging in to [my.telegram.org](https://my.telegram.org) and getting your API ID/hash.

After you provide an API ID [in the settings](https://docs.madelineproto.xyz/docs/SETTINGS.html), you can then login (if you're using the [automatic mode you don't have to do this](#automatic)).  

```php
use danog\MadelineProto\Tools;

$MadelineProto->phoneLogin(Tools::readLine('Enter your phone number: '));
$authorization = $MadelineProto->completePhoneLogin(Tools::readLine('Enter the phone code: '));
if ($authorization['_'] === 'account.password') {
    $authorization = $MadelineProto->complete2falogin(Tools::readLine('Please enter your password (hint '.$authorization['hint'].'): '));
}
if ($authorization['_'] === 'account.needSignup') {
    $authorization = $MadelineProto->completeSignup(Tools::readLine('Please enter your first name: '), readline('Please enter your last name (can be empty): '));
}
```

First, you must call `phoneLogin` to send the verification code, see [here for the parameters and the result](https://docs.madelineproto.xyz/phoneLogin.html).  
Then, use `completePhoneLogin` to complete the login, see [here for the parameters and the result](https://docs.madelineproto.xyz/completePhoneLogin.html).  

Use `complete2falogin` to complete the login to an account with 2FA enabled, see [here for the parameters and the result](https://docs.madelineproto.xyz/complete2FALogin.html).  

If the account does not have an account, use `completeSignup` to signup, see [here for the parameters and the result](https://docs.madelineproto.xyz/completeSignup.html).  


## Manual (bot)

```php
$MadelineProto->botLogin('34298141894:aflknsaflknLKNFS');
```

Use `botLogin` to login as a bot, see [here for the parameters and the result](https://docs.madelineproto.xyz/botLogin.html).  

## QR code (user)

The new QR code login API can be used to render a QR code that can be scanned using the Telegram mobile apps in order to login.  

The API is designed to be easily used in parallel with another login mode (i.e. together with the manual modes described above), but it can also be used standalone.  

[See here for the full documentation of the QR code API &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/TL/Types/LoginQrCode.html).  

### CLI usage example

```php
use Amp\CancelledException;
use Amp\CompositeCancellation;
use Amp\TimeoutCancellation;
use danog\MadelineProto\TL\Types\LoginQrCode;
use danog\MadelineProto\API;
use danog\MadelineProto\Tools;

function login(\danog\MadelineProto\API $MadelineProto): void {
    do {
        $qr = $MadelineProto->qrLogin();
        if (!$qr) {
            if ($MadelineProto->getAuthorization() === API::WAITING_PASSWORD) {
                $MadelineProto->complete2faLogin(Tools::readLine('Please enter your password (hint '.$MadelineProto->getHint().'): '));
            }
            // If null, we're already logged in
            return;
        }

        // Print QR code in text format
        echo $qr->getQRText();

        $expire = $qr->getExpirationCancellation();
        $login = $qr->getLoginCancellation();

        $cancel = new CompositeCancellation($expire, $login);

        try {
            $result = Tools::readLine("Enter your phone number, or scan the above QR code to login: ", $cancel);
            break;
        } catch (CancelledException) {
            if ($login->isRequested()) {
                echo(PHP_EOL.PHP_EOL."QR code login successful!".PHP_EOL);
                if ($MadelineProto->getAuthorization() === API::WAITING_PASSWORD) {
                    $MadelineProto->complete2faLogin(Tools::readLine('Please enter your password (hint '.$MadelineProto->getHint().'): '));
                }
                return;
            }
            echo(PHP_EOL."The QR code expired, generating a new one...".PHP_EOL);
        }
    } while (true);

    $MadelineProto->phoneLogin($result);
    $authorization = $MadelineProto->completePhoneLogin(Tools::readLine('Enter the phone code: '));
    if ($authorization['_'] === 'account.password') {
        $MadelineProto->complete2falogin(Tools::readLine('Please enter your password (hint '.$authorization['hint'].'): '));
    }
    if ($authorization['_'] === 'account.needSignup') {
        $MadelineProto->completeSignup(Tools::readLine('Please enter your first name: '), Tools::readline('Please enter your last name (can be empty): '));
    }
}
```

### Web usage example

In this example, two endpoints are offered:

* `?waitQrCodeOrLogin` long-polls the QR login API, waiting for the QR code to expire or for the user to scan the code.
  * If the QR code expires, a new SVG with the QR code is returned in a JSON payload.
  * If the user scans the code and approves login through a Telegram app, the `logged_in` field in the returned JSON payload is set to true. If the user has also set a 2FA password, the `needs_2fa` field will `true` and the web UI will have to ask for a password and invoke `complete2falogin`.
* `?getQrCode` does the same as `?waitQrCodeOrLogin`, except that it doesn't wait the additional 5 seconds (useful to fetch an initial QR code upon first page load).  

```php
use Amp\CancelledException;
use Amp\CompositeCancellation;
use Amp\TimeoutCancellation;
use danog\MadelineProto\TL\Types\LoginQrCode;
use danog\MadelineProto\API;

if (isset($_GET['waitQrCodeOrLogin']) || isset($_GET['getQrCode'])) {
    \header('Content-type: application/json');
    try {
        $qr = $MadelineProto->qrLogin();
        if (isset($_GET['waitQrCodeOrLogin'])) {
            $qr = $qr?->waitForLoginOrQrCodeExpiration(new TimeoutCancellation(5.0));
        }
    } catch (CancelledException) {
        $qr = $MadelineProto->qrLogin();
    }
    if ($qr) {
        $result = [
            'logged_in' => false,
            'svg' => $qr->getQRSvg(400, 2)
        ];
    } else {
        $result = [
            'logged_in' => true,
            'needs_2fa' => $MadelineProto->getAuthorization() === MTProto::WAITING_PASSWORD
        ];
    }
    echo(\json_encode($result));
}
```

<a href="https://docs.madelineproto.xyz/docs/FEATURES.html">Next section</a>