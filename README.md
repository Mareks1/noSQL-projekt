# Marek Białousz

(zaliczenie)
- [ ] EDA
- [ ] Aggregation Pipeline

(egzamin)
- [ ] MapReduce


| Nazwa              | Wartość                      |
|--------------------|------------------------------|
| System operacyjny  | Windows 8.1 x64              |
| Procesor           | Intel Core i7-4510U 2.0 GHz  |
| Dysk               | Toshiba MQ01ABD025 1TB       |
| Pamięć RAM         | 8,0 GB                       |
| Bazy danych        | TODO                         |
| Biblioteki         | TODO                         |


##Zadanie GEO:
Dane pobrane do zadania znajdują się na [stronie](https://data.gov.uk/dataset/index-of-place-names-in-great-britain-july-20165).

[Mapa1](https://Mareks1.github.io/noSQL-projekt/) 

TODO odnośnik na nowa strone








## Przedstawić dane

Przykładowy rekord. Ile tego jest/będzie (w sztukach, w GB)

```json
{
  "x": "raz dwa trzy",
  "latlon": [-6, 60]
}
```

Z tych danych zrobię mapki, podsumowania.

## Czyszczenie danych

Zmienić nazwy pól, wybrano te pola i dlaczego.

## Elasticsearch

Mapping -- przygotować i zapisać w Elasticsearch

### Import danych

```sh
time gunzip -c dane.json.gz | .... # calość
...                                # próbka / sample
```

### Przykładowe zapytania

Czego szukam?

### Mapki

Zapytania mapkowe.

```sh
curl localhost:9200/.... | jq .hits.hits[] | przerabiamy na GEOJson / TopoJSON
```

... [mapka-es](mapki-es)


## PostgreSQL

Schema -- przygotować i użyć w trakcie importu.

### Import danych


## MongoDB

Pamiętać aby DateTime było zaimportowane jako DateTime, liczby – to samo

### Import danych
