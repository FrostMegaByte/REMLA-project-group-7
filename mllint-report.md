# ML Project Report
**Project** | **Details**
--------|--------
Date    | Tue, 21 Jun 2022 09:45:23 +0200 
Path    | `/home/hielke/repos/REMLA-project-group-7`
Config  | `.mllint.yml`
Default | No
Git: Remote URL | `git@github.com:FrostMegaByte/REMLA-project-group-7.git`
Git: Commit     | `9746e1d2f57d7774382d3ba8a96e762aa34fe84b`
Git: Branch     | `mllint-greater-than-0122`
Git: Dirty Workspace?  | Yes
Number of Python files | 22
Lines of Python code   | 661

---

## Reports

### Version Control (`version-control`) — **93.8**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project uses Git | `version-control/code/git`
❌ | 50.0% | 1 | Project should not have any large files in its Git history | `version-control/code/git-no-big-files`
✅ | 100.0% | 1 | DVC: Project uses Data Version Control | `version-control/data/dvc`
✅ | 100.0% | 1 | DVC: Is installed | `version-control/data/dvc-is-installed`
✅ | 100.0% | 1 | DVC: Folder '.dvc' should be committed to Git | `version-control/data/commit-dvc-folder`
✅ | 100.0% | 1 | DVC: Should have at least one remote data storage configured | `version-control/data/dvc-has-remote`
✅ | 100.0% | 1 | DVC: Should be tracking at least one data file | `version-control/data/dvc-has-files`
✅ | 100.0% | 1 | DVC: File 'dvc.lock' should be committed to Git | `version-control/data/commit-dvc-lock`
 | _Total_ | | | 
❌ | **93.8**% | | Version Control | `version-control`

#### Details — Project should not have any large files in its Git history — ❌

Your project's Git history contains the following files that are larger than 10 MB:
- **15 MB** - commit `8cf6230f090e7076f7432aa87172d1a6095d88a8` - `models/tfidf_model.pickle`
- **15 MB** - commit `0a7866f9ff54abcf6c351ac7e50378c508f1038d` - `models/tfidf_model.pickle`

These files may not necessarily be in your project right now, but they are still stored inside your project's Git history.
Thus, whenever your project is downloaded (with `git clone`), all these unnecessary files have to be downloaded as well.

