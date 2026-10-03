# AZZ Universal Username OSINT v2

A CLI tool for public-source username reconnaissance.

## Included
- 60+ public profile URL patterns
- Categories: Social Media, Video/Streaming, Developer, Creative, Publishing, Profiles, Gaming
- FOUND / NOT FOUND / UNKNOWN classification
- Concurrent scanning
- Search-engine OSINT query generation
- Username variants
- Professional HTML report
- JSON and TXT reports
- Python standard library only

## Run
```bash
python main.py azz-mobile
```

Interactive:
```bash
python main.py
```

Optional concurrency:
```bash
python main.py azz-mobile --workers 8
```

## Status semantics
FOUND = successful HTTP response.
NOT FOUND = typically HTTP 404.
UNKNOWN = rate limit, access restriction, auth wall, network error, or ambiguous platform behavior.

A match is only an OSINT lead; it does not prove identity.

Use only public information and comply with applicable laws and platform terms. No login bypass, private-data extraction, credential attacks, exploitation, or rate-limit evasion.
