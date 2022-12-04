# GitHub Action for querying pypi versions of package

![gha-yamledit](https://socialify.git.ci/hojland/gha-yamledit/image?description=1&font=KoHo&forks=1&issues=1&language=1&owner=1&pattern=Floating%20Cogs&pulls=1&stargazers=1&theme=Light)

<p align="center">
<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white" align="center">
<img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white" align="center">
<img src="https://img.shields.io/badge/github%20actions%20-%232671E5.svg?&style=for-the-badge&logo=github%20actions&logoColor=white "align="center">
</p>

GitHub actions can be integrated in any repository. Create a new folder called `.github/workflows/<any-name>.yml`. Paste the following starter code:

```yml
name: Edit yaml

on:
  pull_request:
    branches:
      - main
    types: [closed]


jobs:
  edit-yaml:
    name: Edit Yaml
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Update version in deployment.yaml with release tag
        uses: Hojland/gha-yamledit@v0.0.2
        with:
          file: "test.yaml"
          key: "key1.key2"
          value: "value2"
      steps:
      - uses: actions/checkout@v2

```

## License

The scripts and documentation in this project are released under the [MIT License](LICENSE)

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/hojland/gha-yamledit/tags).

## Authors

- **Martin Højand Hansen** - _Initial work_ - [hojland](https://github.com/hojland)

See also the list of [contributors](https://github.com/hojland/gha-yamledit/contributors) who participated in this project.
