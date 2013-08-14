#!/usr/bin/env python
#coding=utf-8

RULERS = {
    "aerotechnews.com": {
        "name": "Aerotech News and Review",
        "url": "www.aerotechnews.com",
        "language": 2,
        "rulers": set(["http://www.aerotechnews.com/news/",
                       "http://www.aerotechnews.com/edwardsafb/",
                       "http://www.aerotechnews.com/ntcfortirwin/",
                       "http://www.aerotechnews.com/marcharb/",
                       "http://www.aerotechnews.com/laafb/",
                       "http://www.aerotechnews.com/nellisafb/",
                       "http://www.aerotechnews.com/davis-monthanafb/",
                       "http://www.aerotechnews.com/lukeafb/",
                       "http://www.aerotechnews.com/forthuachuca/",
                       "http://www.aerotechnews.com/mcasyuma/"])
    },
    "uk-airport-news.info": {
        "name": "UK Aiport News",
        "url": "www.uk-airport-news.info",
        "language": 2,
        "rulers": set(["http://www.uk-airport-news.info/"])
    },
    "airspacemag.com": {
        "name": "AIR & SPACE Magazine",
        "url": "www.airspacemag.com",
        "language": 2,
        "rulers": set(["http://www.airspacemag.com/history-of-flight/",
                       "http://www.airspacemag.com/flight-today/",
                       "http://www.airspacemag.com/military-aviation/",
                       "http://www.airspacemag.com/space-exploration/",
                       "http://www.airspacemag.com/need- to-know/",
                       "http://www.airspacemag.com/how-things-work/",
                       "http://www.airspacemag.com/multimedia/",
                       "http://www.airspacemag.com/daily-planet/",
                       "http://www.airspacemag.com/view/"])
    },
    "anna.aero": {
        "name": "anna.aero Airport News",
        "url": "www.anna.aero",
        "language": 2,
        "rulers": set(["http://www.anna.aero/category/top-story/",
                       "http://www.anna.aero/category/all-new-airline-routes/",
                       "http://www.anna.aero/category/latest-airline-route-news/",
                       "http://www.anna.aero/category/airline-analysis/",
                       "http://www.anna.aero/category/take-offs-landings/",
                       "http://www.anna.aero/category/airport-analysis/",
                       "http://www.anna.aero/category/country-feature/",
                       "http://www.anna.aero/category/airline-airport-strategy-interviews/",
                       "http://www.anna.aero/category/farewatch/",
                       "http://www.anna.aero/category/market-trends/",
                       "http://www.anna.aero/category/route-analysis/",
                       "http://www.anna.aero/network-planning-community-news/"])
    },
    "aviationweek.com": {
        "name": "Aviation Week",
        "url": "www.aviationweek.com",
        "language": 2,
        "rulers": set(["http://www.aviationweek.com/Article.aspx?id=/article-xml/"])
    },
    "defensenews.com": {
        "name": "Defense News",
        "url": "www.defensenews.com",
        "language": 2,
        "rulers": set(["http://www.defensenews.com/article/"])
    },
    "janes.com": {
        "name": "IHS Jane's 360",
        "url": "www.janes.com",
        "language": 2,
        "rulers": set(["http://www.janes.com/article/"])
    },
    "spacenews.com": {
        "name": "Space News",
        "url": "www.spacenews.com",
        "language": 2,
        "rulers": set(["http://www.spacenews.com/article/"])
    },
    "farmassist.com": {
        "name": "Farm Assist",
        "url": "www.farmassist.com",
        "language": 2,
        "rulers": set(["http://www.farmassist.com/Alerts/",
                       "http://www.farmassist.com/Prodrender/",
                       "http://www.farrmassist.com/PestLibrary/"])
    },
    "agweb.com": {
        "name": "U. S. Farm Report",
        "url": "www.agweb.com",
        "language": 2,
        "rulers": set(["http://www.agweb.com/article/",
                       "http://www.agweb.com/news/",
                       "http://www.agweb.com/markets/",
                       "http://www.agweb.com/crops/",
                       "http://www.agweb.com/livestock/",
                       "http://www.agweb.com/business/",
                       "http://www.agweb.com/land/",
                       "http://www.agweb.com/machinery/"])
    },
    "market-news.com": {
        "name": "Market News Reporter",
        "url": "www.market-news.com",
        "language": 2,
        "rulers": set(["http://www.market-news.com/"])
    },
    "ipm.iastate.edu": {
        "name": "Horticulture and Home Pest News",
        "url": "www.ipm.iastate.edu",
        "language": 2,
        "rulers": set(["http://www.ipm.iastate.edu/ipm/hortnews"])
    },
    "producer.com": {
        "name": "Western Producer",
        "url": "www.producer.com",
        "language": 2,
        "rulers": set(["http://www.producer.com/section/news/",
                       "http://www.producer.com/section/crops/",
                       "http://www.producer.com/section/livestock/",
                       "http://www.producer.com/section/markets/",
                       "http://www.producer.com/section/weather/",
                       "http://www.producer.com/section/farmliving/",
                       "http://www.producer.com/section/opinion/"])
    },
    "poultrypress.com": {
        "name": "Poultry Press",
        "url": "www.poultrypress.com",
        "language": 2,
        "rulers": set(["http://www.poultrypress.com/articles/"])
    },
    "dtnprogressivefarmer.com": {
        "name": "Progressive Farmer Online",
        "url": "www.dtnprogressivefarmer.com",
        "language": 2,
        "rulers": set(["http://about.dtnprogressivefarmer.com/ag/news_events/",
                       "http://www.dtnprogressivefarmer.com/dtnag/common/"])
    },
    "smallfarmersjournal.com": {
        "name": "Small Farmer's Journal",
        "url": "smallfarmersjournal.com",
        "language": 2,
        "rulers": set(["http://smallfarmersjournal.com/"])
    },
    "underwatertimes.com": {
        "name": "Underwater Times",
        "url": "www.underwatertimes.com",
        "language": 2,
        "rulers": set(["http://www.underwatertimes.com/"])
    },
    "lepidopterology.com": {
        "name": "Lepidopterology",
        "url": "www.lepidopterology.com",
        "language": 2,
        "rulers": set(["http://www.lepidopterology.com/"])
    },
    "critterchatter.com": {
        "name": "Critter Chatter",
        "url": "www.critterchatter.com",
        "language": 2,
        "rulers": set(["http://www.critterchatter.com/"])
    },
    "rmca.org": {
        "name": "Rat & Mouse Gazette",
        "url": "www.rmca.org",
        "language": 2,
        "rulers": set(["http://mouseknight.rmca.org/",
                       "http://squeaks.rmca.org/",
                       "http://www.rmca.org/Stories/airabella/",
                       "http://www.rmca.org/Articles/",
                       "http://www.rmca.org/Resources/"])
    },
    "jwsr.org": {
        "name": "Journal of World-Systems Research",
        "url": "www.jwsr.org",
        "language": 2,
        "rulers": set(["http://www.jwsr.org/"])
    },
    "ucla.edu": {
        "name": "Anthropoetics",
        "url": "www.anthropoetics.ucla.edu",
        "language": 2,
        "rulers": set(["http://www.anthropoetics.ucla.edu/news_files/",
                       "http://www.anthropoetics.ucla.edu/views/",
                       "http://www.anthropoetics.ucla.edu/GASC/"]),
    },
    "ajaonline.org": {
        "name": "American Journal of Archaeology",
        "url": "www.ajaonline.org",
        "language": 2,
        "rulers": set(["http://www.ajaonline.org/article/",
                       "http://www.ajaonline.org/online-review-book/",
                       "http://www.ajaonline.org/field-report/",
                       "http://www.ajaonline.org/necrology/",
                       "http://www.ajaonline.org/submissions/",
                       "http://www.ajaonline.org/about/"])
    },
    "athenapub.com": {
        "name": "Athena Review",
        "url": "www.athenapub.com",
        "language": 2,
        "rulers": set(["http://www.athenapub.com/"])
    },
    "anistor.gr": {
        "name": "Anistoriton",
        "url": "www.anistor.gr",
        "language": 2,
        "rulers": set(["http://www.anistor.gr/music/"])
    },
    "jackstargazer.com": {
        "name": "Jack Horkheimer: Star Gazer",
        "url": "www.jackstargazer.com",
        "language": 2,
        "rulers": set(["http://www.jackstargazer.com/"])
    },
    "portaltotheuniverse.org": {
        "name": "Portal to the Universe",
        "url": "www.portaltotheuniverse.org",
        "language": 2,
        "rulers": set(["http://www.portaltotheuniverse.org/news/",
                       "http://www.portaltotheuniverse.org/review/"])
    },
    "radio.seti.org": {
        "name": "Are We Alone? - SETI Institute Science Radio",
        "url": "radio.seti.org",
        "language": 2,
        "rulers": set(["http://radio.seti.org/episodes/",
                       "http://radio.seti.org/blog/"])
    },
    "astroppo.com": {
        "name": "Astroppo",
        "url": "www.astroppo.com",
        "language": 2,
        "rulers": set(["http://www.astroppo.com/"])
    },
    "astronomy.com": {
        "name": "Astronomy.com",
        "url": "www.astronomy.com",
        "language": 2,
        "rulers": set(["http://www.astronomy.com/en/Magazine/",
                       "http://www.astronomy.com/en/News-Observing/",
                       "http://www.astronomy.com/en/Multimedia/",
                       "http://www.astronomy.com/Columnists/"])
    },
    "skyandtelescope.com": {
        "name": "Sky & Telescope: The Essential Magazine of Astronomy",
        "url": "www.skyandtelescope.com",
        "language": 2,
        "rulers": set(["http://www.skyandtelescope.com/news/",
                       "http://www.skyandtelescope.com/observing/"])
    },
    "astronomynow.com": {
        "name": "Astronomy Now Online",
        "url": "www.astronomynow.com",
        "language": 2,
        "rulers": set(["http://www.astronomynow.com/news/"])
    },
    "stardate.org": {
        "name": "StarDate Online",
        "url": "stardate.org",
        "language": 2,
        "rulers": set(["http://stardate.org/radio/program/",
                       "http://stardate.org/nightsky/",
                       "http://stardate.org/astro-guide/",
                       "http://stardate.org/mediacenter/",
                       "http://blackholes.stardate.org/"])
    },
    "nightskyobserver.com": {
        "name": "Night Sky Observer",
        "url": "www.nightskyobserver.com",
        "language": 2,
        "rulers": set(["http://www.nightskyobserver.com/astronomy-news/",
                       "http://www.nightskyobserver.com/the-sky-this-month/"])
    },
    "oneminuteastronomer.com": {
        "name": "oneminuteastronomer.com",
        "url": "www.oneminuteastronomer.com",
        "language": 2,
        "rulers": set(["http://www.oneminuteastronomer.com/articles/",
                       "http://www.oneminuteastronomer.com/stargazer-university/"
                       "http://www.oneminuteastronomer.com/sky-this-month/",
                       "http://www.oneminuteastronomer.com/archives/"])
    },
    "moonfacts.net": {
        "name": "moonfacts.net",
        "url": "www.moonfacts.net",
        "language": 2,
        "rulers": set(["http://www.moonfacts.net/moon-news/",
                       "http://www.moonfacts.net/moon-name-meanings/",
                       "http://www.moonfacts.net/moon-resources/",
                       "http://www.moonfacts.net/observing-resources/"])
    },
    "astronomy.ie": {
        "name": "Astronomy and Space",
        "url": "www.astronomy.ie",
        "language": 2,
        "rulers": set(["http://www.astronomy.ie/"])
    },
    "skynews.ca": {
        "name": "SkyNews",
        "url": "www.skynews.ca",
        "language": 2,
        "rulers": set(["http://www.skynews.ca/"])
    },
    "womanastronomer.com": {
        "name": "Woman Astronomer",
        "url": "www.womanastronomer.com",
        "language": 2,
        "rulers": set(["http://www.womanastronomer.com/"])
    },
    "arm.ac.uk": {
        "name": "Irish Astronomical Journal",
        "url": "www.arm.ac.uk/latest.html",
        "language": 2,
        "rulers": set(["http://www.arm.ac.uk/latest.html"
                       "http://www.arm.ac.uk/press/"])
    },
    "the-scientist.com": {
        "name": "The Scientist",
        "url": "www.the-scientist.com",
        "language": 2,
        "rulers": set(["http://www.the-scientist.com/?articles.view/articleNo/"])
    },
    "bioworld.com": {
        "name": "BioWorld Online",
        "url": "www.bioworld.com",
        "language": 2,
        "rulers": set(["http://www.bioworld.com/latest_news/",
                       "http://www.bioworld.com/analysis/",
                       "http://www.bioworld.com/content/",
                       "http://www.bioworld.com/conferences/"])
    },
    "biosciencetechnology.com": {
        "name": "Bioscience Technology",
        "url": "www.biosciencetechnology.com",
        "language": 2,
        "rulers": set(["http://www.biosciencetechnology.com/News/",
                       "http://www.biosciencetechnology.com/product-releases/",
                       "http://www.biosciencetechnology.com/Articles/",
                       "http://www.biosciencetechnology.com/events/",
                       "http://www.biosciencetechnology.com/podcasts/"])
    },
    "genome-technology.com": {
        "name": "Genome Technology Magazine",
        "url": "www.genome-technology.com",
        "language": 2,
        "rulers": set(["http://www.genome-technology.com/arrays/",
                       "http://www.genome-technology.com/clinical-genomics/",
                       "http://www.genome-technology.com/informatics/",
                       "http://www.genome-technology.com/pcr/",
                       "http://www.genome-technology.com/proteomics/",
                       "http://www.genome-technology.com/rnai/",
                       "http://www.genome-technology.com/sequencing/",
                       "http://www.genome-technology.com/blog/"])
    },
    "newscientist.com": {
        "name": "New Scientist",
        "url": "www.newscientist.com",
        "language": 2,
        "rulers": set(["http://www.newscientist.com/articles/",
                       "http://www.newscientist.com/gallery/"])
    },
    "cbinpractice.org": {
        "name": "Conservation Biology in Practice",
        "url": "www.cbinpractice.org",
        "language": 2,
        "rulers": set(["http://www.cbinpractice.org/"])
    },
    "radres.org": {
        "name": "Radiation Research",
        "url": "www.radres.org",
        "language": 2,
        "rulers": set(["http://www.radres.org/news/",
                       "http://www.radres.org/events/"])
    },
    "wisc.edu": {
        "name": "Journal of Chemical Education",
        "url": "jchemed.chem.wisc.edu",
        "language": 2,
        "rulers": set(["http://jchemed.chem.wisc.edu/arttcle/",
                       "http://jchemed.chem.wisc.edu/arttcle/blog/",
                       "http://jchemed.chem.wisc.edu/picks/",
                       "http://jchemed.chem.wisc.edu/activity/"])
    },
    "versita.com": {
        "name": "versita",
        "url": "www.versita.com",
        "language": 2,
        "rulers": set(["http://www.versita.com/"])
    },
    "waset.org": {
        "name": "World Academy of Science, Engineering and Technology",
        "url": "www.waset.org",
        "language": 2,
        "rulers": set(["http://www.waset.org/"])
    },
    "acm.org": {
        "name": "Association for Computing Machinery",
        "url": "www.acm.org",
        "language": 2,
        "rulers": set(["http://cacm.acm.org/",
                       "http://techpack.acm.org/",
                       "http://www.acm.org/news/"])
    },
    "ibm.com": {
        "name": "IBM Research",
        "url": "www.research.ibm.com",
        "language": 2,
        "rulers": set(["http://www.research.ibm.com/"])
    },
    "uchicago.edu": {
        "name": "Chicago Journal of Theoretical Computer Science",
        "url": "cjtcs.cs.uchicago.edu/",
        "language": 2,
        "rulers": set(["http://cjtcs.cs.uchicago.edu/articles/"])
    },
    "mit.edu": {
        "name": "The MIT Press",
        "url": "mitpress.mit.edu",
        "language": 2,
        "rulers": set(["http://mitpress.mit.edu/disciplines/",
                       "http://mitpress.mit.edu/blog/"])
    },
    "springer.com": {
        "name": "Springer Link",
        "url": "link.springer.com",
        "language": 2,
        "rulers": set(["http://link.springer.com/chapter/",
                       "http://link.springer.com/article/"])
    },
    "platts.com": {
        "name": "PLATTS",
        "url": "www.platts.com",
        "language": 2,
        "rulers": set(["http://blogs.platts.com/",
                       "http://www.platts.com/latest-news/",
                       "http://www.platts.com/news-feature/"])
    },
    "energycentral.com": {
        "name": "Energy Central",
        "url": "www.energycentral.com",
        "language": 2,
        "rulers": set(["http://www.energycentral.com/news/",
                       "http://www.energycentral.com/articles/",
                       "http://www.energycentral.com/events/",
                       "http://www.energycentral.com/utilitybusiness/",
                       "http://www.energycentral.com/generationstorage/",
                       "http://www.energycentral.com/gridtandd/",
                       "http://www.energycentral.com/enduse/"])
    },
    "matternetwork.com": {
        "name": "Matter Network",
        "url": "www.matternetwork.com",
        "language": 2,
        "rulers": set(["http://www.matternetwork.com/"])
    },
    "energy-business-review.com": {
        "name": "Energy Business Review",
        "url": "www.energy-business-review.com",
        "language": 2,
        "rulers": set(["http://www.energy-business-review.com/suppliers/",
                       "http://carbon.energy-business-review.com/news/",
                       "http://carbon.energy-business-review.com/suppliers/",
                       "http://coal.energy-business-review.com/news/",
                       "http://coal.energy-business-review.com/suppliers/",
                       "http://drillingandproduction.energy-business-review.com/news",
                       "http://drillingandproduction.energy-business-review.com/suppliers/",
                       "http://explorationanddevelopment.energy-business-review.com/news/",
                       "http://explorationanddevelopment.energy-business-review.com/suppliers/",
                       "http://fossilfuel.energy-business-review.com/news/",
                       "http://fossilfuel.energy-business-review.com/suppliers/",
                       "http://transportationandstorage.energy-business-review.com/news/",
                       "http://transportationandstorage.energy-business-review.com/suppliers/",
                       "http://refiningandpetrochemicals.energy-business-review.com/news/",
                       "http://refiningandpetrochemicals.energy-business-review.com/suppliers/",
                       "http://solar.energy-business-review.com/news/",
                       "http://solar.energy-business-review.com/suppliers/",
                       "http://biofuelsandbiomass.energy-business-review.com/news/",   
                       "http://biofuelsandbiomass.energy-business-review.com/suppliers/",
                       "http://nuclear.energy-business-review.com/news/",
                       "http://nuclear.energy-business-review.com/suppliers/",
                       "http://nuclearfuels.energy-business-review.com/news/",
                       "http://nuclearfuels.energy-business-review.com/suppliers/",
                       "http://mineralsandmaterials.energy-business-review.com/news/",
                       "http://mineralsandmaterials.energy-business-review.com/suppliers/",
                       "http://geothermal.energy-business-review.com/news/",
                       "http://geothermal.energy-business-review.com/suppliers/",
                       "http://wind.energy-business-review.com/news/",
                       "http://wind.energy-business-review.com/suppliers/",
                       "http://hydro.energy-business-review.com/news/",
                       "http://hydro.energy-business-review.com/suppliers/",
                       "http://utilitiesnetwork.energy-business-review.com/news",
                       "http://utilitiesnetwork.energy-business-review.com/suppliers/",
                       "http://utilitiesretail.energy-business-review.com/news/",
                       "http://utilitiesretail.energy-business-review.com/suppliers/",
                       "http://wind.cleantechnology-business-review.com/news/",
                       "http://wind.cleantechnology-business-review.com/suppliers/",
                       "http://solar.cleantechnology-business-review.com/news/",
                       "http://solar.cleantechnology-business-review.com/suppliers/",
                       "http://hydro.cleantechnology-business-review.com/news/",
                       "http://hydro.cleantechnology-business-review.com/suppliers/"])
    },
    "cleantechnology-business-review.com": {
        "name": "CTBR",
        "url": "www.cleantechnology-business-review.com",
        "language": 2,
        "rulers": set(["http://airandenvironmentmanagement.cleantechnology-business-review.com/news/",
                       "http://airandenvironmentmanagement.cleantechnology-business-review.com/suppliers/",
                       "http://biopower.cleantechnology-business-review.com/news/",
                       "http://biopower.cleantechnology-business-review.com/suppliers/",
                       "http://hydro.cleantechnology-business-review.com/news/",
                       "http://hydro.cleantechnology-business-review.com/suppliers/",
                       "http://waterwastemanagement.cleantechnology-business-review.com/news/",
                       "http://waterwastemanagement.cleantechnology-business-review.com/suppliers/",
                       "http://wind.cleantechnology-business-review.com/news/",
                       "http://wind.cleantechnology-business-review.com/suppliers/",
                       "http://recyclingandwastemanagement.cleantechnology-business-review.com/news/",
                       "http://recyclingandwastemanagement.cleantechnology-business-review.com/suppliers/",
                       "http://solar.cleantechnology-business-review.com/news/",
                       "http://solar.cleantechnology-business-review.com/suppliers/"])
    },
    "hydropower-dams.com": {
        "name": "International Journal on Hydropower & Dams",
        "url": "www.hydropower-dams.com",
        "language": 2,
        "rulers": set(["http://www.hydropower-dams.com/"])
    },
    "murdoch.edu.au": {
        "name": "Synergy: Leading Edge Research at Murdoch University",
        "url": "www.murdoch.edu.au/synergy/",
        "language": 2,
        "rulers": set(["http://www.murdoch.edu.au/synergy/"])
    },
    "theengineer.co.uk": {
        "name": "Engineertalk.com",
        "url": "www.theengineer.co.uk",
        "language": 2,
        "rulers": set(["http://www.theengineer.co.uk/aerospace/",
                       "http://www.theengineer.co.uk/automotive/",
                       "http://www.theengineer.co.uk/civil-and-structural/",
                       "http://www.theengineer.co.uk/electronics/",
                       "http://www.theengineer.co.uk/energy-and-environment/",
                       "http://www.theengineer.co.uk/medical-and-healthcare/",
                       "http://www.theengineer.co.uk/military-and-defence/",
                       "http://www.theengineer.co.uk/rail-and-marine/",
                       "http://www.theengineer.co.uk/channels/",
                       "http://www.theengineer.co.uk/in-depth/",
                       "http://www.theengineer.co.uk/news/",
                       "http://www.theengineer.co.uk/opinion/",
                       "http://www.theengineer.co.uk/home/blog/",
                       "http://www.theengineer.co.uk/blog/"])
    },
    "progressiveengineer.com": {
        "name": "Progressive Engineer",
        "url": "www.progressiveengineer.com",
        "language": 2,
        "rulers": set(["http://www.progressiveengineer.com/profiles/",
                       "http://www.progressiveengineer.com/company_profiles/"])
    },
    "acs.org": {
        "name": "C&EN",
        "url": "cen.acs.org",
        "language": 2,
        "rulers": set(["http://cen.acs.org/articles/"])
    },
    "techbriefs.com": {
        "name": "NASA Tech Briefs",
        "url": "www.techbriefs.com",
        "language": 2,
        "rulers": set(["http://www.techbriefs.com/tech-briefs/",
                       "http://www.techbriefs.com/component/content/article/",
                       "http://www.techbriefs.com/blog/"])
    },
    "canadiangeographic.ca": {
        "name": "Canadian Geographic Magazine",
        "url": "www.canadiangeographic.ca",
        "language": 2,
        "rulers": set(["http://www.canadiangeographic.ca/blog/",
                       "http://www.canadiangeographic.ca/magazine/"])
    },
    "geog.nau.edu": {
        "name": "Tourism Geographies",
        "url": "www.geog.nau.edu/tg/",
        "language": 2,
        "rulers": set(["http://www.geog.nau.edu/contents/"])
    },
    "joma.org": {
        "name": "Journal of Online Mathematics and its Applications (JOMA)",
        "url": "www.joma.org",
        "language": 2,
        "rulers": set(["http://www.joma.org/news/"])
    },
    "livingreviews.org": {
        "name": "LivingReviews",
        "url": "www.livingreviews.org",
        "language": 2,
        "rulers": set(["http://blog.livingreviews.org/"])
    },
    "sciencedaily.com": {
        "name": "ScienceDaily",
        "url": "www.sciencedaily.com",
        "language": 2,
        "rulers": set(["http://www.sciencedaily.com/releases/",
                       "http://www.sciencedaily.com/news/",
                       "http://www.sciencedaily.com/articles/"])
    },
    "eurekalert.org": {
        "name": "EurekAlert! Science News",
        "url": "www.eurekalert.org",
        "language": 2,
        "rulers": set(["http://www.eurekalert.org/bysubject/"])
    },
    "livescience.com": {
        "name": "livescience",
        "url": "www.livescience.com",
        "language": 2,
        "rulers": set(["http://www.livescience.com/"])
    },
    "sciencemag.org": {
        "name": "Science",
        "url": "www.sciencemag.org",
        "language": 2,
        "rulers": set(["http://news.sciencemag.org/",
                       "http://www.sciencemag.org/content/",
                       "http://www.sciencemag.org/site/products/",
                       "http://sciencecareers.sciencemag.org/career_magazine/previous_issues/articles/",
                       "http://blogs.sciencemag.org/origins/",
                       "http://blogs.sciencemag.org/newsblog/"])
    },
    "scitechdaily.com": {
        "name": "Scitechdaily",
        "url": "www.scitechdaily.com",
        "language": 2,
        "rulers": set(["http://www.scitechdaily.com/"])
    },
    "bbc.co.uk": {
        "name": "Science/Nature - BBC News",
        "url": "www.bbc.co.uk",
        "language": 2,
        "rulers": set(["http://www.bbc.co.uk/news/"])
    },
    "earthsky.org": {
        "name": "Earthsky",
        "url": "earthsky.org",
        "language": 2,
        "rulers": set(["http://earthsky.org/earth/",
                       "http://earthsky.org/space/",
                       "http://earthsky.org/human-world/",
                       "http://earthsky.org/science-wire/",
                       "http://earthsky.org/todays-image/",
                       "http://earthsky.org/tonight/"])
    },
    "alphagalileo.org": {
        "name": "AlphaGalileo",
        "url": "www.alphagalileo.org",
        "language": 2,
        "rulers": set(["http://www.alphagalileo.org/"])
    },
    "scienceagogo.com": {
        "name": "Science A Gogo",
        "url": "www.scienceagogo.com",
        "language": 2,
        "rulers": set(["http://www.scienceagogo.com/news/"])
    },
    "whyfiles.org": {
        "name": "The Why Files",
        "url": "whyfiles.org",
        "language": 2,
        "rulers": set(["http://whyfiles.org/"])
    },
    "esi-topics.com": {
        "name": "Essential Science Indicators Special Topics",
        "url": "www.esi-topics.com",
        "language": 2,
        "rulers": set(["http://www.esi-topics.com/"])
    },
    "creativecommons.org": {
        "name": "Science Commons",
        "url": "creativecommons.org",
        "language": 2,
        "rulers": set(["http://creativecommons.org/weblog/entry/"])
    },
    "plos.org": {
        "name": "PLOS",
        "url": "www.plos.org",
        "language": 2,
        "rulers": set(["http://blogs.plos.org",
                       "http://currents.plos.org"])
    },
    "plosone.org": {
        "name": "plosone",
        "url": "www.plosone.org",
        "language": 2,
        "rulers": set(["http://www.plosone.org/article/"])
    },
    "plosbiology.org": {
        "name": "plosbiology",
        "url": "www.plosbiology.org",
        "language": 2,
        "rulers": set(["http://www.plosbiology.org/article/"])
    },
    "plosmedicine.org": {
        "name": "plosmedicine",
        "url": "www.plosmedicine.org",
        "language": 2,
        "rulers": set(["http://www.plosmedicine.org/article/"])
    },
    "ploscompbiol.org": {
        "name": "ploscompbiol",
        "url": "www.ploscompbiol.org",
        "language": 2,
        "rulers": set(["http://www.ploscompbiol.org/article/"])
    },
    "plosgenetics.org": {
        "name": "plosgenetics",
        "url": "www.plosgenetics.org",
        "language": 2,
        "rulers": set(["http://www.plosgenetics.org/article/"])
    },
    "plospathogens.org": {
        "name": "plospathogens",
        "url": "www.plospathogens.org",
        "language": 2,
        "rulers": set(["http://www.plospathogens.org/article/"])
    },
    "plosntds.org": {
        "name": "plosntds",
        "url": "www.plosntds.org",
        "language": 2,
        "rulers": set(["http://www.plosntds.org/article/"])
    },
    "ploscollections.org": {
        "name": "ploscollections",
        "url": "www.ploscollections.org",
        "language": 2,
        "rulers": set(["http://www.ploscollections.org/article/"])
    },
    "hindawi.com": {
        "name": "Hindawi Publishing Corporation",
        "url": "www.hindawi.com",
        "language": 2,
        "rulers": set(["http://www.hindawi.com/journals/prt/contents/"
                       "http://www.hindawi.com/journals/srt/contents/",
                       "http://www.hindawi.com/journals/cggr/contents/",
                       "http://www.hindawi.com/journals/mse/contents/",
                       "http://www.hindawi.com/journals/pd/contents/",
                       "http://www.hindawi.com/journals/np/contents/"])
    },
    "nature.com": {
        "name": "nature nature.com",
        "url": "www.nature.com",
        "language": 2,
        "rulers": set(["http://www.nature.com/news/",
                       "http://www.nature.com/nature/journal/",
                       "http://blog.nature.com/"])
    },
    "mit.edu": {
        "name": "MIT Library",
        "url": "libraries.mit.edu",
        "language": 2,
        "rulers": set(["http://libraries.mit.edu/news/"])
    },
    "lbl.gov": {
        "name": "Berkeley Lab Science Beat",
        "url": "www.lbl.gov",
        "language": 2,
        "rulers": set(["http://www.lbl.gov/Science-Articles/"])
    },
    "nsf.gov": {
        "name": "Science Nation",
        "url": "www.nsf.gov",
        "language": 2,
        "rulers": set(["http://www.nsf.gov/news/",
                       "http://www.nsf.gov/discoveries/"])
    },
    "usgs.gov": {
        "name": "USGS",
        "url": "www.usgs.gov",
        "language": 2,
        "rulers": set(["http://www.usgs.gov"])
    },
    "science-news.org": {
        "name": "Science News",
        "url": "science-news.org",
        "language": 2,
        "rulers": set(["http://science-news.org"])
    },
    "abc.net.au": {
        "name": "ABC",
        "url": "www.abc.net.au",
        "language": 2,
        "rulers": set(["http://www.abc.net.au/science/articles/"])
    },
    "epigenie.com": {
        "name": "epigenie",
        "url": "epigenie.com",
        "language": 2,
        "rulers": set(["http://epigenie.com/"])
    },
    "scientificcage.com": {
        "name": "Scientific Cage",
        "url": "www.scientificcage.com",
        "language": 2,
        "rulers": set(["http://www.scientificcage.com/"])
    },
    "americanchemistry.com": {
        "name": "American Chemistry Council",
        "url": "www.americanchemistry.com",
        "language": 2,
        "rulers": set(["http://blog.americanchemistry.com/",
                       "http://www.americanchemistry.com/Media/PressReleasesTranscripts/ACC-news-releases/",
                       "http://www.americanchemistry.com/Innovation/",
                       "http://www.americanchemistry.com/Safety/",
                       "http://www.americanchemistry.com/Policy/",
                       "http://www.americanchemistry.com/ProductsTechnology/",
                       "http://polyurethane.americanchemistry.com/",
                       "http://plastics.americanchemistry.com/"])
    },
    "sciscoop.com": {
        "name": "SciScoop",
        "url": "www.sciscoop.com",
        "language": 2,
        "rulers": set(["http://www.sciscoop.com"])
    },
    "sciencewatch.com": {
        "name": "ScienceWatch.com",
        "url": "sciencewatch.com",
        "language": 2,
        "rulers": set(["http://sciencewatch.com/articles/"])
    },
    "scientificamerican.com": {
        "name": "Scientific American",
        "url": "www.scientificamerican.com",
        "language": 2,
        "rulers": set(["http://www.scientificamerican.com/"])
    },
    "newscientist.com": {
        "name": "New Scientist",
        "url": "www.newscientist.com",
        "language": 2,
        "rulers": set(["http://www.newscientist.com/article/"])
    },
    "sciencenews.org": {
        "name": "Science News",
        "url": "www.sciencenews.org",
        "language": 2,
        "rulers": set(["http://www.sciencenews.org/view/generic/id/"])
    },
    "scidev.net": {
        "name": "SciDev.net",
        "url": "www.scidev.net/global",
        "language": 2,
        "rulers": set(["http://www.scidev.net/"])
    },
    "thebulletin.org": {
        "name": "Bulletin of the Atomic Scientists",
        "url": "www.thebulletin.org",
        "language": 2,
        "rulers": set(["http://www.thebulletin.org/"])
    },
    "physicstoday.org": {
        "name": "Physics Today",
        "url": "www.physicstoday.org",
        "language": 2,
        "rulers": set(["http://www.physicstoday.org/daily_edition/"])
    },
    "smithsonianmag.com": {
        "name": "Smithsonian Magazine",
        "url": "www.smithsonianmag.com",
        "language": 2,
        "rulers": set(["http://blog.smithsonianmag.com",
                       "http://www.smithsonianmag.com/history-archaeology/",
                       "http://www.smithsonianmag.com/science-nature/",
                       "http://www.smithsonianmag.com/ideas-innovations/",
                       "http://www.smithsonianmag.com/arts-culture/",
                       "http://www.smithsonianmag.com/travel/"])
    },
    "seedmagazine.com": {
        "name": "SEED",
        "url": "seedmagazine.com",
        "language": 2,
        "rulers": set(["http://seedmagazine.com/content/article/"])
    },
    "americanscientist.org": {
        "name": "American Scientist",
        "url": "www.americanscientist.org",
        "language": 2,
        "rulers": set(["http://www.americanscientist.org/issues/",
                       "http://www.americanscientist.org/bookshelf/pub/",
                       "http://www.americanscientist.org/science/pub/"])
    },
    "cosmosmagazine.com": {
        "name": "Cosmos Magazine",
        "url": "www.cosmosmagazine.com",
        "language": 2,
        "rulers": set(["http://www.cosmosmagazine.com/features/"
                       "http://www.cosmosmagazine.com/cosmos_online/",
                       "http://www.cosmosmagazine.com/technology/",
                       "http://www.cosmosmagazine.com/health-genetics/",
                       "http://www.cosmosmagazine.com/opinion/",
                       "http://www.cosmosmagazine.com/planets-galaxies/",
                       "http://www.cosmosmagazine.com/news/",
                       "http://www.cosmosmagazine.com/science-in-society/",
                       "http://www.cosmosmagazine.com/environment-nature/",
                       "http://www.cosmosmagazine.com/blog/",
                       "http://www.cosmosmagazine.com/cosmos_magazine/",
                       "http://www.cosmosmagazine.com/reviews/",
                       "http://www.cosmosmagazine.com/weird-animals/"])
    },
    "issues.org": {
        "name": "Issues in Science and Technology",
        "url": "www.issues.org",
        "language": 2,
        "rulers": set(["http://www.issues.org/29.3/"])
    },
    "sea-technology.com": {
        "name": "Sea Technology",
        "url": "www.sea-technology.com",
        "language": 2,
        "rulers": set(["http://www.sea-technology.com/news/",
                       "http://www.sea-technology.com/features/"])
    },
    "naturalscience.com": {
        "name": "naturalSCIENCE",
        "url": "naturalscience.com",
        "language": 2,
        "rulers": set(["http://naturalscience.com/ns/articles/",
                       "http://naturalscience.com/ns/cover/",
                       "http://naturalscience.com/ns/letters/",
                       "http://naturalscience.com/ns/news/",
                       "http://naturalscience.com/ns/books/"])
    },
    "physicsworld.com": {
        "name": "Physics World",
        "url": "physicsworld.com",
        "language": 2,
        "rulers": set(["http://physicsworld.com/cws/article/",
                       "http://blog.physicsworld.com/"])
    },
    "australasianscience.com.au": {
        "name": "Australasian Science",
        "url": "www.australasianscience.com.au",
        "language": 2,
        "rulers": set(["http://www.australasianscience.com.au/article/",
                       "http://www.australasianscience.com.au/news/"])
    },
    "spectroscopyeurope.com": {
        "name": "Spectroscopy Europe",
        "url": "www.spectroscopyeurope.com",
        "language": 2,
        "rulers": set(["http://www.spectroscopyeurope.com/article/",
                       "http://www.spectroscopyeurope.com/news/",
                       "http://www.spectroscopyeurope.com/columns/",
                       "http://www.spectroscopyeurope.com/products/",
                       "http://www.spectroscopyeurope.com/blogs/",
                       "http://www.spectroscopyeurope.com/applications-library/",
                       "http://www.spectroscopyeurope.com/webinars/"])
    },
    "nationalgeographic.com": {
        "name": "National Geographic Magazine",
        "url": "www.nationalgeographic.com",
        "language": 2,
        "rulers": set(["http://news.nationalgeographic.com/",
                       "http://newswatch.nationalgeographic.com/",
                       "http://phenomena.nationalgeographic.com/",
                       "http://ngm.nationalgeographic.com/",
                       "http://maps.nationalgeographic.com/maps/",
                       "http://earthpulse.nationalgeographic.com/earthpulse/",
                       "http://science.nationalgeographic.com/science/",
                       "http://education.nationalgeographic.com/education/",
                       "http://games.nationalgeographic.com/",
                       "http://events.nationalgeographic.com/",
                       "http://intelligenttravel.nationalgeographic.com/",
                       "http://digitalnomad.nationalgeographic.com/ /explorers/",
                       "http://animals.nationalgeographic.com/animals/",
                       "http://environment.nationalgeographic.com/environment/",
                       "http://travel.nationalgeographic.com/travel/",
                       "http://adventureblog.nationalgeographic.com/"])
    },
    "dinosaurnews.org": {
        "name": "Dinosaurnews",
        "url": "www.dinosaurnews.org",
        "language": 2,
        "rulers": set(["http://www.dinosaurnews.org/"])
    },
    "us-tech.com": {
        "name": "US TECH",
        "url": "www.us-tech.com",
        "language": 2,
        "rulers": set(["http://www.us-tech.com/RelId/"])
    },
    "spectroscopyonline.com": {
        "name": "Spectroscopy",
        "url": "www.spectroscopyonline.com",
        "language": 2,
        "rulers": set(["http://www.spectroscopyonline.com/spectroscopy/Articles/",
                       "http://www.spectroscopyonline.com/spectroscopy/Departments%3A+Market+Profile/",
                       "http://www.spectroscopyonline.com/spectroscopy/static/",
                       "http://www.spectroscopyonline.com/spectroscopy/Events/",
                       "http://www.spectroscopyonline.com/spectroscopy/Departments%3A+News+Spectrum/News-Spectrum/"])
    },
    "laserfocusworld.com": {
        "name": "Laser Focus World",
        "url": "www.laserfocusworld.com",
        "language": 2,
        "rulers": set(["http://www.laserfocusworld.com/articles/",
                       "http://www.laserfocusworld.com/news/"])
    },
    "lia.org": {
        "name": "lia",
        "url": "www.lia.org",
        "language": 2,
        "rulers": set(["http://www.lia.org/blog/"])
    },
    "eurekamagazine.co.uk": {
        "name": "Eureka Magazine",
        "url": "www.eurekamagazine.co.uk",
        "language": 2,
        "rulers": set(["http://www.eurekamagazine.co.uk/design-engineering-news/",
                       "http://www.eurekamagazine.co.uk/design-engineering-products/",
                       "http://www.eurekamagazine.co.uk/design-engineering-features/",
                       "http://www.eurekamagazine.co.uk/design-engineering-blogs/",
                       "http://www.eurekamagazine.co.uk/design-engineering-events/"])
    },
    "llnl.gov": {
        "name": "Science & Technology Review",
        "url": "str.llnl.gov",
        "language": 2,
        "rulers": set(["http://str.llnl.gov"])
    },
    "informs.org": {
        "name": "OR/MS Today",
        "url": "www.informs.org",
        "language": 2,
        "rulers": set(["http://www.informs.org/ORMS-Today/Public-Articles/"])
    },
    "pennenergy.com": {
        "name": "pennenergy",
        "url": "www.pennenergy.com",
        "language": 2,
        "rulers": set(["http://www.pennenergy.com/articles/",
                       "http://www.pennenergy.com/wirenews/"])
    },
    "power-eng.com": {
        "name": "power-eng",
        "url": "www.power-eng.com",
        "language": 2,
        "rulers": set(["http://www.power-eng.com/articles/",
                       "http://www.power-eng.com/news/"])
    },
    "fireengineering.com": {
        "name": "fireengineering",
        "url": "www.fireengineering.com",
        "language": 2,
        "rulers": set(["http://community.fireengineering.com/",
                       "http://www.fireengineering.com/articles/"])
    },
    "waterworld.com": {
        "name": "waterworld",
        "url": "www.waterworld.com",
        "language": 2,
        "rulers": set(["http://www.waterworld.com/articles/"])
    },
    "dentistryiq.com": {
        "name": "dentistryiq",
        "url": "www.dentistryiq.com",
        "language": 2,
        "rulers": set(["http://www.dentistryiq.com/articles/"])
    },
    "cablinginstall.com": {
        "name": "cablinginstall",
        "url": "www.cablinginstall.com",
        "language": 2,
        "rulers": set(["http://www.cablinginstall.com/articles/"])
    },
    "ledsmagazine.com": {
        "name": "ledsmagazine",
        "url": "ledsmagazine.com",
        "language": 2,
        "rulers": set(["http://ledsmagazine.com/news/"])
    },
    "nsta.org": {
        "name": "Quantum",
        "url": "www.nsta.org/quantum/",
        "language": 2,
        "rulers": set(["http://www.nsta.org/quantum/"])
    },
    "exploratorium.edu": {
        "name": "Exploring: Exploratorium Magazine",
        "url": "www.exploratorium.edu",
        "language": 2,
        "rulers": set(["http://www.exploratorium.edu/exploring/"])
    },
    "symmetrymagazine.org": {
        "name": "symmetry",
        "url": "www.symmetrymagazine.org",
        "language": 2,
        "rulers": set(["http://www.symmetrymagazine.org/article/"])
    },
    "lbl.gov": {
        "name": "Lawrence Berkeley Laboratory Research Review",
        "url": "www.lbl.gov",
        "language": 2,
        "rulers": set(["http://www.lbl.gov/Science-Articles/Research-Review/"])
    },
    "selfhelpmagazine.com": {
        "name": "Self-Help Psychology Magazine",
        "url": "www.selfhelpmagazine.com",
        "language": 2,
        "rulers": set(["http://www.selfhelpmagazine.com/"])
    },
    "scientificamerican.com": {
        "name": "Scientific American Mind",
        "url": "www.scientificamerican.com/sciammind/",
        "language": 2,
        "rulers": set(["http://www.scientificamerican.com/sciammind/"])
    },
    "nationalpsychologist.com": {
        "name": "National Psychologist",
        "url": "www.nationalpsychologist.com",
        "language": 2,
        "rulers": set(["http://www.nationalpsychologist.com"])
    },
    "space.com": {
        "name": "SPACE.com",
        "url": "www.space.com",
        "language": 2,
        "rulers": set(["http://www.space.com"])
    },
    "space-travel.com": {
        "name": "SpaceDaily",
        "url": "www.space-travel.com",
        "language": 2,
        "rulers": set(["http://www.space-travel.com/reports/"])
    },
    "marsdaily.com": {
        "name": "marsdaily",
        "url": "www.marsdaily.com",
        "language": 2,
        "rulers": set(["http://www.marsdaily.com/reports/"])
    },
    "saturndaily.com": {
        "name": "saturndaily",
        "url": "www.saturndaily.com",
        "language": 2,
        "rulers": set(["http://www.saturndaily.com/reports/"])
    },
    "spacewar.com": {
        "name": "spacewar",
        "url": "www.spacewar.com",
        "language": 2,
        "rulers": set(["http://www.spacewar.com/reports/"])
    },
    "terradaily.com": {
        "name": "terradaily",
        "url": "www.terradaily.com",
        "language": 2,
        "rulers": set(["http://www.terradaily.com/reports/"])
    },
    "russodaily.com": {
        "name": "russodaily",
        "url": "www.russodaily.com",
        "language": 2,
        "rulers": set(["http://www.russodaily.com/reports/"])
    },
    "indodaily.com": {
        "name": "indodaily",
        "url": "www.indodaily.com",
        "language": 2,
        "rulers": set(["http://www.indodaily.com/reports/"])
    },
    "seeddaily.com": {
        "name": "seeddaily",
        "url": "www.seeddaily.com",
        "language": 2,
        "rulers": set(["http://www.seeddaily.com/reports/"])
    },
    "sinodaily.com": {
        "name": "sinodaily",
        "url": "www.sinodaily.com",
        "language": 2,
        "rulers": set(["http://www.sinodaily.com/reports/"])
    },
    "gpsdaily.com": {
        "name": "gpsdaily",
        "url": "www.gpsdaily.com",
        "language": 2,
        "rulers": set(["http://www.gpsdaily.com/reports/"])
    },
    "energy-daily.com": {
        "name": "energy-daily",
        "url": "www.energy-daily.com",
        "language": 2,
        "rulers": set(["http://www.energy-daily.com/reports/"])
    },
    "biofueldaily.com": {
        "name": "biofueldaily",
        "url": "www.biofueldaily.com",
        "language": 2,
        "rulers": set(["http://www.biofueldaily.com/reports/"])
    },
    "winddaily.com": {
        "name": "winddaily",
        "url": "www.winddaily.com",
        "language": 2,
        "rulers": set(["http://www.winddaily.com/reports/"])
    },
    "solardaily.com": {
        "name": "solardaily",
        "url": "www.solardaily.com",
        "language": 2,
        "rulers": set(["http://www.solardaily.com/reports/"])
    },
    "nuclearpowerdaily.com": {
        "name": "nuclearpowerdaily",
        "url": "www.nuclearpowerdaily.com",
        "language": 2,
        "rulers": set(["http://www.nuclearpowerdaily.com/reports/"])
    },
    "robodaily.com": {
        "name": "robodaily",
        "url": "www.robodaily.com",
        "language": 2,
        "rulers": set(["http://www.robodaily.com/reports/"])
    },
    "spacemart.com": {
        "name": "spacemart",
        "url": "www.spacemart.com",
        "language": 2,
        "rulers": set(["http://www.spacemart.com/reports/"])
    },
    "moondaily.com": {
        "name": "moondaily",
        "url": "www.moondaily.com",
        "language": 2,
        "rulers": set(["http://www.moondaily.com/reports/"])
    },
    "radardaily.com": {
        "name": "radardaily",
        "url": "www.radardaily.com",
        "language": 2,
        "rulers": set(["http://www.radardaily.com/reports/"])
    },
    "skynightly.com": {
        "name": "skynightly",
        "url": "www.skynightly.com",
        "language": 2,
        "rulers": set(["http://www.skynightly.com/reports/"])
    },
    "astronautix.com": {
        "name": "astronautix",
        "url": "www.astronautix.com",
        "language": 2,
        "rulers": set(["http://www.astronautix.com/craft/"])
    },
    "spaceflightnow.com": {
        "name": "Spaceflight Now",
        "url": "www.spaceflightnow.com",
        "language": 2,
        "rulers": set(["http://www.spaceflightnow.com/news/"])
    },
    "spaceref.com": {
        "name": "SpaceRef.com",
        "url": "www.spaceref.com",
        "language": 2,
        "rulers": set(["http://www.spaceref.com/astronomy/",
                       "http://www.spaceref.com/earth/",
                       "http://www.spaceref.com/mars/",
                       "http://www.spaceref.com/nasa-hack-space/",
                       "http://www.spaceref.com/news/",
                       "http://www.spaceref.com/onorbit/",
                       "http://www.spaceref.com/missions-and-programs/nasa/",
                       "http://www.spaceref.com/international-space-station/",
                       "http://www.spaceref.com/spaceweather/",
                       "http://www.spaceref.com/calendar/",
                       "http://www.spaceref.com/sun/",
                       "http://www.spaceref.com/exoplanets/"])
    },
    "esa.int": {
        "name": "Science & Technology",
        "url": "sci.esa.int",
        "language": 2,
        "rulers": set(["http://sci.esa.int/object/"])
    },
    "spacetoday.org": {
        "name": "Space Today Online (STO)",
        "url": "www.spacetoday.org",
        "language": 2,
        "rulers": set(["http://www.spacetoday.org/SpcStns/",
                       "http://www.spacetoday.org/Occurrences/",
                       "http://www.spacetoday.org/SpcShtls/",
                       "http://www.spacetoday.org/History/",
                       "http://www.spacetoday.org/SolSys/",
                       "http://www.spacetoday.org/Satellites",
                       "http://www.spacetoday.org/Japan/Japan/",
                       "http://www.spacetoday.org/Rockets/",
                       "http://www.spacetoday.org/Astronauts/",
                       "http://www.spacetoday.org/DeepSpace/",
                       "http://www.spacetoday.org/China/",
                       "http://www.spacetoday.org/Europe/",
                       "http://www.spacetoday.org/India/"])
    },
    "floridatoday.com": {
        "name": "Florida Today: Space",
        "url": "www.floridatoday.com",
        "language": 2,
        "rulers": set(["http://www.floridatoday.com/article/"])
    },
    "space.com": {
        "name": "Space News",
        "url": "www.space.com",
        "language": 2,
        "rulers": set(["http://www.space.com/"])
    },
    "tripod.com": {
        "name": "WWW Space and Mystery",
        "url": "spaceandmystery.tripod.com",
        "language": 2,
        "rulers": set(["http://spaceandmystery.tripod.com/"])
    },
    "orlandosentinel.com": {
        "name": "Orlando Sentinel: Space & Science",
        "url": "www.orlandosentinel.com",
        "language": 2,
        "rulers": set(["http://www.orlandosentinel.com/news/space/"])
    },
    "nss.org": {
        "name": "National Space Societ",
        "url": "www.nss.org",
        "language": 2,
        "rulers": set(["http://www.nss.org/news"])
    },
    "naveenjain.org": {
        "name": "Naveen Jain Space Explorers",
        "url": "www.naveenjain.org",
        "language": 2,
        "rulers": set(["http://www.naveenjain.org/"])
    },
    "asi.org": {
        "name": "Moon Miners' Manifesto",
        "url": "www.asi.org",
        "language": 2,
        "rulers": set(["http://www.asi.org/adb/"])
    },
    "wired.com": {
        "name": "Wired News",
        "url": "www.wired.com",
        "language": 2,
        "rulers": set(["http://www.wired.com/"])
    },
    "cnet.com": {
        "name": "CNET",
        "url": "www.cnet.com",
        "language": 2,
        "rulers": set(["http://reviews.cnet.com/",
                       "http://news.cnet.com/",
                       "http://download.cnet.com/",
                       "http://howto.cnet.com/"])
    },
    "zdnet.com": {
        "name": "ZDNet",
        "url": "www.zdnet.com",
        "language": 2,
        "rulers": set(["http://www.zdnet.com/"])
    },
    "techweb.com": {
        "name": "Techweb",
        "url": "www.techweb.com",
        "language": 2,
        "rulers": set(["http://www.techweb.com/news/"])
    },
    "freecode.com": {
        "name": "free code",
        "url": "freecode.com",
        "language": 2,
        "rulers": set(["http://freecode.com/articles/"])
    },
    "redherring.com": {
        "name": "Red Herring",
        "url": "www.redherring.com",
        "language": 2,
        "rulers": set(["http://www.redherring.com/internet/",
                       "http://www.redherring.com/clean-tech/",
                       "http://www.redherring.com/features/",
                       "http://www.redherring.com/finance/",
                       "http://www.redherring.com/global/",
                       "http://www.redherring.com/mobile/",
                       "http://www.redherring.com/social/",
                       "http://www.redherring.com/software/",
                       "http://www.redherring.com/startups/",
                       "http://www.redherring.com/top-100/"])
    },
    "theinquirer.net": {
        "name": "Inquirer",
        "url": "www.theinquirer.net",
        "language": 2,
        "rulers": set(["http://www.theinquirer.net/inquirer/news/",
                       "http://www.theinquirer.net/inquirer/review/"])
    },
    "betanews.com": {
        "name": "Beta News",
        "url": "betanews.com",
        "language": 2,
        "rulers": set(["http://betanews.com/"])
    },
    "valleywag.com": {
        "name": "Valleywag",
        "url": "www.valleywag.com",
        "language": 2,
        "rulers": set(["http://www.valleywag.com/"])
    },
    "siliconvalley.com": {
        "name": "SiliconValley.com",
        "url": "www.siliconvalley.com",
        "language": 2,
        "rulers": set(["http://www.siliconvalley.com/news/",
                       "http://www.siliconvalley.com/blogs-op-ed/",
                       "http://www.siliconvalley.com/slide-shows/",
                       "http://www.siliconvalley.com/reviews/"])
    },
    "crn.com": {
        "name": "crn",
        "url": "www.crn.com",
        "language": 2,
        "rulers": set(["http://www.crn.com/story/",
                       "http://www.crn.com/rt_story/",
                       "http://www.crn.com/rt/"])
    },
    "crnbuzz.com": {
        "name": "crnbuzz",
        "url": "www.crnbuzz.com",
        "language": 2,
        "rulers": set(["http://www.crnbuzz.com/"])
    },
    "i4u.com": {
        "name": "14U",
        "url": "www.i4u.com",
        "language": 2,
        "rulers": set(["http://www.i4u.com/"])
    },
    "technewsworld.com": {
        "name": "TECHNEWSWORLD",
        "url": "www.technewsworld.com",
        "language": 2,
        "rulers": set(["http://www.technewsworld.com/story/"])
    },
    "ecommercetimes.com": {
        "name": "ecommercetimes",
        "url": "www.ecommercetimes.com",
        "language": 2,
        "rulers": set(["http://www.ecommercetimes.com/story/"])
    },
    "macnewsworld.com": {
        "name": "macnewsworld",
        "url": "www.macnewsworld.com",
        "language": 2,
        "rulers": set(["http://www.macnewsworld.com/story/"])
    },
    "arnnet.com.au": {
        "name": "ARN",
        "url": "www.arnnet.com.au",
        "language": 2,
        "rulers": set(["http://www.arnnet.com.au/article/"])
    },
    "cfoworld.com": {
        "name": "CFOworld",
        "url": "www.cfoworld.com",
        "language": 2,
        "rulers": set(["http://www.cfoworld.com/strategic-finance/",
                       "http://www.cfoworld.com/accounting/",
                       "http://www.cfoworld.com/operations/",
                       "http://www.cfoworld.com/technology/",
                       "http://www.cfoworld.com/human-capital/"])
    },
    "cfoworld.co.uk": {
        "name": "CFO World",
        "url": "www.cfoworld.co.uk",
        "language": 2,
        "rulers": set(["http://www.cfoworld.co.uk/news/",
                       "http://www.cfoworld.co.uk/in-depth/",
                       "http://www.cfoworld.co.uk/cfo-interviews/",
                       "http://blogs.cfoworld.co.uk/"])
    },
    "cfoworld.com.au": {
        "name": "CFO World",
        "url": "www.cfoworld.com.au",
        "language": 2,
        "rulers": set(["http://www.cfoworld.com.au/article/",
                       "http://www.cfoworld.com.au/blog/",
                       "http://www.cfoworld.com.au/mediareleases/"])
    },
    "cio.com.au": {
        "name": "CIO",
        "url": "www.cio.com.au",
        "language": 2,
        "rulers": set(["http://www.cio.com.au/article/"])
    },
    "cio.in": {
        "name": "CIO",
        "url": "www.cio.in",
        "language": 2,
        "rulers": set(["http://www.cio.in/news/",
                       "http://www.cio.in/case-study/",
                       "http://www.cio.in/opinions/",
                       "http://www.cio.in/slideshow/",
                       "http://www.cio.in/article/",
                       "http://www.cio.in/ceo-interviews/",
                       "http://www.cio.in/cio-interview/"])
    },
    "cio.co.uk": {
        "name": "CIO",
        "url": "www.cio.co.uk",
        "language": 2,
        "rulers": set(["http://www.cio.co.uk/news/",
                       "http://www.cio.co.uk/slideshow/",
                       "http://www.cio.co.uk/profile/",
                       "http://www.cio.co.uk/cio100/",
                       "http://www.cio.co.uk/webcasts/",
                       "http://www.cio.co.uk/blogs/",
                       "http://www.cio.co.uk/insight/"])
    },
    "cio.com": {
        "name": "CIO",
        "url": "www.cio.com",
        "language": 2,
        "rulers": set(["http://www.cio.com/article/",
                       "http://www.cio.com/slideshow/",
                       "http://blogs.cio.com/"])
    },
    "citeworld.com": {
        "name": "CITEWORLD",
        "url": "www.citeworld.com",
        "language": 2,
        "rulers": set(["http://www.citeworld.com/tablets/",
                       "http://www.citeworld.com/consumerization/",
                       "http://www.citeworld.com/mobile/",
                       "http://www.citeworld.com/cloud/",
                       "http://www.citeworld.com/business/",
                       "http://www.citeworld.com/development/",
                       "http://www.citeworld.com/security/",
                       "http://www.citeworld.com/social/",
                       "http://www.citeworld.com/news/",
                       "http://www.citeworld.com/slideshow/"])
    },
    "cso.com.au": {
        "name": "cso",
        "url": "www.cso.com.au",
        "language": 2,
        "rulers": set(["http://www.cso.com.au/article/",
                       "http://www.cso.com.au/mediareleases/",
                       "http://www.cso.com.au/slideshow/",
                       "http://www.cso.com.au/blog/"])
    },
    "csoonline.com": {
        "name": "CSO",
        "url": "www.csoonline.com",
        "language": 2,
        "rulers": set(["http://www.csoonline.com/article/",
                       "http://blogs.csoonline.com/",
                       "http://www.csoonline.com/security/"])
    },
    "cw.com.hk": {
        "name": "COMPUTER WORLD",
        "url": "cw.com.hk",
        "language": 2,
        "rulers": set(["http://cw.com.hk/news/",
                       "http://cw.com.hk/features/",
                       "http://cw.com.hk/blog/",
                       "http://cw.com.hk/opinion/",
                       "http://cw.com.hk/events/"])
    },
    "computerworld.in": {
        "name": "COMPUTER WORLD",
        "url": "www.computerworld.in",
        "language": 2,
        "rulers": set(["http://www.computerworld.in/news/",
                       "http://www.computerworld.in/slideshow/",
                       "http://www.computerworld.in/opinion/",
                       "http://www.computerworld.in/interview/",
                       "http://www.computerworld.in/feature/",
                       "http://www.computerworld.in/case-study/",
                       "http://www.computerworld.in/how-to/",
                       "http://www.computerworld.in/compilations/"])
    },
    "computerworld.com.sg": {
        "name": "COMPUTER WORLD",
        "url": "www.computerworld.com.sg",
        "language": 2,
        "rulers": set(["http://www.computerworld.com.sg/resource/",
                       "http://www.computerworld.com.sg/tech/",
                       "http://www.computerworld.com.sg/mgmt/",
                       "http://www.computerworld.com.sg/blogs/"])
    },
    "computerworlduk.com": {
        "name": "COMPUTER WORLD",
        "url": "www.computerworlduk.com",
        "language": 2,
        "rulers": set(["http://www.computerworlduk.com/news/",
                       "http://www.computerworlduk.com/in-depth/",
                       "http://www.computerworlduk.com/webcasts/",
                       "http://www.computerworlduk.com/solution-centre/",
                       "http://www.computerworlduk.com/business-it-hub/",
                       "http://blogs.computerworlduk.com/"])
    },
    "computerworld.com": {
        "name": "COMPUTER WORLD",
        "url": "www.computerworld.com",
        "language": 2,
        "rulers": set(["http://www.computerworld.com/s/article/",
                       "http://blogs.computerworld.com/"])
    },
    "idc.com": {
        "name": "IDC",
        "url": "www.idc.com",
        "language": 2,
        "rulers": set(["http://www.idc.com/"])
    },
    "idgconnect.com": {
        "name": "IDG CONNECT",
        "url": "www.idgconnect.com",
        "language": 2,
        "rulers": set(["http://www.idgconnect.com/blogabstract/",
                       "http://www.idgconnect.com/abstract/"])
    },
    "infoworld.com": {
        "name": "Info World",
        "url": "www.infoworld.com",
        "language": 2,
        "rulers": set(["http://www.infoworld.com/t",
                       "http://www.infoworld.com/node/",
                       "http://www.infoworld.com/d/"])
    },
    "itworldcanada.com": {
        "name": "IT World",
        "url": "www.itworldcanada.com",
        "language": 2,
        "rulers": set(["http://www.itworldcanada.com/news/",
                       "http://www.itworldcanada.com/blogs/"])
    },
    "itworld.com": {
        "name": "IT World",
        "url": "www.itworld.com",
        "language": 2,
        "rulers": set(["http://www.itworld.com/"])
    },
    "techworld.com.au": {
        "name": "TECH WORLD",
        "url": "www.techworld.com.au",
        "language": 2,
        "rulers": set(["http://www.techworld.com.au/article/"])
    },
    "techworld.com": {
        "name": "TECH WORLD",
        "url": "www.techworld.com",
        "language": 2,
        "rulers": set(["http://news.techworld.com/",
                       "http://features.techworld.com/",
                       "http://blogs.techworld.com/",
                       "http://howto.techworld.com/"])
    },
    "macworld.com.au": {
        "name": "Mac world",
        "url": "www.macworld.com.au",
        "language": 2,
        "rulers": set(["http://www.macworld.com.au/news/",
                       "http://www.macworld.com.au/features/",
                       "http://www.macworld.com.au/reviews/",
                       "http://www.macworld.com/help/",
                       "http://www.macworld.com/blogs/",
                       "http://www.macworld.com/press/"])
    },
    "macworld.co.uk": {
        "name": "Mac world",
        "url": "www.macworld.co.uk",
        "language": 2,
        "rulers": set(["http://www.macworld.co.uk/blogs/",
                       "http://www.macworld.co.uk/apple-business/",
                       "http://www.macworld.co.uk/macsoftware/",
                       "http://www.macworld.co.uk/digitallifestyle/",
                       "http://www.macworld.co.uk/newswire/",
                       "http://www.macworld.co.uk/mac/",
                       "http://www.macworld.co.uk/ipad-iphone/",
                       "http://www.macworld.co.uk/mac-creative/",
                       "http://www.macworld.co.uk/apple-education/"])
    },
    "macworld.com": {
        "name": "Mac world",
        "url": "www.macworld.com",
        "language": 2,
        "rulers": set(["http://www.macworld.com/article/"])
    },
    "networkworld.com": {
        "name": "networksasia",
        "url": "www.networkworld.com",
        "language": 2,
        "rulers": set(["http://www.networkworld.com/news/",
                       "http://www.networkworld.com//slideshow/",
                       "http://www.networkworld.com/community/",
                       "http://www.networkworld.com/reviews/",
                       "http://www.networkworld.com/supp/"])
    },
    "pcadvisor.co.uk": {
        "name": "PC ADVISOR",
        "url": "www.pcadvisor.co.uk",
        "language": 2,
        "rulers": set(["http://www.pcadvisor.co.uk/news/",
                       "http://www.pcadvisor.co.uk/reviews/",
                       "http://www.pcadvisor.co.uk/how-to/"])
    },
    "pcworld.com": {
        "name": "pcworld",
        "url": "www.pcworld.com",
        "language": 2,
        "rulers": set(["http://www.pcworld.com/article/"])
    },
    "techhive.com": {
        "name": "techhive",
        "url": "www.techhive.com",
        "language": 2,
        "rulers": set(["http://www.techhive.com/article/"])
    },
    "goodgearguide.com.au": {
        "name": "goodgearguide",
        "url": "www.goodgearguide.com.au",
        "language": 2,
        "rulers": set(["http://www.goodgearguide.com.au/review/",
                       "http://www.goodgearguide.com.au/article/",
                       "http://www.goodgearguide.com.au/slideshow/",
                       "http://www.goodgearguide.com.au//roundup/"])
    },
    "techadvisor.co.uk": {
        "name": "techadvisor",
        "url": "www.techadvisor.co.uk",
        "language": 2,
        "rulers": set(["http://www.techadvisor.co.uk/features/",
                       "http://www.techadvisor.co.uk/opinion/",
                       "http://www.techadvisor.co.uk/buying-advice/"])
    },
    "techradar.com": {
        "name": "TechRadar",
        "url": "www.techradar.com/",
        "language": 2,
        "rulers": set(["http://www.techradar.com/news/",
                       "http://www.techradar.com/reviews/",
                       "http://www.techradar.com/blog/"])
    },
    "digitaltrends.com": {
        "name": "DIGITAL TRENDS",
        "url": "www.digitaltrends.com",
        "language": 2,
        "rulers": set(["http://www.digitaltrends.com/mobile/",
                       "http://www.digitaltrends.com/computing/",
                       "http://www.digitaltrends.com/social-media/",
                       "http://www.digitaltrends.com/lifestyle/",
                       "http://www.digitaltrends.com/gaming/",
                       "http://www.digitaltrends.com/guides/",
                       "http://www.digitaltrends.com/movies/",
                       "http://www.digitaltrends.com/gadgets/",
                       "http://www.digitaltrends.com/music/",
                       "http://www.digitaltrends.com/photography/",
                       "http://www.digitaltrends.com/cars/",
                       "http://www.digitaltrends.com/photogalleries/",
                       "http://www.digitaltrends.com/cool-tech/",
                       "http://www.digitaltrends.com/international/",
                       "http://www.digitaltrends.com/web/",
                       "http://www.digitaltrends.com/home-theater/"])
    },
    "itsecurity.com": {
        "name": "IT Security",
        "url": "www.itsecurity.com",
        "language": 2,
        "rulers": set(["http://www.itsecurity.com/features/",
                       "http://www.itsecurity.com/news/"])
    },
    "theglobeandmail.com": {
        "name": "GLOBEtechnology.com",
        "url": "www.theglobeandmail.com",
        "language": 2,
        "rulers": set(["http://www.theglobeandmail.com/news/",
                       "http://www.theglobeandmail.com/commentary/",
                       "http://www.theglobeandmail.com/report-on-business/",
                       "http://www.theglobeandmail.com/globe-investor/",
                       "http://www.theglobeandmail.com/globe-drive/",
                       "http://www.theglobeandmail.com/life/",
                       "http://www.theglobeandmail.com/arts/",
                       "http://www.theglobeandmail.com/sports/",
                       "http://www.theglobeandmail.com/technology/"])
    },
    "hpcwire.com": {
        "name": "HPCwire",
        "url": "www.hpcwire.com",
        "language": 2,
        "rulers": set(["http://www.hpcwire.com/hpcwire/"])
    },
    "hyperorg.com": {
        "name": "JOHO",
        "url": "www.hyperorg.com",
        "language": 2,
        "rulers": set(["http://www.hyperorg.com/backissues/"])
    },
    "geeknews.net": {
        "name": "Geeknews",
        "url": "www.geeknews.net",
        "language": 2,
        "rulers": set(["http://www.geeknews.net/"])
    },
    "techreport.com": {
        "name": "Tech Report",
        "url": "techreport.com",
        "language": 2,
        "rulers": set(["http://techreport.com/news/",
                       "http://techreport.com/review/",
                       "http://techreport.com/blog/"])
    },
    "tbtf.com": {
        "name": "Tasty Bits from the Technology Front (TBTF)",
        "url": "tbtf.com",
        "language": 2,
        "rulers": set(["http://tbtf.com/roving_reporter/",
                       "http://tbtf.com/unblinking/",
                       "http://tbtf.com/jaundiced/",
                       "http://tbtf.com/unpund/",
                       "http://tbtf.com/blog-archive/",
                       "http://tbtf.com/archive/"])
    },
    "futurelooks.com": {
        "name": "Futurelooks",
        "url": "www.futurelooks.com",
        "language": 2,
        "rulers": set(["http://www.futurelooks.com"])
    },
    "computerbytesman.com": {
        "name": "Computer Bytes Man",
        "url": "www.computerbytesman.com",
        "language": 2,
        "rulers": set(["http://www.computerbytesman.com/privacy/",
                       "http://www.computerbytesman.com/security/",
                       "http://www.computerbytesman.com/copyprotect/",
                       "http://www.computerbytesman.com/biometrics/",
                       "http://www.computerbytesman.com/anthrax/"])
    },
    "webtechgeek.com": {
        "name": "WebTechGeek.com",
        "url": "www.webtechgeek.com",
        "language": 2,
        "rulers": set(["http://www.webtechgeek.com/wp/"])
    },
    "alterslash.org": {
        "name": "AlterSlash",
        "url": "www.alterslash.org",
        "language": 2,
        "rulers": set(["http://www.alterslash.org/"])
    },
    "techjunkeez.com": {
        "name": "Tech Junkeez",
        "url": "www.techjunkeez.com",
        "language": 2,
        "rulers": set(["http://www.techjunkeez.com/old/archive/",
                       "http://www.techjunkeez.com/news/"])
    },
    "pc1news.com": {
        "name": "PC1News",
        "url": "www.pc1news.com",
        "language": 2,
        "rulers": set(["http://www.pc1news.com/news/"])
    },
    "oreilly.com": {
        "name": "O'Reilly Network Weblogs",
        "url": "radar.oreilly.com",
        "language": 2,
        "rulers": set(["http://radar.oreilly.com/"])
    },
    "eweek.com": {
        "name": "eWeek",
        "url": "www.eweek.com",
        "language": 2,
        "rulers": set(["http://www.eweek.com/storage/",
                       "http://www.eweek.com/security/",
                       "http://www.eweek.com/cloud/",
                       "http://www.eweek.com/pc-hardware/",
                       "http://www.eweek.com/networking/",
                       "http://www.eweek.com/small-business/",
                       "http://www.eweek.com/mobile/",
                       "http://www.eweek.com/it-management/",
                       "http://www.eweek.com/servers/",
                       "http://www.eweek.com/blogs/",
                       "http://www.eweek.com/developer/",
                       "http://www.eweek.com/enterprise-apps/",
                       "http://www.eweek.com/innovation/",
                       "http://www.eweek.com/networking/",
                       "http://www.eweek.com/android/",
                       "http://www.eweek.com/apple/",
                       "http://www.eweek.com/pc-hardware/",
                       "http://www.eweek.com/virtualization/",
                       "http://www.eweek.com/database/"])
    },
    "informationweek.com": {
        "name": "informationweek",
        "url": "www.informationweek.com",
        "language": 2,
        "rulers": set(["http://www.informationweek.com/byte/",
                       "http://www.informationweek.com/software/",
                       "http://www.informationweek.com/security/",
                       "http://www.informationweek.com/cloud/",
                       "http://www.informationweek.com/mobility/",
                       "http://www.informationweek.com/social-business/",
                       "http://www.informationweek.com/big-data/",
                       "http://www.informationweek.com/windows/",
                       "http://www.informationweek.com/global-cio/",
                       "http://www.informationweek.com/goverment/",
                       "http://www.informationweek.com/healthcare/",
                       "http://www.informationweek.com/education/",
                       "http://www.informationweek.com/financial/",
                       "http://www.informationweek.com/smb/",
                       "http://www.informationweek.com/hardware/",
                       "http://www.informationweek.com/internet/",
                       "http://www.informationweek.com/news/"])
    },
    "fcw.com": {
        "name": "FCW",
        "url": "fcw.com",
        "language": 2,
        "rulers": set(["http://fcw.com/articles/"])
    },
    "cbronline.com": {
        "name": "CBR",
        "url": "www.cbronline.com",
        "language": 2,
        "rulers": set(["http://www.cbronline.com/news/",
                       "http://www.cbronline.com/blogs/"])
    },
    "reviews.com": {
        "name": "Computing Reviews",
        "url": "www.reviews.com",
        "language": 2,
        "rulers": set(["http://www.reviews.com/"])
    },
    "electricnews.net": {
        "name": "ENN",
        "url": "www.electricnews.net",
        "language": 2,
        "rulers": set(["http://www.electronics.net"])
    },
    "esj.com": {
        "name": "Enterprise Systems",
        "url": "esj.com",
        "language": 2,
        "rulers": set(["http://www.esj.com/articles/"])
    },
    "computer.org": {
        "name": "Computer Magazine",
        "url": "www.computer.org",
        "language": 2,
        "rulers": set(["http://www.computer.org/portal/site/computer/"])
    },
    "computoredge.com": {
        "name": "ComputorEdge Online",
        "url": "www.computoredge.com",
        "language": 2,
        "rulers": set(["http://www.computoredge.com/"])
    },
    "chipanalyst.com": {
        "name": "MicroDesign Resources",
        "url": "www.chipanalyst.com",
        "language": 2,
        "rulers": set(["http://www.chipanalyst.com/"])
    },
    "reviewboard.com": {
        "name": "Reviewboard Magazine",
        "url": "www.reviewboard.com",
        "language": 2,
        "rulers": set(["http://www.reviewboard.com/"])
    },
    "streport.com": {
        "name": "STReport International Online Magazine",
        "url": "www.streport.com",
        "language": 2,
        "rulers": set(["http://www.streport.com/files/"])
    },
    "thetechmag.com": {
        "name": "The Tech Bolg",
        "url": "www.thetechmag.com",
        "language": 2,
        "rulers": set(["http://www.thetechmag.com"])
    },
    "ymmv.com": {
        "name": "Your Mileage May Vary (YMMV)",
        "url": "www.ymmv.com",
        "language": 2,
        "rulers": set(["http://www.ymmv.com/goodreads/"])
    },
    "ceocio.com.cn": {
        "name": "经理世界网",
        "url": "www.ceocio.com.cn",
        "language": 1,
        "rulers": set(["http://www.ceocio.com.cn/it/",
                       "http://www.ceocio.com.cn/cio/",
                       "http://www.ceocio.com.cn/net/",
                       "http://www.ceocio.com.cn/news/",
                       "http://www.ceocio.com.cn/finance/",
                       "http://www.ceocio.com.cn/property/",
                       "http://www.ceocio.com.cn/tech/",
                       "http://www.ceocio.com.cn/car/",
                       "http://www.ceocio.com.cn/manage/",
                       "http://www.ceocio.com.cn/views/",
                       "http://www.ceocio.com.cn/life/",
                       "http://www.ceocio.com.cn/meeting/",
                       "http://www.ceocio.com.cn/magazine/it/"])
    },
    "cnw.com.cn": {
        "name": "网界",
        "url": "www.cnw.com.cn",
        "language": 1,
        "rulers": set(["http://www.cnw.com.cn/news-international/",
                       "http://www.cnw.com.cn/news-china/",
                       "http://blog.cnw.com.cn",
                       "http://ndc.cnw.com.cn",
                       "http://www.cnw.com.cn/bigdata-orginal/",
                       "http://www.cnw.com.cn/bigdata-newinformation/",
                       "http://www.cnw.com.cn/bigdata-column/",
                       "http://www.cnw.com.cn/network-carrier-ethernets/",
                       "http://www.cnw.com.cn/network-switch/",
                       "http://www.cnw.com.cn/network-router/",
                       "http://www.cnw.com.cn/cloud-original/",
                       "http://www.cnw.com.cn/cloud-computing/",
                       "http://www.cnw.com.cn/cloud-specialist/",
                       "http://www.cnw.com.cn/server-x86/",
                       "http://www.cnw.com.cn/server-mainframe/",
                       "http://www.cnw.com.cn/server-os/",
                       "http://www.cnw.com.cn/storage-san-nas/",
                       "http://www.cnw.com.cn/storage-Management/",
                       "http://www.cnw.com.cn/storage-Technology/",
                       "http://www.cnw.com.cn/security-10g-firewall/",
                       "http://www.cnw.com.cn/security-next-firewall/",
                       "http://www.cnw.com.cn/security-utm/",
                       "http://www.cnw.com.cn/software-bi/",
                       "http://www.cnw.com.cn/software-net-management/",
                       "http://www.cnw.com.cn/software-database/",
                       "http://www.cnw.com.cn/industries-cio/",
                       "http://www.cnw.com.cn/industries-event/",
                       "http://www.cnw.com.cn/zhuanti/",
                       "http://www.cnw.com.cn/test-news/",
                       "http://www.cnw.com.cn/test-report/",
                       "http://www.cnw.com.cn/edu-web/",
                       "http://www.cnw.com.cn/edu-dev/",
                       "http://mobile.cnw.com.cn/",
                       "http://www.cnw.com.cn/weekly/",
                       "http://dcw.cnw.com.cn"])
    }
}
