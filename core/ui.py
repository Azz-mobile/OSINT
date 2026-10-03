RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
DIM = "\033[2m"
PURPLE = "\033[95m"


def banner():

    # =========================================================
    # OSINT - DOT MATRIX
    # =========================================================

    O = [
        "   ●●●●●   ",
        " ●●     ●● ",
        "●●       ●●",
        "●●       ●●",
        "●●       ●●",
        " ●●     ●● ",
        "   ●●●●●   ",
    ]

    S = [
        " ●●●●●●●● ",
        "●●        ",
        "●●        ",
        " ●●●●●●●  ",
        "        ●●",
        "        ●●",
        "●●●●●●●●  ",
    ]

    I = [
        "●●●●●●●●●",
        "    ●    ",
        "    ●    ",
        "    ●    ",
        "    ●    ",
        "    ●    ",
        "●●●●●●●●●",
    ]

    N = [
        "●●      ●●",
        "●●●     ●●",
        "●●●●    ●●",
        "●● ●●   ●●",
        "●●  ●●  ●●",
        "●●   ●● ●●",
        "●●    ●●●●",
    ]

    T = [
        "●●●●●●●●●●",
        "     ●    ",
        "     ●    ",
        "     ●    ",
        "     ●    ",
        "     ●    ",
        "     ●    ",
    ]

    letters = [O, S, I, N, T]

    print()

    # =========================================================
    # TOP FRAME
    # =========================================================

    print(
        CYAN
        + "╭"
        + "─" * 62
        + "╮"
        + RESET
    )

    # Decorative dots
    print(
        CYAN
        + "│"
        + RESET
        + "    "
        + DIM
        + "· · · · · · · · · · · · · · · · · · · · · ·"
        + RESET
        + "    "
        + CYAN
        + "│"
        + RESET
    )

    print(
        CYAN
        + "│"
        + RESET
    )

    # =========================================================
    # OSINT DOT MATRIX
    # =========================================================

    for row in range(7):

        line = ""

        for letter in letters:
            line += letter[row] + "   "

        print(
            CYAN
            + "│"
            + RESET
            + "   "
            + CYAN
            + line
            + RESET
            + "  "
            + CYAN
            + "│"
            + RESET
        )

    print(
        CYAN
        + "│"
        + RESET
    )

    # =========================================================
    # BY AZZ - NORMAL FONT
    # =========================================================

    print(
        CYAN
        + "│"
        + RESET
        + "                     "
        + PURPLE
        + "BY AZZ"
        + RESET
        + "                     "
        + CYAN
        + "│"
        + RESET
    )

    print(
        CYAN
        + "│"
        + RESET
        + "        "
        + PURPLE
        + "───────────◆──────────────◆───────────"
        + RESET
        + "        "
        + CYAN
        + "│"
        + RESET
    )

    print(
        CYAN
        + "│"
        + RESET
        + "              "
        + DIM
        + "· · · · · · · · · · · · · ·"
        + RESET
        + "              "
        + CYAN
        + "│"
        + RESET
    )

    # =========================================================
    # BOTTOM FRAME
    # =========================================================

    print(
        CYAN
        + "╰"
        + "─" * 62
        + "╯"
        + RESET
    )

    print()


def badge(s):

    return {
        "FOUND": f"{GREEN}FOUND{RESET}",
        "NOT FOUND": f"{DIM}NOT FOUND{RESET}",
        "UNKNOWN": f"{YELLOW}UNKNOWN{RESET}"
    }.get(s, s)


def print_results(result):

    print(
        f"\n{BOLD}Target:{RESET} "
        f"{result['target']}"
    )

    print(
        f"{BOLD}Platforms:{RESET} "
        f"{len(result['platforms'])} | "
        f"{GREEN}FOUND {result['counts']['FOUND']}{RESET} | "
        f"{DIM}NOT FOUND {result['counts']['NOT FOUND']}{RESET} | "
        f"{YELLOW}UNKNOWN {result['counts']['UNKNOWN']}{RESET}"
    )

    current = None

    for x in result["platforms"]:

        if x["category"] != current:

            current = x["category"]

            print(
                f"\n{CYAN}{BOLD}{current}{RESET}\n"
                + "─" * 58
            )

        print(
            f"  {badge(x['status']):<20} "
            f"{x['name']:<20} "
            f"{x['url']}"
        )

    print(
        f"\n{CYAN}{BOLD}"
        "SEARCH ENGINE OSINT"
        f"{RESET}"
    )

    for x in result["searches"]:

        print(
            f"  {x['engine']:<14} "
            f"{x['query']}"
        )

        print(
            f"                 "
            f"{x['url']}"
        )

    print(
        f"\n{CYAN}{BOLD}"
        "USERNAME VARIANTS"
        f"{RESET}"
    )

    print(
        "  "
        + ", ".join(result["variants"])
    )

    print(
        f"\n{GREEN}Reports:{RESET}"
    )

    print(
        "  JSON:",
        result["report_json"]
    )

    print(
        "  HTML:",
        result["report_html"]
    )

    print(
        "  TXT :",
        result["report_txt"]
    )