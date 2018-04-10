# bm

Simple bookmark manager that uses Sqlite to store the links.

# Usage

## Add link

```bash
bm a http://example.com
```

## List available links

```bash
bm ls
```

## Search for links

```bash
bm ls "keyword1 keyword2..."
```

## Remove link(s)

```bash
bm rm "keyword1 keyword2..."
```

or

```bash
bm rm --id=<id>
```

the ids are displayed when using ls


# Export to csv

```bash
bm export out.csv
```
