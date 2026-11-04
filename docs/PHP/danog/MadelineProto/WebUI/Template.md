---
title: "danog\\MadelineProto\\WebUI\\Template: A template being rendered: `$this` inside a .phtml template."
description: "\nTemplates can extend a layout and fill its sections:\n\n```php\n<?php $this->layout('layout', ['title' => $page->title]) ?>\n<?php $this->start('head') ?><style>...</style><?php $this->stop() ?>\n<p>The rest of the output becomes the \"content\" section of the layout.</p>\n```\n\nUse {@see self::e()} to output any value: strings are escaped, {@see SafeHtml} is output as-is.\n"
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\WebUI\Template`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

A template being rendered: `$this` inside a .phtml template.  


Templates can extend a layout and fill its sections:

```php
<?php $this->layout('layout', ['title' => $page->title]) ?>
<?php $this->start('head') ?><style>...</style><?php $this->stop() ?>
<p>The rest of the output becomes the "content" section of the layout.</p>
```

Use {@see self::e()} to output any value: strings are escaped, {@see SafeHtml} is output as-is.



## Method list:
* [`getEngine(): \danog\MadelineProto\WebUI\TemplateEngine`](#getEngine)
* [`layout(string $name, array<string, mixed> $data = []): void`](#layout)
* [`start(string $name): void`](#start)
* [`stop(): void`](#stop)
* [`section(string $name, string $default = ''): \danog\MadelineProto\WebUI\SafeHtml`](#section)
* [`hasSection(string $name): bool`](#hasSection)
* [`insert(string $name, array<string, mixed> $data = []): \danog\MadelineProto\WebUI\SafeHtml`](#insert)
* [`asset(string $file): \danog\MadelineProto\WebUI\SafeHtml`](#asset)
* [`script(string $file): \danog\MadelineProto\WebUI\SafeHtml`](#script)
* [`escapeScript(string $script): string`](#escapeScript)
* [`e(mixed $value): string`](#e)
* [`attrs(array<string, (scalar|\Stringable|null)> $attributes): \danog\MadelineProto\WebUI\SafeHtml`](#attrs)
* [`t(string $key, (string|int|float) ...$args): string`](#t)
* [`tHtml(string $key, (string|int|float) ...$args): \danog\MadelineProto\WebUI\SafeHtml`](#tHtml)
* [`translate(string $key, (string|int|float) ...$args): string`](#translate)

## Methods:
### <a name="getEngine"></a> `getEngine(): \danog\MadelineProto\WebUI\TemplateEngine`

Get the template engine.


#### See also: 
* [`\danog\MadelineProto\WebUI\TemplateEngine`: Renders the native PHP templates of the web UI.](../../../danog/MadelineProto/WebUI/TemplateEngine.html)




### <a name="layout"></a> `layout(string $name, array<string, mixed> $data = []): void`

Extend a layout: the output of this template becomes its `content` section.


Parameters:

* `$name`: `string`   
* `$data`: `array<string, mixed>` Additional variables for the layout  



### <a name="start"></a> `start(string $name): void`

Start capturing a section.


Parameters:

* `$name`: `string`   



### <a name="stop"></a> `stop(): void`

Stop capturing the current section.



### <a name="section"></a> `section(string $name, string $default = ''): \danog\MadelineProto\WebUI\SafeHtml`

Output a section.


Parameters:

* `$name`: `string`   
* `$default`: `string` Default HTML if the section was not filled  


#### See also: 
* [`\danog\MadelineProto\WebUI\SafeHtml`: A trusted HTML fragment, output as-is by templates instead of being escaped.](../../../danog/MadelineProto/WebUI/SafeHtml.html)




### <a name="hasSection"></a> `hasSection(string $name): bool`

Check whether a section was filled.


Parameters:

* `$name`: `string`   



### <a name="insert"></a> `insert(string $name, array<string, mixed> $data = []): \danog\MadelineProto\WebUI\SafeHtml`

Render another template (partial) in place.


Parameters:

* `$name`: `string`   
* `$data`: `array<string, mixed>` Variables passed to the template  


#### See also: 
* [`\danog\MadelineProto\WebUI\SafeHtml`: A trusted HTML fragment, output as-is by templates instead of being escaped.](../../../danog/MadelineProto/WebUI/SafeHtml.html)




### <a name="asset"></a> `asset(string $file): \danog\MadelineProto\WebUI\SafeHtml`

Get the contents of an asset, to inline it in a `<style>` or `<script>` tag.


Parameters:

* `$file`: `string`   


#### See also: 
* [`\danog\MadelineProto\WebUI\SafeHtml`: A trusted HTML fragment, output as-is by templates instead of being escaped.](../../../danog/MadelineProto/WebUI/SafeHtml.html)




### <a name="script"></a> `script(string $file): \danog\MadelineProto\WebUI\SafeHtml`

Get the contents of a script asset, to inline it in a `<script>` tag.
  
A `</script` in the script (in a string literal, or in a comment) would close the tag early, and a  
`<!--` followed by `<script` would keep the real `</script>` from closing it: they're escaped to  
`<\/script` and `<\!--`, which mean the same in JavaScript strings and comments.  


Parameters:

* `$file`: `string`   


#### See also: 
* [`\danog\MadelineProto\WebUI\SafeHtml`: A trusted HTML fragment, output as-is by templates instead of being escaped.](../../../danog/MadelineProto/WebUI/SafeHtml.html)




### <a name="escapeScript"></a> `escapeScript(string $script): string`

Escape a script to inline it in a `<script>` tag, see {@see self::script()}.


Parameters:

* `$script`: `string`   



### <a name="e"></a> `e(mixed $value): string`

Escape a value for output in HTML text or in a quoted attribute.


Parameters:

* `$value`: `mixed`   



### <a name="attrs"></a> `attrs(array<string, (scalar|\Stringable|null)> $attributes): \danog\MadelineProto\WebUI\SafeHtml`

Build an HTML attribute list: `true` outputs just the name, `null` and `false` skip the attribute.


Parameters:

* `$attributes`: `array<string, (scalar|\Stringable|null)>`   


#### See also: 
* `scalar`
* `\Stringable`
* [`\danog\MadelineProto\WebUI\SafeHtml`: A trusted HTML fragment, output as-is by templates instead of being escaped.](../../../danog/MadelineProto/WebUI/SafeHtml.html)




### <a name="t"></a> `t(string $key, (string|int|float) ...$args): string`

Translate a string, escaping it.


Parameters:

* `$key`: `string`   
* `...$args`: `(string|int|float)` sprintf arguments  



### <a name="tHtml"></a> `tHtml(string $key, (string|int|float) ...$args): \danog\MadelineProto\WebUI\SafeHtml`

Translate a string that contains trusted HTML (like links), escaping only the arguments.


Parameters:

* `$key`: `string`   
* `...$args`: `(string|int|float)` sprintf arguments  


#### See also: 
* [`\danog\MadelineProto\WebUI\SafeHtml`: A trusted HTML fragment, output as-is by templates instead of being escaped.](../../../danog/MadelineProto/WebUI/SafeHtml.html)




### <a name="translate"></a> `translate(string $key, (string|int|float) ...$args): string`

Translate a string.


Parameters:

* `$key`: `string`   
* `...$args`: `(string|int|float)` sprintf arguments  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
