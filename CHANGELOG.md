# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to
[Semantic Versioning].

## Unreleased
### Fixed
- Allow transaction category to be any string. Monzo supports custom categories
  as part of their "Plus" plan.

## [v2.1.0](https://github.com/pawelad/pymonzo/releases/tag/v2.1.0) - 2024-04-16
### Added
- Add `rich` support to `MonzoPot`.

### Changed
- When using `rich`, make transaction title red if the amount is negative.
- Update `codecov/codecov-action` GitHub Action to v4.

## [v2.0.1](https://github.com/pawelad/pymonzo/releases/tag/v2.0.1) - 2024-04-13
### Fixed
- Monzo pot `goal_amount` is not always present (by [@csogilvie](https://github.com/csogilvie)).
  [[#32](https://github.com/pawelad/pymonzo/pull/32)]
- Add missing account types (by [@csogilvie](https://github.com/csogilvie)).
  [[#31](https://github.com/pawelad/pymonzo/pull/31)]
- Add missing space to `NoSettingsFile` exception message.

## [v2.0.0](https://github.com/pawelad/pymonzo/releases/tag/v2.0.0) - 2024-03-07
### Added
- Add (optional) `rich` and `babel` support.
- Add `expand_merchant` parameter to `TransactionsResource.list`. It's not very 
  clear in the API docs, but it works on that endpoint as well.
- Add custom `NoSettingsFile` exception. It's raised when the access token wasn't
  passed explicitly to `MonzoAPI()` and the settings file couldn't be loaded.

### Changed
- Update `MonzoTransactionMerchant` schema with new fields returned by the API.
- Simplify `MonzoAPI` initialization.
  This (unfortunately) needed an API change because the current attributes (in 
  hindsight) didn't really make sense.
  Now, you can either use an already generated (and temporary) access
  token, or generate it with `MonzoAPI.authorize()` and load from disk.

### Fixed
- Make `MonzoTransaction.settled` validator run in `before` mode.
- Add new `MonzoTransactionDeclineReason` values missing from Monzo API docs.
- Add new `MonzoTransactionCategory` values missing from Monzo API docs.
- Remove Markdown links from PyPI package description.

## [v1.0.0](https://github.com/pawelad/pymonzo/releases/tag/v1.0.0) - 2024-02-04
### Changed
- Project refresh.

## [v0.11.0](https://github.com/pawelad/pymonzo/releases/tag/v0.11.0) - 2018-02-16
### Added
- Made redirect URI, token file name and token path configurable via
  environment variables. (#14)
- Added Monzo Pots API endpoint - thanks @Sheaffy! (#13)

### Changed
- Renamed `config.PYMONZO_REDIRECT_URI` to `config.REDIRECT_URI`.

## [v0.10.3](https://github.com/pawelad/pymonzo/releases/tag/v0.10.3) - 2017-10-15
### Fixed
- Fixed saving token file to disk. (#9)

## [v0.10.2](https://github.com/pawelad/pymonzo/releases/tag/v0.10.2) - 2017-10-05
### Fixed
- Fixed automatic token refreshing - thanks @bartonp! (#5)

### Changed
- `MonzoAPI()._refresh_oath_token()` now doesn't return anything, replaces
  current token and raises `CantRefreshTokenError` when token couldn't be
  refreshed.
- Client secret is now saved in token file JSON file.
- Cleaned up exceptions.

## [v0.10.1](https://github.com/pawelad/pymonzo/releases/tag/v0.10.1) - 2017-09-24
### Fixed
- Try to refresh token if API request returned HTTP 401 (which could mean that
  the token is expired). (#6)

## [v0.10.0](https://github.com/pawelad/pymonzo/releases/tag/v0.10.0) - 2017-09-22
### Changed
 - Changed token file format from `shelve` to JSON. Because of that the file
   will need to be regenerated. (#3)
 - Updated `six` library to version 1.11.0.

## [v0.9.1](https://github.com/pawelad/pymonzo/releases/tag/v0.9.1) - 2017-09-21
### Deprecated
 - Added deprecation warning about changing token file format from `shelve`
   to JSON in next release. Because of that the file will need to be
   regenerated. (#4)

## [v0.9.0](https://github.com/pawelad/pymonzo/releases/tag/v0.9.0) - 2017-09-17
### Added
- Started keeping a changelog.

### Changed
- Major test suite overhaul.
- Code cleanup.


[keep a changelog]: https://keepachangelog.com/en/1.1.0/
[semantic versioning]: https://semver.org/spec/v2.0.0.html
