/**
 * wedding-data.js — Customer-facing editable data layer for marigold-bhavan
 * Wedding of Dalwinder Kaur Sidhu & Hardeep Singh Dhaliwal (Bride Side)
 */

window.WEDDING_DATA = {
  // Couple Information (Bride Side: Dalwinder & Hardeep)
  couple: {
    groom: "Dalwinder", // Primary name on card (Bride side order)
    bride: "Hardeep",   // Secondary name on card
    brideRealName: "Dalwinder Kaur Sidhu",
    groomRealName: "Hardeep Singh Dhaliwal",
    brideFirst: true,
    monogram: "DH",
    side: "Bride Side",
    heroSubtitle: "Together with their families, join us to celebrate the wedding of",
  },

  // Family & Parents Details
  parents: {
    bride: {
      sideTitle: "Bride's Family",
      title: "With the heavenly blessings of Late Sardar Harmail Singh Sidhu",
      father: "Late Sardar Harmail Singh Sidhu",
      mother: "Sardarni Charnjit Kaur Sidhu",
      familyLine: "Sidhu Family",
      village: "Village Bhaini, District Bathinda",
    },
    groom: {
      sideTitle: "Groom's Family",
      father: "Sardar Jagroop Singh Dhaliwal",
      mother: "Sardarni Beant Kaur Dhaliwal",
      familyLine: "Dhaliwal Family",
    },
  },

  // Wedding Core Date & Times
  wedding: {
    eventTitle: "Wedding of Dalwinder & Hardeep",
    dateLabel: "01.11.26",
    dayLine: "Sunday, 1st November 2026",
    timeLine: "7:00 AM (Anand Karaj) · 11:30 AM (Barat)",
    // ISO local time driving countdown timer (Anand Karaj 7:00 AM)
    start: "2026-11-01T07:00:00",
    end: "2026-11-01T17:00:00",
    timeZoneOffset: "+05:30",
  },

  // Invitation Message & Blessings
  invitation: {
    ikOnkar: "ੴ ਸਤਿਗੁਰ ਪ੍ਰਸਾਦਿ",
    shabad: "ਲਖ ਖੁਸੀਆ ਪਾਤਿਸਾਹੀਆ ਜੇ ਸਤਿਗੁਰੁ ਨਦਰਿ ਕਰੇਇ ॥",
    note: "With the divine grace of Sri Guru Granth Sahib Ji and heavenly blessings of our elders, we cordially invite you to grace the auspicious wedding ceremony of our beloved daughter Dalwinder with Hardeep.",
    closing: "With Best Compliments from Near & Dear Ones",
  },

  // Wedding Events Programme / Itinerary
  events: [
    {
      id: "jaggo",
      title: "Jaggo & Sangeet",
      punjabiTitle: "ਜਾਗੋ ਅਤੇ ਸੰਗੀਤ",
      badge: "Pre-Wedding Celebration",
      dayLine: "Saturday, 31st October 2026",
      timeLine: "Evening onwards",
      venueName: "Family Residence",
      address: "Village Bhaini, District Bathinda, Punjab",
      description: "An auspicious night illuminated with glowing Jaggo lights, lively Giddha & Bhangra beats, and cherished Punjabi boliyan.",
      mapQuery: "Village Bhaini Bathinda Punjab",
      mapUrl: "https://www.google.com/maps/search/?api=1&query=Village+Bhaini+Bathinda+Punjab",
    },
    {
      id: "anand-karaj",
      title: "Anand Karaj (Lavaan)",
      punjabiTitle: "ਅਨੰਦ ਕਾਰਜ (ਚਾਰ ਲਾਵਾਂ)",
      badge: "Sacred Wedding Ceremony",
      dayLine: "Sunday, 1st November 2026",
      timeLine: "7:00 AM",
      venueName: "Gurudwara Sri Guru Hargobind Sahib Ji",
      address: "Bhaini, District Bathinda / Barnala, Punjab",
      description: "The sacred Four Lavaan ceremony solemnising the spiritual union in the holy presence of Sri Guru Granth Sahib Ji.",
      mapQuery: "Gurudwara Sri Guru Hargobind Sahib ji Bhaini",
      mapUrl: "https://www.google.com/maps/search/?api=1&query=Gurudwara+Sri+Guru+Hargobind+Sahib+ji+Bhaini",
    },
    {
      id: "barat-reception",
      title: "Welcome of Barat & Reception",
      punjabiTitle: "ਬਰਾਤ ਸੁਆਗਤ ਅਤੇ ਪ੍ਰੀਤੀ ਭੋਜ",
      badge: "Grand Luncheon & Festivities",
      dayLine: "Sunday, 1st November 2026",
      timeLine: "11:30 AM",
      venueName: "The Grand Venice Resort",
      address: "Barnala Road, Bhadaur, Punjab 148103",
      description: "Warm welcome of the Barat followed by celebratory luncheon, musical performances, and joyous blessings for the newlyweds.",
      mapQuery: "The Grand Venice, Barnala Road, Bhadaur, Punjab",
      mapUrl: "https://maps.app.goo.gl/bik3NP8SpQhrkmPaA?g_st=iw",
    },
  ],

  // Venue & Directions
  venue: {
    name: "The Grand Venice Resort",
    address: "Barnala Road, Bhadaur, Punjab 148103",
    city: "Bhadaur, Punjab",
    query: "The Grand Venice, Barnala Road, Bhadaur, Punjab 148103",
    lat: 30.4815,
    lng: 75.3218,
    mapSearchUrl: "https://maps.app.goo.gl/bik3NP8SpQhrkmPaA?g_st=iw",
    directionsUrl: "https://maps.app.goo.gl/bik3NP8SpQhrkmPaA?g_st=iw",
  },

  // Photo Gallery / Moments
  gallery: [
    {
      src: "./editable/assets/photo-together.jpg",
      title: "Better Together",
      subtitle: "Dalwinder & Hardeep",
    },
    {
      src: "./editable/assets/photo-field-upright.jpg?v=20261101",
      title: "Forever & Always",
      subtitle: "A Sacred Journey Begins",
    },
  ],

  // Images
  images: {
    couple: "./editable/assets/couple.png",
    footerBg: "./editable/assets/footer-bg.jpg",
    map: "./editable/assets/map.jpg",
    photoTogether: "./editable/assets/photo-together.jpg",
    photoField: "./editable/assets/photo-field-upright.jpg?v=20261101",
    ogImage: "./editable/assets/og-image.jpg",
  },
  websiteUrl: "https://dalwinder-weds-hardeep.invitingyou.top/",

  // Background Music
  music: {
    title: "Rab Khaire Kra",
    subtitle: "Rabb Khair Kare",
    audioSrc: "./editable/assets/rab-khaire-kra.mp3",
    autoPlayOnOpen: true,
  },
};
