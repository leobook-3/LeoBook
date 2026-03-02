
import requests

base = 'https://assets.football-logos.cc/collections/'
seasons = ['-2025-2026', '-2024-2025', '-2025', '-2024', '']
postfix = '.football-logos.cc.zip'

leagues = {
    'croatia-hnl': ['croatia-hnl', 'croatia-supersport-hnl', 'croatia-prva-hnl'],
    'czech-republic-first-league': ['czech-republic-first-league', 'czech-republic-fortuna-liga', 'czech-republic-chance-liga'],
    'denmark-superliga': ['denmark-superliga', 'denmark-3f-superliga'],
    'norway-eliteserien': ['norway-eliteserien'],
    'sweden-allsvenskan': ['sweden-allsvenskan'],
    'switzerland-super-league': ['switzerland-super-league', 'switzerland-credit-suisse-super-league'],
    'ukraine-premier-league': ['ukraine-premier-league'],
    'russia-premier-league': ['russia-premier-league'],
    'japan-j1-league': ['japan-j1-league', 'japan-j-league'],
    'south-korea-k-league-1': ['south-korea-k-league-1'],
    'colombia-primera-a': ['colombia-primera-a', 'colombia-liga-betplay'],
    'chile-primera-division': ['chile-primera-division'],
}

for name, variants in leagues.items():
    print(f"Probing {name}...")
    found = False
    for v in variants:
        for s in seasons:
            url = f"{base}{v}{s}{postfix}"
            try:
                r = requests.head(url, timeout=3)
                if r.status_code == 200:
                    print(f"  [FOUND] {name} -> {v}{s}")
                    found = True
                    break
                else:
                    # print(f"  [NO] {v}{s} ({r.status_code})")
                    pass
            except Exception as e:
                # print(f"  [ERR] {v}{s}: {e}")
                pass
        if found: break
    if not found:
        print(f"  [MISSING] {name}")
