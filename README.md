# Media Tracker

A command-line tool for tracking books, movies, and games you've read, watched, or played — including status, ratings, and type-specific details (author, director, platform, etc.). Data persists to a local JSON file between sessions.

## Features

- **Add items** — Book, Movie, or Game, each with its own fields (pages/author, runtime/director, hours played/platform)
- **View all** — numbered list of every item in your collection
- **Search & filter** — by title keyword, media type, or status
- **Update status** — mark items as `finished`, `in-progress`, or `not-started`
- **Delete items** — with a confirmation prompt before anything is removed
- **Stats** — counts by status and type, plus average rating across the collection
- **Persistence** — collection auto-loads on startup and saves to `media.json` on exit, on Ctrl+C, or on an unexpected crash

## Requirements

- Python **3.12+**
- No external dependencies — standard library only (`json`, `datetime`)

## Installation

```bash
git clone <your-repo-url>
cd media-tracker
python main.py
```

No `pip install` needed.

## Usage

Run the app and follow the on-screen menu:

```
--- Media Tracker ---
1. Add item
2. View all
3. Search or filter
4. Update status
5. Delete item
6. Stats
7. Save and exit
```

Data is saved when you choose option 7, and also automatically if the program is interrupted (Ctrl+C) or hits an unexpected error, so a crash mid-session won't lose your changes.

### Adding an item

You'll be prompted for a media type, then fields specific to that type:

| Type  | Fields |
|-------|--------|
| Book  | Name, Status, Pages, Author, Rating |
| Movie | Name, Status, Rating, Runtime (min), Director |
| Game  | Name, Status, Rating, Hours Played, Platform |

Ratings are validated to the range 0–5.

### Sample session

```
--- Media Tracker ---
1. Add item
2. View all
3. Search or filter
4. Update status
5. Delete item
6. Stats
7. Save and exit
Enter your choice: 1
Please select your media type:
1-Book
2-Movie
3-Game
Enter your choice: 1
---- Book Data Entry ----
Name: Dune
Select status:
1-finished
2-not-started
3-in-progress
Enter your choice: 2
Pages: 412
Author: Frank Herbert
Rating (0-5): 5

--- Media Tracker ---
...
Enter your choice: 2
1. Dune - not-started

--- Media Tracker ---
...
Enter your choice: 6

Items by status:
finished: 0
not-started: 1
in-progress: 0

Items by type:
book: 1
movie: 0
game: 0

Average rating: 5.0
```

## Design Decisions

### Why inheritance (`Media` → `Book`/`Movie`/`Game`) instead of one flat class

Books, movies, and games share a core set of fields — `title`, `status`, `rating`, `date_added` — but each also has fields the others don't (a book has `pages` and `author`; a game has `hours_played` and `platform`, and so on). A single flat class would need every field for every type, with irrelevant fields left `None` on most instances — e.g. every `Movie` object carrying an unused `pages` attribute. That gets messier as more media types get added later.

Inheritance keeps the shared behavior (serialization, string formatting, the shared fields) in one place — `Media` — while each subclass only defines what's actually specific to it. It also means `isinstance()` checks (used throughout `filter_by_type` and `show_stats`) map directly onto real media categories instead of a manually-tracked type field with no structural guarantee behind it.

### Why JSON over CSV for persistence

The data isn't flat — three different item shapes are being stored (`Book`, `Movie`, `Game`), each with a different set of fields. CSV assumes one row shape, so it would need blank columns for the fields each type doesn't use, or a lossy lowest-common-denominator format. JSON naturally represents each item as a dict with only the keys it actually has, and Python's `json` module maps directly to the `to_dict()`/rebuild-from-dict pattern already used here — no extra parsing library, no schema mismatch to work around.

## File Structure

```
.
├── main.py       # CLI logic: menu loop, input handling, persistence
├── models.py     # Media, Book, Movie, Game classes
└── media.json    # Auto-generated on first save — your saved collection
```

## Data Model

`Media` is the base class (`title`, `status`, `rating`, `date_added`). `Book`, `Movie`, and `Game` subclass it and add their own fields. Each class implements `to_dict()` for JSON serialization; `main.py`'s `rebuild_item()` reverses this on load using a `type` field stored in each record, and raises `ValueError` if it encounters an unrecognized type rather than silently dropping the item.

## Known Limitations

- `media.json` with a `type` value other than `book`/`movie`/`game` will fail to load with a clear error, rather than silently skipping the bad record — by design, but worth knowing if you ever hand-edit the file
- No autosave after every individual add/update/delete — saving happens on exit, on interrupt, or on crash, not continuously
- Deleted items cannot be recovered once confirmed

## License

Add your license of choice here.
