# Bulls&amp;Cows game
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/bulls_cows/pep257.yml?label=Pep257&style=plastic&branch=master)](https://github.com/vb64/bulls_cows/actions?query=workflow%3Apep257)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/bulls_cows/py3.yml?label=Python%203.7-3.10&style=plastic&branch=master)](https://github.com/vb64/bulls_cows/actions?query=workflow%3Apy3)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/c54f0192f4a444a4afbae2f5f1f7ab1e)](https://app.codacy.com/gh/vb64/bulls_cows/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/c54f0192f4a444a4afbae2f5f1f7ab1e)](https://app.codacy.com/gh/vb64/bulls_cows/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)

[Game rules](https://en.wikipedia.org/wiki/Bulls_and_Cows)

## Run game on localhost
```bash
git clone git@github.com:vb64/bulls_cows.git
python bulls_cows/source/default/bull_cows.py imcheater
my puzzle: 5091
enter 4 digits: 0519
cows: 4 bulls: 0
enter 4 digits: 5091
cows: 0 bulls: 4
Done!
Quest solved with 2 tries
```

## Yandex.Alice skill, that hosted at GoogleAppEngine Standard Environment
You need Google account and registration at [Google Cloud Platform](https://cloud.google.com/). Create [new python project](https://console.cloud.google.com/projectcreate) and save your new GAE project ID. [Download](https://cloud.google.com/sdk/) and install Cloud SDK, then:
```bash
gcloud init
cd bulls_cows
make setup PYTHON_BIN=path/to/python3
make tests
make deploy
```
After successful deployment visit the URL https://Your-GAE-project-ID.appspot.com You should see something like this:
```
Yandex Alice Bulls&Cows game lives here
```
Then, you need Yandex account and registration at [Yandex.Dialogs](https://dialogs.yandex.ru). Create [new Alice skill](https://dialogs.yandex.ru/developer/) and set `Webhook URL` field to

```bash
https://Your-GAE-project-ID.appspot.com/alice
```
Test your Alice skill at the 'Testing' tab.

For security purpose, you can [uncomment next lines](https://github.com/vb64/bulls_cows/blob/bfcbfec8156e7e470062a94596a786ec89701cf1/source/views.py#L57) of code and set a correct ID for your Alice skill.

## Live version
The live version of this code is available as [Yandex.Alice skill](https://alice.ya.ru/s/59166701-101b-44b3-b7e3-b7e078036890).
