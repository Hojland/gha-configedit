# GitHub Action for editing YAML files

![gha-yamledit](https://socialify.git.ci/hojland/gha-yamledit/image?description=1&font=KoHo&forks=1&issues=1&language=1&owner=1&pattern=Floating%20Cogs&pulls=1&stargazers=1&theme=Light)

<p align="center">
<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white" align="center">
<img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white" align="center">
<img src="https://img.shields.io/badge/github%20actions%20-%232671E5.svg?&style=for-the-badge&logo=github%20actions&logoColor=white "align="center">
</p>

GitHub actions can be integrated in any repository. Create a new folder called `.github/workflows/<any-name>.yml`. Paste the following starter code:

```yml
name: Push OCI image

on:
  pull_request:
    branches:
      - main
    types: [closed]

env:
  APPLICATION_NAME: query-engine


jobs:
  setup-build-publish:
    name: Setup, Build, Publish, and Deploy
    runs-on: ubuntu-latest
    #    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    outputs:
      release_tag: ${{ steps.fetch-latest-release.outputs.latest-release }}
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - id: fetch-latest-release
        run: |
          git fetch --tags
          export LATEST_RELEASE_VERSION=$(git describe --tags $(git rev-list --tags --max-count=1))
          echo "::set-output name=latest-release::$(echo $LATEST_RELEASE_VERSION)"
          echo The latest release version is \"$LATEST_RELEASE_VERSION\".
        shell: bash

      # Setup gcloud CLI
      - uses: google-github-actions/setup-gcloud@94337306dda8180d967a56932ceb4ddcf01edae7
        with:
          service_account_key: ${{ secrets.GKE_SA_KEY_SANDBOX }}
          project_id: ${{ secrets.GKE_PROJECT_SANDBOX }}

      # Configure docker to use the gcloud command-line tool as a credential helper
      - run: |-
          gcloud --quiet auth configure-docker

      # Build the Docker image
      - name: Build
        run: |-
          docker build \
            --tag "$IMAGE:${{ steps.fetch-latest-release.outputs.latest-release }}" \
            .

      # Push the Docker image to Google Container Registry
      - name: Publish
        run: |-
          docker push "$IMAGE:${{ steps.fetch-latest-release.outputs.latest-release }}"

      - name: Update version in deployment.yaml with release tag
        uses: Hojland/gha-yamledit@v0.0.1
        with:
          file: "k8s/environments/sandbox/deployment.yaml"
          key: "tool.poetry.version"
          value: ${{ steps.fetch-latest-release.outputs.latest-release }}
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
