---
title: "danog\\MadelineProto\\Namespace\\Langpack: "
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Namespace\Langpack`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

  




## Method list:
* [`getLangPack(string $lang_pack = '', string $lang_code = ''): array{_: \"langPackDifference", lang_code: string, from_version: int, version: int, strings: \list<array{_: "langPackString", key: string, value: string}|array{_: "langPackStringPluralized", key: string, zero_value: string, one_value: string, two_value: string, few_value: string, many_value: string, other_value: string}|array{_: "langPackStringDeleted", key: string}>} @see https://docs.madelineproto.xyz/API_docs/types/LangPackDifference.htm}`](#getlangpack-string-lang_pack-string-lang_code-array-_-langpackdifference-lang_code-string-from_version-int-version-int-strings-list-array-_-langpackstring-key-string-value-string-array-_-langpackstringpluralized-key-string-zero_value-string-one_value-string-two_value-string-few_value-string-many_value-string-other_value-string-array-_-langpackstringdeleted-key-string-see-https-docs-madelineproto-xyz-api_docs-types-langpackdifference-htm)
* [`getStrings(string $lang_pack = '', string $lang_code = '', list<string> $keys = []): \list<array{_: "langPackString", key: string, value: string}|array{_: "langPackStringPluralized", key: string, zero_value: string, one_value: string, two_value: string, few_value: string, many_value: string, other_value: string}|array{_: "langPackStringDeleted", key: string}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/LangPackString.html`](#getstrings-string-lang_pack-string-lang_code-list-string-keys-list-array-_-langpackstring-key-string-value-string-array-_-langpackstringpluralized-key-string-zero_value-string-one_value-string-two_value-string-few_value-string-many_value-string-other_value-string-array-_-langpackstringdeleted-key-string-array-of-see-https-docs-madelineproto-xyz-api_docs-types-langpackstring-html)
* [`getDifference(string $lang_pack = '', string $lang_code = '', int $from_version = 0): array{_: \"langPackDifference", lang_code: string, from_version: int, version: int, strings: \list<array{_: "langPackString", key: string, value: string}|array{_: "langPackStringPluralized", key: string, zero_value: string, one_value: string, two_value: string, few_value: string, many_value: string, other_value: string}|array{_: "langPackStringDeleted", key: string}>} @see https://docs.madelineproto.xyz/API_docs/types/LangPackDifference.htm}`](#getdifference-string-lang_pack-string-lang_code-int-from_version-0-array-_-langpackdifference-lang_code-string-from_version-int-version-int-strings-list-array-_-langpackstring-key-string-value-string-array-_-langpackstringpluralized-key-string-zero_value-string-one_value-string-two_value-string-few_value-string-many_value-string-other_value-string-array-_-langpackstringdeleted-key-string-see-https-docs-madelineproto-xyz-api_docs-types-langpackdifference-htm)
* [`getLanguages(string $lang_pack = ''): \list<array{_: "langPackLanguage", official: bool, rtl: bool, beta: bool, name: string, native_name: string, lang_code: string, base_lang_code: string, plural_code: string, strings_count: int, translated_count: int, translations_url: string}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/LangPackLanguage.html`](#getlanguages-string-lang_pack-list-array-_-langpacklanguage-official-bool-rtl-bool-beta-bool-name-string-native_name-string-lang_code-string-base_lang_code-string-plural_code-string-strings_count-int-translated_count-int-translations_url-string-array-of-see-https-docs-madelineproto-xyz-api_docs-types-langpacklanguage-html)
* [`getLanguage(string $lang_pack = '', string $lang_code = ''): array{_: \"langPackLanguage", official: bool, rtl: bool, beta: bool, name: string, native_name: string, lang_code: string, base_lang_code: string, plural_code: string, strings_count: int, translated_count: int, translations_url: \string} @see https://docs.madelineproto.xyz/API_docs/types/LangPackLanguage.htm}`](#getlanguage-string-lang_pack-string-lang_code-array-_-langpacklanguage-official-bool-rtl-bool-beta-bool-name-string-native_name-string-lang_code-string-base_lang_code-string-plural_code-string-strings_count-int-translated_count-int-translations_url-string-see-https-docs-madelineproto-xyz-api_docs-types-langpacklanguage-htm)

## Methods:
### `getLangPack(string $lang_pack = '', string $lang_code = ''): array{_: \"langPackDifference", lang_code: string, from_version: int, version: int, strings: \list<array{_: "langPackString", key: string, value: string}|array{_: "langPackStringPluralized", key: string, zero_value: string, one_value: string, two_value: string, few_value: string, many_value: string, other_value: string}|array{_: "langPackStringDeleted", key: string}>} @see https://docs.madelineproto.xyz/API_docs/types/LangPackDifference.htm}`

Get localization pack strings


Parameters:

* `$lang_pack`: `string` Language pack name, usually obtained from a [language pack link](https://core.telegram.org/api/links#language-pack-links)  
* `$lang_code`: `string` Language code  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/LangPackDifference.html


### `getStrings(string $lang_pack = '', string $lang_code = '', list<string> $keys = []): \list<array{_: "langPackString", key: string, value: string}|array{_: "langPackStringPluralized", key: string, zero_value: string, one_value: string, two_value: string, few_value: string, many_value: string, other_value: string}|array{_: "langPackStringDeleted", key: string}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/LangPackString.html`

Get strings from a language pack


Parameters:

* `$lang_pack`: `string` Language pack name, usually obtained from a [language pack link](https://core.telegram.org/api/links#language-pack-links)  
* `$lang_code`: `string` Language code  
* `$keys`: `list<string>` Strings to get  


Return value: Array of  @see https://docs.madelineproto.xyz/API_docs/types/LangPackString.html


### `getDifference(string $lang_pack = '', string $lang_code = '', int $from_version = 0): array{_: \"langPackDifference", lang_code: string, from_version: int, version: int, strings: \list<array{_: "langPackString", key: string, value: string}|array{_: "langPackStringPluralized", key: string, zero_value: string, one_value: string, two_value: string, few_value: string, many_value: string, other_value: string}|array{_: "langPackStringDeleted", key: string}>} @see https://docs.madelineproto.xyz/API_docs/types/LangPackDifference.htm}`

Get new strings in language pack


Parameters:

* `$lang_pack`: `string` Language pack  
* `$lang_code`: `string` Language code  
* `$from_version`: `int` Previous localization pack version  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/LangPackDifference.html


### `getLanguages(string $lang_pack = ''): \list<array{_: "langPackLanguage", official: bool, rtl: bool, beta: bool, name: string, native_name: string, lang_code: string, base_lang_code: string, plural_code: string, strings_count: int, translated_count: int, translations_url: string}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/LangPackLanguage.html`

Get information about all languages in a localization pack


Parameters:

* `$lang_pack`: `string` Language pack  


Return value: Array of  @see https://docs.madelineproto.xyz/API_docs/types/LangPackLanguage.html


### `getLanguage(string $lang_pack = '', string $lang_code = ''): array{_: \"langPackLanguage", official: bool, rtl: bool, beta: bool, name: string, native_name: string, lang_code: string, base_lang_code: string, plural_code: string, strings_count: int, translated_count: int, translations_url: \string} @see https://docs.madelineproto.xyz/API_docs/types/LangPackLanguage.htm}`

Get information about a language in a localization pack


Parameters:

* `$lang_pack`: `string` Language pack name, usually obtained from a [language pack link](https://core.telegram.org/api/links#language-pack-links)  
* `$lang_code`: `string` Language code  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/LangPackLanguage.html


---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