See [this StackOverflow answer](https://stackoverflow.com/a/46615578/8059181) to learn how to remove these files from your project's Git history.

### Dependency Management (`dependency-management`) — **50.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project properly keeps track of its dependencies | `dependency-management/use`
❌ | 0.0% | 1 | Project should only use one dependency manager | `dependency-management/single`
❌ | 50.0% | 1 | Project places its development dependencies in dev-dependencies | `dependency-management/use-dev`
 | _Total_ | | | 
❌ | **50.0**% | | Dependency Management | `dependency-management`

#### Details — Project should only use one dependency manager — ❌

Your project was found to be using multiple dependency managers: [Poetry requirements.txt setup.py]

Consider using Poetry to replace both your `requirements.txt` and `setup.py`

#### Details — Project places its development dependencies in dev-dependencies — ❌

Poetry is tracking the following dependencies as regular dependencies, but they should actually be development dependencies.

Please move the following dependencies from the `dependencies` section to the `dev-dependencies` section in your `pyproject.toml`, then run `poetry lock` to update your lock file.

- dvc


### Code Quality (`code-quality`) — **58.5**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project should use code quality linters | `code-quality/use-linters`
✅ | 100.0% | 1 | All code quality linters should be installed in the current environment | `code-quality/linters-installed`
✅ | 100.0% | 1 | Pylint is configured for this project | `code-quality/pylint/is-configured`
❌ | 0.0% | 1 | Mypy reports no issues with this project | `code-quality/mypy/no-issues`
❌ | 0.0% | 1 | Black reports no issues with this project | `code-quality/black/no-issues`
✅ | 100.0% | 1 | isort reports no issues with this project | `code-quality/isort/no-issues`
✅ | 100.0% | 0 | isort is properly configured | `code-quality/isort/is-configured`
❌ | 9.2% | 1 | Bandit reports no issues with this project | `code-quality/bandit/no-issues`
 | _Total_ | | | 
❌ | **58.5**% | | Code Quality | `code-quality`

#### Details — Project should use code quality linters — ✅

Hooray, all linters detected:

- Pylint
- Mypy
- Black
- isort
- Bandit


#### Details — Mypy reports no issues with this project — ❌

Mypy reported **118** issues with your project:

- `tests/test_data_schema.py:1,1` - Error: Skipping analyzing "tensorflow_data_validation": module is installed, but missing library stubs or py.typed marker  [import]
- `tests/test_data_schema.py:6,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `docs/conf.py:29,1` - Error: Need type annotation for "extensions" (hint: "extensions: List[<type>] = ...")  [var-annotated]
- `docs/conf.py:172,1` - Error: Need type annotation for "latex_elements" (hint: "latex_elements: Dict[<type>, <type>] = ...")  [var-annotated]
- `src/models/train_model.py:4,1` - Error: Skipping analyzing "sklearn.linear_model": module is installed, but missing library stubs or py.typed marker  [import]
- `src/models/train_model.py:5,1` - Error: Skipping analyzing "sklearn.multiclass": module is installed, but missing library stubs or py.typed marker  [import]
- `src/models/train_model.py:8,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/models/train_model.py:24,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/models/train_model.py:24,1` - Note: Use "-> None" if function does not return a value
- `src/models/train_model.py:35,24` - Error: Call to untyped function "train_classifier" in typed context  [no-untyped-call]
- `src/models/train_model.py:37,24` - Error: Call to untyped function "train_classifier" in typed context  [no-untyped-call]
- `src/models/train_model.py:49,5` - Error: Call to untyped function "main" in typed context  [no-untyped-call]
- `src/models/predict_model.py:6,1` - Error: Skipping analyzing "sklearn.metrics": module is installed, but missing library stubs or py.typed marker  [import]
- `src/models/predict_model.py:20,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/models/predict_model.py:25,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/models/predict_model.py:30,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/models/predict_model.py:30,1` - Note: Use "-> None" if function does not return a value
- `src/models/predict_model.py:36,17` - Error: Call to untyped function "Evaluator" in typed context  [no-untyped-call]
- `src/models/predict_model.py:54,5` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/models/predict_model.py:54,5` - Note: Use "-> None" if function does not return a value
- `src/models/predict_model.py:96,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/models/predict_model.py:122,5` - Error: Call to untyped function "main" in typed context  [no-untyped-call]
- `src/util/util.py:8,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/util/util.py:15,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/util/util.py:15,1` - Error: Function is missing a type annotation for one or more arguments  [no-untyped-def]
- `src/features/build_features.py:7,1` - Error: Skipping analyzing "scipy": module is installed, but missing library stubs or py.typed marker  [import]
- `src/features/build_features.py:8,1` - Error: Skipping analyzing "sklearn.feature_extraction.text": module is installed, but missing library stubs or py.typed marker  [import]
- `src/features/build_features.py:9,1` - Error: Skipping analyzing "sklearn.preprocessing": module is installed, but missing library stubs or py.typed marker  [import]
- `src/features/build_features.py:27,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/build_features.py:33,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/build_features.py:37,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/build_features.py:52,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/build_features.py:53,5` - Error: Need type annotation for "count_dict" (hint: "count_dict: Dict[<type>, <type>] = ...")  [var-annotated]
- `src/features/build_features.py:64,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/build_features.py:65,5` - Error: Need type annotation for "count_dict" (hint: "count_dict: Dict[<type>, <type>] = ...")  [var-annotated]
- `src/features/build_features.py:77,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/build_features.py:78,29` - Error: Call to untyped function "count_words_strings" in typed context  [no-untyped-call]
- `src/features/build_features.py:86,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/build_features.py:90,21` - Error: Call to untyped function "my_bag_of_words" in typed context  [no-untyped-call]
- `src/features/build_features.py:97,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/build_features.py:98,20` - Error: Call to untyped function "count_words_strings" in typed context  [no-untyped-call]
- `src/features/build_features.py:108,34` - Error: Call to untyped function "my_bag_of_words" in typed context  [no-untyped-call]
- `src/features/build_features.py:114,34` - Error: Call to untyped function "my_bag_of_words" in typed context  [no-untyped-call]
- `src/features/build_features.py:120,34` - Error: Call to untyped function "my_bag_of_words" in typed context  [no-untyped-call]
- `src/features/build_features.py:129,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/build_features.py:132,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/features/build_features.py:136,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/features/build_features.py:170,20` - Error: Call to untyped function "FeatureExtractorBow" in typed context  [no-untyped-call]
- `src/features/build_features.py:176,22` - Error: Call to untyped function "FeatureExtractorTfidf" in typed context  [no-untyped-call]
- `src/features/build_features.py:177,17` - Error: Call to untyped function "get_features" in typed context  [no-untyped-call]
- `src/features/build_features.py:178,18` - Error: Call to untyped function "get_features" in typed context  [no-untyped-call]
- `src/features/build_features.py:183,19` - Error: Call to untyped function "count_words_lists" in typed context  [no-untyped-call]
- `src/features/build_features.py:184,18` - Error: Call to untyped function "LabelsMlb" in typed context  [no-untyped-call]
- `src/features/build_features.py:187,19` - Error: Call to untyped function "get_features" in typed context  [no-untyped-call]
- `src/features/build_features.py:188,17` - Error: Call to untyped function "get_features" in typed context  [no-untyped-call]
- `src/features/build_features.py:205,5` - Error: Name "output_filepath" already defined on line 136  [no-redef]
- `src/features/build_features.py:207,31` - Error: Unsupported left operand type for + ("Path")  [operator]
- `src/features/build_features.py:208,29` - Error: Unsupported left operand type for + ("Path")  [operator]
- `src/features/build_features.py:209,30` - Error: Unsupported left operand type for + ("Path")  [operator]
- `src/features/build_features.py:211,33` - Error: Unsupported left operand type for + ("Path")  [operator]
- `src/features/build_features.py:212,31` - Error: Unsupported left operand type for + ("Path")  [operator]
- `src/features/build_features.py:213,32` - Error: Unsupported left operand type for + ("Path")  [operator]
- `src/features/build_features.py:215,35` - Error: Unsupported left operand type for + ("Path")  [operator]
- `src/features/build_features.py:216,33` - Error: Unsupported left operand type for + ("Path")  [operator]
- `src/features/build_features.py:217,34` - Error: Unsupported left operand type for + ("Path")  [operator]
- `src/features/build_features.py:219,27` - Error: Unsupported left operand type for + ("Path")  [operator]
- `src/features/build_features.py:220,35` - Error: Unsupported left operand type for + ("Path")  [operator]
- `src/features/build_features.py:221,33` - Error: Unsupported left operand type for + ("Path")  [operator]
- `src/data/make_dataset.py:7,1` - Error: Skipping analyzing "nltk": module is installed, but missing library stubs or py.typed marker  [import]
- `src/data/make_dataset.py:7,1` - Note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
- `src/data/make_dataset.py:9,1` - Error: Skipping analyzing "nltk.corpus": module is installed, but missing library stubs or py.typed marker  [import]
- `src/data/make_dataset.py:10,1` - Error: Skipping analyzing "sklearn.model_selection": module is installed, but missing library stubs or py.typed marker  [import]
- `src/data/make_dataset.py:19,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/data/make_dataset.py:49,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/data/make_dataset.py:95,16` - Error: Call to untyped function "text_prepare" in typed context  [no-untyped-call]
- `src/data/make_dataset.py:96,14` - Error: Call to untyped function "text_prepare" in typed context  [no-untyped-call]
- `src/data/make_dataset.py:97,15` - Error: Call to untyped function "text_prepare" in typed context  [no-untyped-call]
- `src/data/make_dataset.py:101,34` - Error: Call to untyped function "filterDuplicates" in typed context  [no-untyped-call]
- `src/data/make_dataset.py:119,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/data/make_dataset.py:139,5` - Error: Call to untyped function "main" in typed context  [no-untyped-call]
- `tests/test_make_dataset.py:4,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `tests/test_make_dataset.py:4,1` - Note: Use "-> None" if function does not return a value
- `tests/test_make_dataset.py:8,12` - Error: Call to untyped function "text_prepare" in typed context  [no-untyped-call]
- `tests/test_make_dataset.py:11,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `tests/test_make_dataset.py:11,1` - Note: Use "-> None" if function does not return a value
- `tests/test_make_dataset.py:14,12` - Error: Call to untyped function "text_prepare" in typed context  [no-untyped-call]
- `tests/test_build_features.py:4,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `tests/test_build_features.py:4,1` - Note: Use "-> None" if function does not return a value
- `tests/test_build_features.py:9,16` - Error: Call to untyped function "count_words_strings" in typed context  [no-untyped-call]
- `tests/test_build_features.py:28,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `tests/test_build_features.py:28,1` - Note: Use "-> None" if function does not return a value
- `tests/test_build_features.py:34,16` - Error: Call to untyped function "count_words_lists" in typed context  [no-untyped-call]
- `tests/test_build_features.py:53,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `tests/test_build_features.py:53,1` - Note: Use "-> None" if function does not return a value
- `tests/test_build_features.py:60,13` - Error: Call to untyped function "my_bag_of_words" in typed context  [no-untyped-call]
- `tests/test_data.py:13,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `tests/test_data.py:30,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `tests/test_data.py:39,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `tests/test_data.py:51,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `tests/test_data.py:59,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `tests/conftest.py:19,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `tests/conftest.py:28,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `tests/conftest.py:33,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `tests/conftest.py:37,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/serve_model.py:12,1` - Error: Skipping analyzing "uvicorn": module is installed, but missing library stubs or py.typed marker  [import]
- `src/serve_model.py:34,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/serve_model.py:42,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/serve_model.py:43,17` - Error: Call to untyped function "Evaluator" in typed context  [no-untyped-call]
- `src/serve_model.py:48,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/serve_model.py:49,17` - Error: Call to untyped function "Evaluator" in typed context  [no-untyped-call]
- `src/serve_model.py:54,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/serve_model.py:55,17` - Error: Call to untyped function "Evaluator" in typed context  [no-untyped-call]
- `src/serve_model.py:65,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/serve_model.py:66,17` - Error: Call to untyped function "Evaluator" in typed context  [no-untyped-call]
- `src/serve_model.py:71,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/serve_model.py:72,11` - Error: Call to untyped function "text_prepare" in typed context  [no-untyped-call]
- `src/serve_model.py:80,25` - Error: Call to untyped function (unknown) in typed context  [no-untyped-call]
- `src/serve_model.py:91,1` - Error: Function is missing a return type annotation  [no-untyped-def]


#### Details — Black reports no issues with this project — ❌

Black reported **1** files in your project that it would reformat:

- `tests/conftest.py`

Black can fix these issues automatically when you run `black .` in your project.

#### Details — isort reports no issues with this project — ✅

Congratulations, `isort` is happy with your project!

#### Details — Bandit reports no issues with this project — ❌

Bandit reported **24** issues with your project:

- `src/features/build_features.py:2` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/features/build_features.py:28` - _(B106, severity: LOW, confidence: MEDIUM)_ - Possible hardcoded password: '(\S+)' [More Info](https://bandit.readthedocs.io/en/1.7.4/plugins/b106_hardcoded_password_funcarg.html)
- `src/models/predict_model.py:2` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/models/predict_model.py:22` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_calls.html#b301-pickle)
- `src/models/predict_model.py:27` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_calls.html#b301-pickle)
- `src/models/train_model.py:2` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/models/train_model.py:30` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_calls.html#b301-pickle)
- `src/models/train_model.py:31` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_calls.html#b301-pickle)
- `src/models/train_model.py:32` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_calls.html#b301-pickle)
- `src/serve_model.py:8` - _(B403, severity: LOW, confidence: HIGH)_ - Consider possible security implications associated with pickle module. [More Info](https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_imports.html#b403-import-pickle)
- `src/serve_model.py:77` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_calls.html#b301-pickle)
- `src/serve_model.py:78` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_calls.html#b301-pickle)
- `src/serve_model.py:81` - _(B301, severity: MEDIUM, confidence: HIGH)_ - Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue. [More Info](https://bandit.readthedocs.io/en/1.7.4/blacklists/blacklist_calls.html#b301-pickle)
- `src/serve_model.py:105` - _(B104, severity: MEDIUM, confidence: MEDIUM)_ - Possible binding to all interfaces. [More Info](https://bandit.readthedocs.io/en/1.7.4/plugins/b104_hardcoded_bind_all_interfaces.html)
- `tests/test_build_features.py:25` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/1.7.4/plugins/b101_assert_used.html)
- `tests/test_build_features.py:50` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/1.7.4/plugins/b101_assert_used.html)
- `tests/test_build_features.py:64` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/1.7.4/plugins/b101_assert_used.html)
- `tests/test_data.py:36` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/1.7.4/plugins/b101_assert_used.html)
- `tests/test_data.py:48` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/1.7.4/plugins/b101_assert_used.html)
- `tests/test_data.py:56` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/1.7.4/plugins/b101_assert_used.html)
- `tests/test_data.py:62` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/1.7.4/plugins/b101_assert_used.html)
- `tests/test_data_schema.py:24` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/1.7.4/plugins/b101_assert_used.html)
- `tests/test_make_dataset.py:8` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/1.7.4/plugins/b101_assert_used.html)
- `tests/test_make_dataset.py:14` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/1.7.4/plugins/b101_assert_used.html)


