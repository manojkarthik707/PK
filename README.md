# Praveen & Shalini Wedding Invitation & Royal Studio Editor

A luxury web-based wedding invitation application with a dedicated visual customization studio.

---

## 🌟 Features

- **Royal Invitation Experience (`index.html`)**:
  - **3D Royal Envelope Stage**: 3D folding flaps, Damask gold foil patterns, SVG corner flourishes, rotating sunburst, and animated wax seal with smooth unsealing transition.
  - **Canvas Particle System**: Ambient floating gold dust effect powered by HTML5 Canvas.
  - **Couple Presentation**: Elegant typography, academic & company credentials, luxury gold frame photo holder with crown emblem.
  - **Live Muhurtham Countdown**: Dynamic countdown timer ticking down to Subamuhurtham.
  - **Sacred Event Venue Card**: Event timings, hall address, and interactive Google Maps direction link.
  - **Family Greetings & Thirukkural**: Groom's and Bride's parents' details and traditional blessing verse.
  - **Background Audio**: Romantic wedding piano track with floating playback toggle.
  - **One-Click Quick Edit**: Floating `✏️ Edit` button to jump straight into the studio editor.

- **Royal Invitation Studio Editor (`editor.html`)**:
  - **Live Side-by-Side Dual Pane**: Make changes on the left, watch them reflect immediately in the simulated smartphone frame on the right.
  - **Couple Details**: Customize Groom & Bride names, degrees, professions, and monogram initials (e.g. `P&S`).
  - **Muhurtham & Countdown**: Set wedding dates and pick exact countdown target timestamps.
  - **Venue & Google Maps**: Modify marriage hall name, address, and maps URL.
  - **Quotes & Words**: Change Thirukkural / auspicious verses and invitation body paragraphs.
  - **Family Column**: Edit Groom's and Bride's parents and locations.
  - **Photo & Music Uploaders**: Drag & drop or pick custom couple portrait, hero banner, or audio track.
  - **Regal Color Themes**: Choose between *Royal Burgundy*, *Sacred Emerald*, *Midnight Sapphire*, and *Imperial Plum*.
  - **Interactive Tools**: Test "Re-seal Envelope" and audio toggle inside the preview.
  - **Dedicated "💾 Save Changes" Button**:
    - Prominent save button in the top navigation bar and a sticky save bar at the bottom of the controls panel.
    - Directly writes and saves your modifications to `index.html` on your computer.
    - Keyboard shortcut: **`Ctrl + S`** (or `Cmd + S` on Mac) triggers an instant save.
    - Dynamic status badge: displays `● All changes saved` or `● Unsaved changes...` with the exact timestamp of the last save.
  - **Auto-Save & Local Backup**: Automatically preserves your working draft in `localStorage` and writes `invitation-data.json` for backup.
  - **Export / Download HTML**: Option to download a standalone, self-contained `index.html` file anytime.

---

## 📁 File Structure

```
pk/
├── index.html       # The main wedding invitation page
├── editor.html      # Visual studio editor with real-time live preview
├── wedding.jpeg     # Couple portrait photo (used in royal frame)
├── reception.jpeg   # Hero banner background photograph
├── bgmusic.mp3      # Romantic wedding piano audio track
└── README.md        # Documentation and quickstart guide
```

---

## 🚀 How to Run & Use Locally

You can open either file directly in your browser, or run a local server:

### 1. Start a local server:
```powershell
python -m http.server 3000
```

### 2. Access the apps:
- **Visual Studio Editor**: [http://localhost:3000/editor.html](http://localhost:3000/editor.html)
- **Wedding Invitation**: [http://localhost:3000/index.html](http://localhost:3000/index.html)

*(You can also double-click `editor.html` or `index.html` to open them directly in Google Chrome, Microsoft Edge, or any browser).*
