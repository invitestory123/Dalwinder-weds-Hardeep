# Customer Editing Guide — marigold-bhavan (Wedding Edition)

This template is an elegant royal Indian wedding invitation with an interactive wax seal gate opener, sacred Ik Onkar blessings, bride-first couple showcase, family & parents lineage cards, comprehensive wedding programme itinerary, captured moments gallery, venue details with live Google Maps link, and ambient background music.

---

## Normal Customer Changes

All routine customer edits are configured in:
→ [editable/wedding-data.js](file:///c:/invitestory/week4/dalwinder-wds-hardeep/editable/wedding-data.js)

### Couple names & Monogram
Edit `couple` in `editable/wedding-data.js`:
- `couple.groom`: First name displayed (e.g. `"Dalwinder"` for bride-side priority)
- `couple.bride`: Second name displayed (e.g. `"Hardeep"`)
- `couple.brideRealName`: Full name of bride (e.g. `"Dalwinder Kaur Sidhu"`)
- `couple.groomRealName`: Full name of groom (e.g. `"Hardeep Singh Dhaliwal"`)
- `couple.monogram`: Wax seal monogram (e.g. `"DH"`)
- `couple.heroSubtitle`: Custom intro headline (e.g. `"Together with their families, join us to celebrate the wedding of"`)
- `couple.hashtag`: Wedding celebration hashtag (e.g. `"#Hardil"`)

### Parents & Family Details
Edit `parents` in `editable/wedding-data.js`:
- `parents.bride.father`: Bride's father (e.g. `"Late Sardar Harmail Singh Sidhu"`)
- `parents.bride.mother`: Bride's mother (e.g. `"Sardarni Charnjit Kaur Sidhu"`)
- `parents.bride.village`: Village/District (e.g. `"Village Bhaini, District Bathinda"`)
- `parents.groom.father`: Groom's father (e.g. `"Sardar Jagroop Singh Dhaliwal"`)
- `parents.groom.mother`: Groom's mother (e.g. `"Sardarni Beant Kaur Dhaliwal"`)

### Wedding Date & Times
Edit in `wedding` block:
- `dateLabel`: short date (e.g. `"01.11.26"`)
- `dayLine`: formatted day string (e.g. `"Sunday, 1st November 2026"`)
- `timeLine`: formatted time string (e.g. `"7:00 AM (Anand Karaj) · 11:30 AM (Barat)"`)
- `start` & `end`: ISO timestamp strings driving the live countdown timer.

### Sacred Blessings & Invitation Note
Edit `invitation` block:
- `invitation.ikOnkar`: `"ੴ ਸਤਿਗੁਰ ਪ੍ਰਸਾਦਿ"`
- `invitation.shabad`: `"ਲਖ ਖੁਸੀਆ ਪਾਤਿਸਾਹੀਆ ਜੇ ਸਤਿਗੁਰੁ ਨਦਰਿ ਕਰੇਇ ॥"`
- `invitation.note`: Heartfelt invitation invitation text.
- `invitation.closing`: Closing sign-off note.

### Events Programme / Itinerary
Edit `events` array with each ceremony:
- **Jaggo & Sangeet**: 31st October 2026 at Village Bhaini, Distt. Bathinda
- **Anand Karaj (Lavaan)**: 1st November 2026, 7:00 AM at Gurudwara Sri Guru Hargobind Sahib Ji, Bhaini
- **Welcome of Barat & Reception**: 1st November 2026, 11:30 AM at The Grand Venice Resort, Bhadaur

### Venue & Maps
Edit `venue` in `editable/wedding-data.js`:
- `venue.name`: `"The Grand Venice Resort"`
- `venue.address`: `"Barnala Road, Bhadaur, Punjab 148103"`
- `venue.directionsUrl` & `mapSearchUrl`: `"https://maps.app.goo.gl/bik3NP8SpQhrkmPaA?g_st=iw"`

### Background Music
Edit `music` block:
- `music.title`: `"Rab Khaire Kra"`
- `music.audioSrc`: `"./editable/assets/rab-khaire-kra.mp3"`

### Images & Moments
Images stored in `editable/assets/`:
- Hero couple illustration: `editable/assets/couple.png`
- Couple portrait ("Better Together"): `editable/assets/photo-together.jpg`
- Couple field portrait: `editable/assets/photo-field.jpg`
- Footer background: `editable/assets/footer-bg.jpg`
- Map illustration: `editable/assets/map.jpg`

---

## Special Sections & Features

- **Wax Seal Opener Gate**: Fullscreen intro that opens on tap or click with gold petal animations. Automatically initiates background music playback upon opening.
- **Background Music Player**: Floating audio toggle with sound waves, spinning vinyl aura, and song title badge.
- **Countdown Timer**: Real-time counter derived from `wedding.start`.
- **Calendar & Share Action Bar**: Fixed bottom bar allows guests to save `.ics` file, open Google Calendar, view directions, or share/copy invitation link.
