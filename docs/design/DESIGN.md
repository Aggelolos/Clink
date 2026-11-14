# Clink design guide

How the app should look. Match this when building the real front end (`web/`). The mockups are in `docs/design/mockups/`. Open the `.dc.html` files as reading material for exact styles. They need a special viewer, so they will not render as normal web pages. The logo is `logo.svg`.

## Feel

- Adult, calm, warm. An evening out, golden hour at a rooftop bar.
- Not childish. No thick black outlines, no loud primary colors, no cartoon shadows.
- Happy colors (gold, sunset orange, soft pink) on a calm deep teal background.
- Very little text on screen. One clear answer, not a long list.

## Colors

| Use | Hex |
|---|---|
| Page background | `#0F2C31` |
| Card / input background | `#153A41` |
| Chip background (small tags) | `#1F4E57` |
| Card border | `#285A63` |
| Input / pill border | `#4A8892` |
| Main text | `#FFF7EC` |
| Muted text and labels | `#A9C4C6` |
| Gold (main accent, buttons, chosen tags, top pick border) | `#FFD27A` |
| Sunset orange (accent, selected party size) | `#FF8A4C` |
| Soft pink (third accent, place number 3) | `#FF9EB5` |
| Text on gold / orange / pink | `#1A0F0A` |
| Photo card text panel | `rgba(15, 44, 49, 0.86)` |

Decoration: one big orange circle (280 px) in the top right corner, partly off the screen (`right: -90px; top: -90px`). It looks like a setting sun.

## Fonts

- Headings and the wordmark: **Sora**, weight 700 or 800, slightly tight letter spacing (`-0.01em` to `-0.03em`).
- Body, buttons, labels: **DM Sans**, weights 400, 500, 700.
- Both from Google Fonts.
- Small labels (THE AREA, THE VIBE, GOING AS, OR TRY): 14 px, weight 700, letter spacing `0.1em`, uppercase, muted color.

Sizes used: page title "Where to?" 72 px. Top pick name 44 px. Backup names 22 px. Body text 17 to 22 px. Button text 15 to 19 px.

## Shape and spacing

- Cards: 22 to 26 px rounded corners, 1 px border.
- Inputs: 18 to 20 px corners.
- Buttons and pills: fully round (radius half the height).
- Every tap target is at least 44 px tall.
- Page content is centered, max width 880 px for the search screen and 1200 px for results.
- Gap between sections: 32 to 44 px.

## Logo

Two martini glasses leaning in and clinking, one gold and one orange, with three small gold spark lines above where they touch. File: `logo.svg`. The wordmark "Clink" sits next to it in Sora 800, 30 px.

## Screens

### 1. Search (solo and group versions)

Top to bottom:

1. Logo and wordmark.
2. Title: "Where **to?**" with "to?" in gold.
3. **THE AREA**: text input with a pin icon, plus a "Near me" outline button.
4. **GOING AS**: three pills, Solo, Couple, Group. The chosen one is filled orange with dark text. When Group is chosen, a small stepper (minus, number, plus) appears next to the pills.
5. **THE VIBE** (tags, not free text):
   - A box holding the chosen tags as gold chips, each with an x to remove it, plus a text field to type in.
   - Small helper line: "Type anything. Pick the tag it matches."
   - A suggestion list under the box. The first row is the best match ("Chill, matches 'lowkey'"). The last row is "+ Add 'lowkey' as a new tag".
   - A row of outline shortcut chips: Cozy, Date night, Lively, Rooftop, Live music.
6. A gold **Find places** button on the right.

### 2. Results

- Top bar: a recap of the search as small pills (party size, area, then the chosen tags as gold chips) and an **Edit** link that goes back to the search screen.
- Left side:
  - **Top pick**: one big card, 540 px tall, with a gold 2 px border. A photo of the place fills the whole card. A "TOP PICK" gold badge sits in the top left. A dark translucent panel at the bottom holds the name, price and walking time, one sentence saying why it fits, two small tag chips, and a gold **Open in Maps** button.
  - **OR TRY**: two smaller photo cards side by side with the same layout. A round numbered badge (2 orange, 3 pink) sits in the top left. The button is an outline **Open in Maps**.
- Right side: a small map, 440 px wide, with a 26 px rounded border. You are the white dot in the middle. Places are numbered round pins that match the cards. Pin 1 is gold and larger, 2 is orange, 3 is pink.
- In the mockup the photos are drawn illustrations. In the real app, use a real photo if there is one. If there is none, use a plain dark card with the place name. Do not show Yelp photos on any public site (the Yelp dataset license does not allow it).

## Behavior notes

- Typing in the vibe box suggests tags. Search runs only on tags, never on raw text.
- Picking a suggestion turns the typed word into a chip.
- "+ Add as a new tag" saves the word as a candidate tag for review. It is not trusted until checked.
- The "why it fits" line must come from review evidence. Never show a reason the data does not support.
- Show only one top pick and two backups. Do not add a long list.
- The map is secondary. Build the cards first and the map last. Use Leaflet with OpenStreetMap. "Open in Maps" hands off to the phone's maps app, so do not build navigation.

## Accessibility

- Text on dark backgrounds is `#FFF7EC` or `#A9C4C6`. Text on gold, orange and pink is `#1A0F0A`.
- Every icon-only button has an `aria-label`.
- Do not use color alone to show the chosen state. The chosen pill is also filled and bold.

## Do not

- No thick black outlines, no hard offset shadows, no bright yellow page background. An early version had them and was rejected as childish.
- No long walls of text.
- No extra screens (accounts, saved lists, booking) in the first version.
