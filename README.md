## Apps Dashboard

This dashboard aims at tracking the status of Ledger apps.

Each app is described in a separate YAML file in the `apps/` directory.


### Rate limiting

Unfortunately, the GitHub API
[rate limiting rules](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting)
is quite strict for unauthenticated requests (the rate limit allows for up to 60
requests per hour).

The solution is to
[create](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)
a personal access token (PAT) and pass it through the dashboard URL hash
location. Eg.

```
/index.html#token=username:ghp_IlNE7ysuXOdh7Bk2yYgFAs0e7heqCA357Qxg
```

That isn't super convenient, if you find a better way to use the token, please
tell us.


### Contributions

Contributions should be made through pull requests, which should be reviewed
before being merged to the `main` branch. External contributors who are outside
of [LedgerHQ](https://github.com/LedgerHQ/) organization aren't expected.

Please run `./tools/validate-schema.py` after having modified a YAML file. The
following dependencies are required:

```shell
apt install jq python3-jsonschema python3-yaml
```


### How to run the dashboard locally

Run the following script and go to
[https://127.0.0.1:4433/docs/index.html](https://127.0.0.1:4433/docs/index.html):

```shell
./tools/webserver.py
```
