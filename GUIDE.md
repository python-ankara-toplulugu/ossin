# Development Guide

## Commands

### install

```sh
uv tool install hatch
uv sync
```

### init

```sh
uv run hatch new <package-name>
```

### bump

```sh
uv run hatch version major/minor/patch
```

### build

```sh
uv run hatch build
```

### unarchive-wheel

```sh
uv run -m zipfile -e dist/<package-name>-<version>-py3-none-any.whl dist/<package-name>-<version>-unpacked
# unzip dist/<package-name>-<version>-py3-none-any.whl -d dist/<package-name>-<version>-unpacked
```

### unarchive-tar-gz

```sh
uv run -m tarfile -e dist/<package-name>-<version>.tar.gz dist/<package-name>-<version>-unpacked
# tar -xzf dist/<package-name>-<version>.tar.gz -C dist/<package-name>-<version>-unpacked
```

### publish

```sh
hatch publish --repo test --user __token__ --auth <token>
```

### publish-test

```sh
uv pip install --index-url https://test.pypi.org/simple/ <package-name>
```
