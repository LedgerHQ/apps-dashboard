## Apps Dashboard

This dashboard aims at tracking the status of Ledger apps.

Each app is described in a separate YAML file in the `apps/` directory.


### Contributions

Contributions should be made through pull requests, which should be reviewed
before being merged to the `main` branch. External contributors aren't expected.

Please run `./tools/validate-schema.py` after having modified a YAML file. The
following dependencies are required:

```shell
apt install jq python3-jsonschema python3-yaml
```
