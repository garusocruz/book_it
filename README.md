# book_it

## Create a virtual env

```sh
python -m venv .venv
```

## Load a virtual env

```sh
source .venv/bin/activate
```

## Install python project dependencies

```sh
pip install -r requirements.txt
```

## run sample app

```sh
uvicorn src.base_app.main:app --reload
```

## run places app

```sh
uvicorn src.places.main:app --reload
```

## run schedule app

```sh
uvicorn src.schedules.main:app --reload
```

## run customers app

```sh
uvicorn src.customers.main:app --reload
```

## run professionals app

```sh
uvicorn src.professionals.main:app --reload
```
