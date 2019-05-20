# Bulls&amp;Cows game
[![Python 2.7](https://img.shields.io/travis/vb64/bulls_cows.svg?label=Python%202.7&style=plastic)](https://travis-ci.org/vb64/bulls_cows)
[![Code Climate](https://img.shields.io/codeclimate/maintainability-percentage/vb64/bulls_cows.svg?label=Code%20Climate&style=plastic)](https://codeclimate.com/github/vb64/bulls_cows)
[![Coverage Status](https://coveralls.io/repos/github/vb64/bulls_cows/badge.svg?branch=master)](https://coveralls.io/github/vb64/bulls_cows?branch=master)

[Game rules](https://en.wikipedia.org/wiki/Bulls_and_Cows)

## Local game
```
$ git clone git@github.com:vb64/bulls_cows.git
$ cd source
$ python bull_cows.py imcheater
my puzzle: 5091
enter 4 digits: 0519
cows: 4 bulls: 0
enter 4 digits: 5091
cows: 0 bulls: 4
Done!
Quest solved with 2 tries
```

## Yadex.Alice skill, that hosted as GoogleAppEngine StandardEnvironment app
You need Google account and registration at [Google Cloud Platform](https://cloud.google.com/). Create [new python project](https://console.cloud.google.com/projectcreate) and save your new GAE project ID. [Download](https://cloud.google.com/sdk/) and install Cloud SDK, then:
```
$ gcloud init
$ gcloud components install app-engine-python
$ export BULLS_COWS_GAE_ID="Your-GAE-project-ID"
$ git clone git@github.com:vb64/bulls_cows.git
$ make setup PYTHON_BIN=path_to_python27_executable
$ make deploy
```
After successful deployment visit the URL https://Your-GAE-project-ID.appspot.com You should see something like this:
```
Yandex Alice Bulls&Cows game lives here
```
Then, you need Yandex account and registration at [Yandex.Dialogs](https://dialogs.yandex.ru). Create [new Alice skill](https://dialogs.yandex.ru/developer/) and set `Webhook URL` field to

```
https://Your-GAE-project-ID.appspot.com/alice
```
Test your Alice skill at the 'Testing' tab.

For security purpose, you can uncomment next lines of code and set a correct ID for your Alice skill:
https://github.com/vb64/bulls_cows/blob/bfcbfec8156e7e470062a94596a786ec89701cf1/source/views.py#L57
