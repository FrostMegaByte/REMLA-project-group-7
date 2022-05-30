# Release engeneering of Multilabel classification on Stack Overflow tags
This project designs a Release pipeline for a multilabel classifying ML applications. The application detials can be found on [the forked project](https://github.com/luiscruz/remla-baseline-project/blob/main/README.md). The team working on this project has applied the following changes to improve the development of the ML applications:
* Modularise code in separate code files
* PyTest
* MLLint
* Docker
* DVC
* Kubernetes

# Run release pipeline
To add a semantic version tag to a commit, please do the following on the `dev` branch.
```console
# Add release tag
git tag release
git push origin release
```
This will then trigger the "Deploy - Release tag" pipeline, which will increment the version in the VERSION.txt file.
It will also create and push a commit with a v?.?.? tag as a release on `dev`.  

If you need to rerun the "Deploy - Release tag" pipeline, you'll most likely need to delete the `release` tag first. This can be done by running the following commands.
```console
# Remove release tag
git tag -d release
git push origin :release
```
Then just re-add the `release` tag again by running the first commands specified in this section.

## Testing: PyTest
Pytests can be found in the "tests" directory. Newly added test classes should end with "test_*.py" and newly added test functions should start with "test"

## DVC
DVC is used to manage the ML pipeline version control artifacts. The artifacts are pushed to a project google drive repo which, the first time you connect to it, needs authentication.

To use DVC, 
Run the pipeline by:
```console
dvc repro
```

commit completed artifacts by:
```console
dvc commit -am "<message>"
```
and push the commit with:
```console
dvc push
```

To use pushed artifacts you can simply use:
```console
dvc pull
```