### Testing (`testing`) — **47.7**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 90.9% | 1 | Project has automated tests | `testing/has-tests`
❌ | 0.0% | 1 | Project passes all of its automated tests | `testing/pass`
❌ | 0.0% | 1 | Project provides a test coverage report | `testing/coverage`
✅ | 100.0% | 1 | Tests should be placed in the tests folder | `testing/tests-folder`
 | _Total_ | | | 
❌ | **47.7**% | | Testing | `testing`

#### Details — Project has automated tests — ❌

There are **4** test files in your project, which meets the minimum of **1** test files required.

However, this only equates to **18.181818%** of Python files in your project being tests, while `mllint` expects that **20%** of your project's Python files are tests.

#### Details — Project passes all of its automated tests — ❌

A test report was provided, namely `tests-report.xml`, but this file could not be found.

Please update the `testing.report` setting in your project's `mllint` configuration to fix the path to your project's test report. Remember that this path must be relative to the root of your project directory.

#### Details — Project provides a test coverage report — ❌

A test coverage report was provided, namely `coverage.xml`, but this file could not be found or opened (error: `did not find a file matching coverage.xml in folder /home/hielke/repos/REMLA-project-group-7: file does not exist`).

Please update the `testing.coverage.report` setting in your project's `mllint` configuration to fix the path to your project's test report. Remember that this path must be relative to the root of your project directory.

### Continuous Integration (`ci`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project uses Continuous Integration (CI) | `ci/use`
 | _Total_ | | | 
✅ | **100.0**% | | Continuous Integration | `ci`

## Errors

1 error(s) occurred while analysing your project:
- ❌ **Code Quality** - 1 error occurred:
	* Pylint failed to run: error parsing Pylint output 'PYLINTHOME is now '/home/hielke/.cache/pylint' but obsolescent '/home/hielke/.pylint.d' is found; you can safely remove the latter
[]
': invalid character 'P' looking for beginning of value


