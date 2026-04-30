# Portfo — Claude Code Init

## Project
Personal portfolio website for cainepavl. GitHub: https://github.com/cainepavl/portfo

## Stack
- **Backend**: Python / Flask (`server.py`)
- **Templates**: Jinja2 HTML in `templates/`
- **Styles/JS**: Pre-built bundle in `static/` (`main.3f6952e4.css`, `main.70a66962.js`)
- **Data**: Contact form submissions written to `database.csv`

## Running the dev server
Requires a virtual environment with Flask installed (not present system-wide):

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
python server.py
```

Server runs at `http://127.0.0.1:5000`. Routes are dynamic — any `templates/*.html` file is accessible via `/<filename>`.

## File structure
```
templates/
  index.html       # Home (01)
  works.html       # Works / carousel (02)
  work.html        # Individual project detail page
  about.html       # About Me (03)
  contact.html     # Contact form (04)
  thankyou.html    # Form submission confirmation
static/
  assets/images/   # Project hover images for carousel
  main.*.css       # Bundled styles (do not edit)
  main.*.js        # Bundled JS (do not edit)
server.py          # Flask app — routing + CSV form handler
database.csv       # Contact form submissions
```

## Carousel (works.html)
6 projects across 2 slides (3 per slide). Prev/next controls enabled.

| Slot | Project | Image file |
|------|---------|------------|
| 001 | Auditor | work01-hover.png |
| 002 | Web Scraper | work02-hover.png |
| 003 | Restart Society | work-restart-hover.jpg |
| 004 | DKIM_bh_ID | work-dkim-hover.jpg |
| 005 | File Organizer | work-files-hover.jpg |
| 006 | Game Dev | work04-hover.png |

## Git workflow
- `main` — stable/live branch
- Feature branches merged via PR on GitHub
- Auth: `gh auth setup-git` needed before first push in a new session

## GitHub repos referenced in portfolio
- Auditor: https://github.com/cainepavl/Auditor
- Data_Scraping: https://github.com/cainepavl/Data_Scraping
- Restart_Society: https://github.com/cainepavl/Restart_Society
- DKIM_bh_ID: https://github.com/cainepavl/DKIM_bh_ID
- File_Organizer: https://github.com/cainepavl/File_Organizer
