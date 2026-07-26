import random
from insert_data import insert_product_data

# Constants
PRODUCT_CATEGORIES={
"Electronics": 
{"Laptop":
{
    "HP":["Pavilion", "Envy", "Spectre", "Omen","EliteBook", "ProBook", "ZBook"], 
            "Dell": ["XPS", "Inspiron", "G3", "G5", "Optiplex", "Latitude", "Vostro"], 
    "Lenovo": ["ThinkPad", "Yoga", "Legion","ThinkCentre","Ideapad","ThinkBook","Legion","IdeaCentre","YogaBook","Flex","Duet","Chromebook"], 
    "Apple": ["MacBook Air", "MacBook Pro","Mac mini","iMac",],
    "ASUS": ["VivoBook", "ZenBook", "Transformer","TUF","ROG"],
    "Microsoft": ["Surface Laptop", "Surface Pro","Surface Duo",],
    "Acer": ["Aspire", "Predator", "Swift","Aspire", "Predator"],
    "Razer": ["Blade", "Stealth", "Core","Blade Stealth"],
    "MSI": ["GS", "GE", "GT","GP","GF","Prestige","Creator","Modern","Summit","Katana","Raider"],
} ,
"Smartphone":
{
    "Samsung": ["Galaxy S", "Galaxy Note", "Galaxy A", "Galaxy M", "Galaxy Z","Galaxy F", "Galaxy J", "Galaxy C", "Galaxy On"],
"Apple": ["iPhone 13", "iPhone 13 Pro", "iPhone 13 mini", "iPhone 13 Air","iPhone 12", "iPhone 12 Pro", "iPhone 12 mini", "iPhone 12 Air","iPhone 11", "iPhone 11 Pro", "iPhone 11 mini", "iPhone 11 Air"], 
"OnePlus": ["OnePlus 9", "OnePlus 9 Pro", "OnePlus 9R","OnePlus 8T", "OnePlus 8 Pro", "OnePlus 8", "OnePlus Nord", "OnePlus Nord N10", "OnePlus Nord N100"],
"Google": ["Pixel 6", "Pixel 6 Pro", "Pixel 6 XL","Pixel 5", "Pixel 5a", "Pixel 4a", "Pixel 4", "Pixel 3a", "Pixel 3"],
"Xiaomi": ["Mi 11", "Mi 11 Ultra", "Mi 11 Pro","Mi 10", "Mi 10 Pro", "Mi 10T", "Mi 10T Pro", "Redmi Note 10", "Redmi Note 10 Pro", "Redmi Note 9", "Redmi Note 9 Pro"],
"Oppo": ["Find X3", "Find X3 Pro", "Find X3 Neo","Find X3 Lite", "Reno 6", "Reno 6 Pro", "Reno 6 Pro+", "Reno 5", "Reno 5 Pro", "Reno 5 Pro+", "A94", "A74", "A54"],
"Realme": ["Realme GT", "Realme 8", "Realme 8 Pro","Realme 7", "Realme 7 Pro", "Realme Narzo 30", "Realme Narzo 30 Pro", "Realme Narzo 30A"],
"Vivo": ["Vivo Y73", "Vivo Y77", "Vivo Y11","Vivo Y20","Vivo Y21", "Vivo Y31", "Vivo Y51", "Vivo Y53", "Vivo Y55", "Vivo Y70", "Vivo Y75"],
"Motorola": ["Moto G Power", "Moto G Stylus", "Moto G Play","Motorola Edge", "Motorola Edge+", "Motorola One 5G", "Motorola One Fusion+", "Motorola One Hyper", "Motorola One Action", "Motorola One Vision"],
"Nokia": ["Nokia 8.3", "Nokia 5.4", "Nokia 3.4","Nokia 2.4", "Nokia 1.4", "Nokia 7.2", "Nokia 6.2", "Nokia 5.3", "Nokia 4.2", "Nokia 3.2"],
},
"Tablet": 
{
"Apple": ["iPad Pro", "iPad Air", "iPad Mini", "iPad"],
"Samsung": ["Galaxy Tab S7", "Galaxy Tab S6", "Galaxy Tab A7", "Galaxy Tab Active3"],
"Lenovo": ["Tab P11", "Tab M10", "Tab E10", "Yoga Smart Tab"], 
"Microsoft": ["Surface Pro 7", "Surface Go 2", "Surface Book 3", "Surface Laptop Go"], 
"Huawei": ["MatePad Pro", "MatePad 10.4", "MediaPad M5 Lite", "MediaPad T5"], 
"Amazon": ["Fire HD 10", "Fire HD 8", "Fire 7", "Fire Kids Edition"], 
"ASUS": ["ZenPad 3S 10", "ZenPad 8.0", "ZenPad C 7.0", "Transformer Mini T102HA"], 
"Xiaomi": ["Mi Pad 5", "Mi Pad 4", "Mi Pad 3", "Mi Pad 2"],
"Acer": ["Iconia One 10", "Iconia Tab 10", "Iconia Tab 8", "Iconia Tab 7"],
"LG": ["G Pad 5", "G Pad 4", "G Pad 3", "G Pad 2"]
},
"Headphones": 
{
"Sony": ["WH-1000XM4", "WF-1000XM3", "MDR-7506", "MDR-XB950N1", "MDR-ZX110NC"],
"Bose": ["QuietComfort 35 II", "SoundLink Revolve+", "Bose 700"],
"Sennheiser": ["HD 206", "HD 25-1", "HD 560S"],
"JBL": ["TUNE 125TWS", "GO 2", "E50BT"],
"Beats": ["Studio Buds", "Powerbeats Pro", "Solo Pro"],
"Audio-Technica": ["ATH-M40x", "ATH-M50x", "ATH-AD2000X"]
},
"Smartwatch":
{
    "Apple": [
        "Watch SE",
        "Watch Series 9",
        "Watch Series 10",
        "Watch Ultra",
        "Watch Ultra 2"
    ],

    "Samsung": [
        "Galaxy Watch 6",
        "Galaxy Watch 6 Classic",
        "Galaxy Watch 7",
        "Galaxy Watch Ultra",
        "Galaxy Watch FE"
    ],

    "Garmin": [
        "Forerunner 265",
        "Forerunner 965",
        "Fenix 8",
        "Venu 3",
        "Instinct 2"
    ],

    "Fitbit": [
        "Sense 2",
        "Versa 4",
        "Charge 6",
        "Inspire 3",
        "Ace LTE"
    ],

    "Fossil": [
        "Gen 6 Wellness",
        "Gen 6 Venture",
        "Hybrid HR",
        "Collider HR",
        "Machine Gen 6"
    ],

    "Huawei": [
        "Watch GT 5",
        "Watch GT 4",
        "Watch Fit 3",
        "Watch Ultimate",
        "Watch D2"
    ]
},

"Camera":
{
    "Canon": [
        "EOS R50",
        "EOS R8",
        "EOS R6 Mark II",
        "EOS R10",
        "PowerShot G7 X"
    ],

    "Nikon": [
        "Z30",
        "Z50",
        "Z6 II",
        "Z8",
        "D7500"
    ],

    "Sony": [
        "Alpha A6400",
        "Alpha A6700",
        "Alpha A7 IV",
        "Alpha A7C II",
        "ZV-E10"
    ],

    "Fujifilm": [
        "X-T30 II",
        "X-S20",
        "X-T5",
        "X100VI",
        "GFX100S"
    ],

    "Olympus": [
        "OM-D E-M10 IV",
        "OM-D E-M5 III",
        "PEN E-P7",
        "Tough TG-7",
        "OM-1"
    ],

    "Panasonic": [
        "Lumix G85",
        "Lumix GH7",
        "Lumix S5 II",
        "Lumix G100",
        "Lumix TZ99"
    ],

    "Leica": [
        "Q3",
        "M11",
        "SL3",
        "D-Lux 8",
        "CL"
    ]
},

"Television":
{
    "Samsung":[
        "Crystal UHD DU8000",
        "QLED Q70D",
        "Neo QLED QN90D",
        "The Frame",
        "OLED S90D"
    ],

    "LG":[
        "UQ7500",
        "QNED85",
        "OLED C4",
        "OLED G4",
        "NanoCell NANO80"
    ],

    "Sony":[
        "Bravia X80L",
        "Bravia X90L",
        "Bravia 7",
        "Bravia 8",
        "A95L OLED"
    ],

    "Panasonic":[
        "MX800",
        "MX950",
        "MZ980 OLED",
        "MZ1500 OLED",
        "LX650"
    ],

    "TCL":[
        "P755",
        "C655",
        "C755",
        "QM8",
        "Q6"
    ],

    "Vizio":[
        "V-Series",
        "M-Series Quantum",
        "P-Series Quantum",
        "D-Series",
        "OLED H1"
    ],

    "Hisense":[
        "A6 Series",
        "U6N",
        "U7N",
        "U8N",
        "Canvas TV"
    ]
},

"Monitor":
{
    "Dell":[
        "UltraSharp U2723QE",
        "P2422H",
        "S2721QS",
        "Alienware AW2725DF",
        "SE2422H"
    ],

    "ASUS":[
        "TUF VG27AQ",
        "ROG Swift PG27AQDM",
        "ProArt PA278CV",
        "ZenScreen MB16AC",
        "VA24E"
    ],

    "Acer":[
        "Nitro XV272U",
        "Predator X34",
        "Aspire CB272",
        "KA242Y",
        "XV320QU"
    ],

    "LG":[
        "UltraGear 27GP850",
        "UltraFine 5K",
        "MyView Smart Monitor",
        "UltraWide 34WN80C",
        "27UP850"
    ],

    "Samsung":[
        "Odyssey G5",
        "Odyssey G7",
        "Odyssey OLED G8",
        "ViewFinity S8",
        "Smart Monitor M8"
    ],

    "BenQ":[
        "GW2780",
        "PD2705U",
        "EX2710Q",
        "EW3270U",
        "ZOWIE XL2546K"
    ],

    "ViewSonic":[
        "VX2758",
        "VP2768",
        "VG2448",
        "Elite XG270",
        "VA2456"
    ]
},

"Printer":
{
    "HP":[
        "LaserJet Pro MFP 4101",
        "DeskJet 4155e",
        "OfficeJet Pro 9125e",
        "Smart Tank 7602",
        "Color LaserJet Pro 3201"
    ],

    "Canon":[
        "PIXMA G3770",
        "PIXMA TS7720",
        "MAXIFY GX6021",
        "imageCLASS MF455dw",
        "SELPHY CP1500"
    ],

    "Epson":[
        "EcoTank L3250",
        "EcoTank L6270",
        "WorkForce Pro WF-4830",
        "Expression XP-4200",
        "SureColor P700"
    ],

    "Brother":[
        "HL-L2460DW",
        "DCP-L2541DW",
        "MFC-L3760CDW",
        "HL-L3270CDW",
        "MFC-J4335DW"
    ],

    "Lexmark":[
        "MB3442adw",
        "MC3326adwe",
        "CS431dw",
        "CX431adw",
        "MS431dw"
    ],

    "Samsung":[
        "Xpress M2020",
        "Xpress SL-M2070",
        "ProXpress M3820",
        "MultiXpress X4300",
        "Xpress C430W"
    ],

    "Xerox":[
        "B230",
        "B315",
        "C310",
        "VersaLink C415",
        "WorkCentre 6515"
    ]
},

"Router":
{
    "TP-Link":[
        "Archer AX55",
        "Archer AX73",
        "Archer BE550",
        "Deco X50",
        "Deco XE75"
    ],

    "Netgear":[
        "Nighthawk AX5400",
        "Nighthawk RS700",
        "Orbi RBK863",
        "RAX50",
        "XR1000"
    ],

    "ASUS":[
        "RT-AX88U Pro",
        "RT-AX86U",
        "ROG Rapture GT-AX6000",
        "ZenWiFi XT9",
        "RT-BE88U"
    ],

    "D-Link":[
        "DIR-X5460",
        "DIR-2150",
        "Eagle Pro AI M32",
        "Covr X1862",
        "DIR-3040"
    ],

    "Linksys":[
        "Hydra Pro 6",
        "Velop MX4200",
        "Atlas Max 6E",
        "MR7350",
        "EA8300"
    ],

    "Google":[
        "Nest Wifi",
        "Nest Wifi Pro",
        "Google Wifi",
        "Nest Router",
        "Wifi Pro 6E"
    ],

    "Ubiquiti":[
        "UniFi Dream Router",
        "UniFi Express",
        "UniFi Cloud Gateway Max",
        "UniFi Dream Machine Pro",
        "AmpliFi Alien"
    ]
}
},
 "Home Appliances": {
    "Refrigerator": {
        "LG": [
            "InstaView Door-in-Door",
            "Smart Inverter",
            "French Door Max",
            "Side-by-Side 635L",
            "Bottom Freezer Plus"
        ],
        "Samsung": [
            "Family Hub",
            "Bespoke Flex",
            "Twin Cooling Plus",
            "French Door RF28",
            "Side-by-Side RS76"
        ],
        "Whirlpool": [
            "WRS325SDHZ",
            "WRX735SDHZ",
            "Top Freezer 570L",
            "Double Door FreshFlow",
            "Side-by-Side Premium"
        ],
        "Bosch": [
            "Serie 4 Frost Free",
            "Serie 6 VitaFresh",
            "Serie 8 French Door",
            "Bottom Mount XL",
            "MultiAirflow Pro"
        ],
        "GE": [
            "Profile Smart",
            "French Door 27.9",
            "Side-by-Side GSS25",
            "Top Freezer GTE18",
            "Bottom Freezer GBE21"
        ],
        "Frigidaire": [
            "Gallery Series",
            "Professional 4-Door",
            "Top Freezer FFHT",
            "Side-by-Side FRSS",
            "French Door FRFG"
        ],
        "KitchenAid": [
            "KRFC300ESS",
            "KRFF507HPS",
            "Side-by-Side Architect",
            "Counter Depth Plus",
            "French Door Premium"
        ]
    },

    "Washing Machine": {
        "LG": [
            "TurboWash 360",
            "AI Direct Drive",
            "TwinWash",
            "Front Load 9kg",
            "Top Load Smart"
        ],
        "Samsung": [
            "EcoBubble",
            "Bespoke AI",
            "AddWash",
            "QuickDrive",
            "Front Load WW90"
        ],
        "Whirlpool": [
            "FreshCare+",
            "Supreme Care",
            "Top Load 360",
            "Front Load Elite",
            "PowerClean Pro"
        ],
        "Bosch": [
            "Serie 4",
            "Serie 6",
            "Serie 8",
            "EcoSilence Drive",
            "Home Connect"
        ],
        "Maytag": [
            "MVW4505",
            "Pet Pro",
            "Commercial Grade",
            "Smart Top Load",
            "Front Load Max"
        ],
        "GE": [
            "UltraFresh",
            "Profile Smart",
            "Front Load GFW",
            "Top Load GTW",
            "Ultra Capacity"
        ]
    },

    "Microwave": {
        "Panasonic": [
            "Genius Sensor",
            "NN-SN68",
            "Cyclonic Wave",
            "Inverter Turbo",
            "HomeChef 4-in-1"
        ],
        "Samsung": [
            "HotBlast",
            "Solo MS23",
            "Grill MG23",
            "Slim Fry",
            "PowerGrill Duo"
        ],
        "LG": [
            "NeoChef",
            "Smart Inverter",
            "EasyClean",
            "Grill Convection",
            "Solo MS204"
        ],
        "Sharp": [
            "Carousel",
            "R-21LCFS",
            "Sensor Cook",
            "Convection Elite",
            "Compact Solo"
        ],
        "Toshiba": [
            "EM131A5C",
            "Smart Sensor",
            "Origin Inverter",
            "Master Series",
            "Countertop Pro"
        ],
        "Breville": [
            "Smooth Wave",
            "Quick Touch",
            "Combi Wave 3-in-1",
            "Compact Wave",
            "Smart Oven Wave"
        ]
    },

    "Air Conditioner": {
        "Daikin": [
            "FTKM Series",
            "Emura",
            "Streamer Inverter",
            "SkyAir",
            "Premium Split AC"
        ],
        "LG": [
            "Dual Inverter",
            "AI Convertible",
            "ArtCool",
            "Window Smart",
            "Split Deluxe"
        ],
        "Samsung": [
            "WindFree",
            "Bespoke AI",
            "Digital Inverter",
            "Premium Split",
            "AR18 Series"
        ],
        "Panasonic": [
            "Nanoe X",
            "Inverter Deluxe",
            "Sky Series",
            "Eco Tough",
            "CS/CU Premium"
        ],
        "Carrier": [
            "XPower Gold",
            "Optima Plus",
            "Durafresh",
            "FlexCool",
            "Superia NX"
        ]
    },

    "Vacuum Cleaner": {
        "Dyson": [
            "V8 Absolute",
            "V11 Torque Drive",
            "V15 Detect",
            "Gen5 Detect",
            "Ball Animal 3"
        ],
        "Shark": [
            "Navigator Lift-Away",
            "Vertex DuoClean",
            "Stratos Cordless",
            "Rocket Pet Pro",
            "PowerDetect"
        ],
        "Bissell": [
            "CrossWave",
            "CleanView",
            "Pet Hair Eraser",
            "PowerForce Helix",
            "SpinWave"
        ],
        "Hoover": [
            "ONEPWR Evolve",
            "WindTunnel 3",
            "MAXLife Elite",
            "SmartWash",
            "PowerDash Pet"
        ],
        "Miele": [
            "Complete C3",
            "Classic C1",
            "Blizzard CX1",
            "Triflex HX2",
            "Boost CX1"
        ]
    },

    "Dishwasher": {
        "Bosch": [
            "Serie 4",
            "Serie 6",
            "Serie 8",
            "Silence Plus",
            "Home Connect"
        ],
        "KitchenAid": [
            "KDPM604KPS",
            "KDTM404KPS",
            "PrintShield",
            "FreeFlex Rack",
            "Architect Series"
        ],
        "Whirlpool": [
            "WDF540PADM",
            "Top Control Pro",
            "Quiet Partner",
            "Eco Series",
            "PowerClean"
        ],
        "Samsung": [
            "StormWash",
            "Smart Linear Wash",
            "AutoRelease Dry",
            "Bespoke Dishwasher",
            "DW80 Series"
        ],
        "LG": [
            "QuadWash",
            "TrueSteam",
            "EasyRack Plus",
            "ThinQ Smart",
            "Inverter Direct Drive"
        ]
    },

    "Coffee Maker": {
        "Keurig": [
            "K-Classic",
            "K-Elite",
            "K-Supreme",
            "K-Duo",
            "K-Cafe"
        ],
        "Nespresso": [
            "Vertuo Pop",
            "Vertuo Next",
            "Essenza Mini",
            "Lattissima One",
            "Creatista Plus"
        ],
        "Breville": [
            "Barista Express",
            "Barista Pro",
            "Oracle Touch",
            "Bambino Plus",
            "Precision Brewer"
        ],
        "Cuisinart": [
            "DCC-3200",
            "PerfectTemp",
            "Grind & Brew",
            "Coffee Center",
            "Single Serve SS-10"
        ],
        "Hamilton Beach": [
            "FlexBrew",
            "BrewStation",
            "2-Way Brewer",
            "Programmable 12-Cup",
            "Elite Brew"
        ]
    }
},
"Fashion": {
    "T-Shirt": {
        "Nike": [
            "Sportswear Club",
            "Dri-FIT Legend",
            "Pro Compression",
            "Air Max Graphic",
            "Essential Logo Tee"
        ],
        "Adidas": [
            "Essentials Logo",
            "Own The Run",
            "AEROREADY Training",
            "Trefoil Classic",
            "3-Stripes Tee"
        ],
        "Puma": [
            "Essentials Logo",
            "Active Small Logo",
            "Power Graphic",
            "Better Essentials",
            "BMW Motorsport Tee"
        ],
        "Under Armour": [
            "Tech 2.0",
            "Sportstyle Logo",
            "Project Rock",
            "HeatGear Compression",
            "UA Rival Tee"
        ],
        "Reebok": [
            "Identity Logo",
            "Training Speedwick",
            "Classic Vector",
            "Workout Ready",
            "Graphic Series Tee"
        ]
    },

    "Jeans": {
        "Levi's": [
            "501 Original",
            "511 Slim",
            "512 Slim Taper",
            "505 Regular",
            "541 Athletic Fit"
        ],
        "Wrangler": [
            "Cowboy Cut",
            "Retro Slim",
            "Texas Stretch",
            "Five Star Premium",
            "Authentics Regular"
        ],
        "Lee": [
            "Extreme Motion",
            "Regular Fit",
            "Slim Straight",
            "Modern Series",
            "Relaxed Fit"
        ],
        "Diesel": [
            "D-Strukt",
            "Sleenker",
            "Thommer",
            "Larkee",
            "D-Amny"
        ],
        "True Religion": [
            "Ricky Straight",
            "Geno Slim",
            "Rocco Skinny",
            "Bobby Relaxed",
            "Billy Bootcut"
        ]
    },

    "Dress": {
        "Zara": [
            "Floral Midi",
            "Satin Slip",
            "Linen Shirt Dress",
            "Pleated Maxi",
            "Wrap Dress"
        ],
        "H&M": [
            "Ribbed Bodycon",
            "Floral Summer",
            "Shirt Dress",
            "Cotton Maxi",
            "Pleated Midi"
        ],
        "Forever 21": [
            "Smocked Mini",
            "Ruched Bodycon",
            "Floral Wrap",
            "Casual Tank Dress",
            "Tiered Midi"
        ],
        "Mango": [
            "Linen Blend",
            "Satin Elegance",
            "Pleated Midi",
            "Wrap Midi",
            "Printed Maxi"
        ],
        "ASOS": [
            "Design Satin Midi",
            "Curve Wrap Dress",
            "Lace Maxi",
            "Floral Tea Dress",
            "One Shoulder Midi"
        ]
    },

    "Sneakers": {
        "Nike": [
            "Air Force 1",
            "Air Max 270",
            "Air Max 90",
            "Revolution 7",
            "Pegasus 41"
        ],
        "Adidas": [
            "Ultraboost Light",
            "Superstar",
            "Stan Smith",
            "Gazelle",
            "Duramo SL"
        ],
        "Puma": [
            "RS-X",
            "Suede Classic",
            "Smash V2",
            "Velocity Nitro",
            "CA Pro"
        ],
        "Reebok": [
            "Classic Leather",
            "Nano X4",
            "Club C 85",
            "Zig Kinetica",
            "Floatride Energy"
        ],
        "New Balance": [
            "574 Core",
            "327",
            "550",
            "9060",
            "Fresh Foam 1080"
        ]
    },

    "Jacket": {
        "North Face": [
            "Nuptse Jacket",
            "Antora Rain",
            "Aconcagua 3",
            "Resolve Jacket",
            "ThermoBall Eco"
        ],
        "Columbia": [
            "Watertight II",
            "Powder Lite",
            "Bugaboo III",
            "Glennaker Lake",
            "Delta Ridge"
        ],
        "Patagonia": [
            "Nano Puff",
            "Better Sweater",
            "Torrentshell 3L",
            "Down Sweater",
            "R1 Air Full Zip"
        ],
        "Canada Goose": [
            "Langford Parka",
            "Expedition Parka",
            "MacMillan Parka",
            "Chateau Parka",
            "HyBridge Lite"
        ],
        "Arc'teryx": [
            "Atom Hoody",
            "Beta Jacket",
            "Cerium Hoody",
            "Gamma MX",
            "Sabre Jacket"
        ]
    },

    "Handbag": {
        "Michael Kors": [
            "Jet Set Tote",
            "Mercer Gallery",
            "Charlotte Tote",
            "Mae Shoulder Bag",
            "Bradshaw Satchel"
        ],
        "Coach": [
            "Tabby Shoulder Bag",
            "Willow Tote",
            "Charter Crossbody",
            "Rogue Bag",
            "Brooklyn Shoulder Bag"
        ],
        "Kate Spade": [
            "Knott Satchel",
            "Margaux Tote",
            "Sam Icon Bag",
            "Dakota Crossbody",
            "Morgan Shoulder Bag"
        ],
        "Fossil": [
            "Jolie Crossbody",
            "Sydney Satchel",
            "Rachel Tote",
            "Harwell Shoulder",
            "Kinley Crossbody"
        ],
        "Tory Burch": [
            "Ella Tote",
            "Perry Triple Compartment",
            "Kira Chevron",
            "Lee Radziwill",
            "Robinson Satchel"
        ]
    }
},
 "Books": {
    "Python Programming": {
        "O'Reilly Media": [
            "Learning Python",
            "Python Cookbook",
            "Fluent Python",
            "Python for Data Analysis",
            "Programming Python"
        ],

        "Packt Publishing": [
            "Python Journey",
            "Mastering Python",
            "Python Design Patterns",
            "Python Automation Cookbook",
            "Expert Python Programming"
        ],

        "No Starch Press": [
            "Automate the Boring Stuff with Python",
            "Python Crash Course",
            "Serious Python",
            "Black Hat Python",
            "Impractical Python Projects"
        ],

        "Apress": [
            "Beginning Python",
            "Pro Python",
            "Practical Python Projects",
            "Python for Developers",
            "Python Machine Learning by Example"
        ],

        "Manning Publications": [
            "Python in Action",
            "Python Workout",
            "Tiny Python Projects",
            "Grokking Algorithms with Python",
            "Practices of the Python Pro"
        ]
    },

    "Data Science": {
        "O'Reilly Media": [
            "Python for Data Analysis",
            "Hands-On Data Analysis",
            "Practical Statistics for Data Scientists",
            "Fundamentals of Data Engineering",
            "Data Science from Scratch"
        ],

        "Packt Publishing": [
            "Data Science with Python",
            "Python Data Cleaning Cookbook",
            "Data Visualization with Python",
            "Pandas Cookbook",
            "Applied Data Science"
        ],

        "No Starch Press": [
            "Practical SQL",
            "Data Visualization with Python",
            "Math Adventures with Python",
            "The Art of Statistics with Python",
            "Real-World Data Wrangling"
        ],

        "Apress": [
            "Beginning Data Science",
            "Practical Data Science",
            "Data Science Fundamentals",
            "Applied Data Analytics",
            "Modern Data Science"
        ],

        "Manning Publications": [
            "Data Science Bookcamp",
            "Data Analytics with Python",
            "Grokking Data Analysis",
            "Machine Learning in Action",
            "Data Science at the Command Line"
        ]
    },

    "Machine Learning": {
        "O'Reilly Media": [
            "Hands-On Machine Learning",
            "Machine Learning Pocket Reference",
            "Applied Machine Learning",
            "Machine Learning Design Patterns",
            "Reliable Machine Learning"
        ],

        "Packt Publishing": [
            "Machine Learning with Python",
            "Advanced Machine Learning",
            "Deep Learning with Python",
            "Scikit-Learn Cookbook",
            "Machine Learning Engineering"
        ],

        "No Starch Press": [
            "The Art of Machine Learning",
            "Practical Deep Learning",
            "Neural Networks from Scratch",
            "Machine Learning Projects",
            "Building AI Applications"
        ],

        "Apress": [
            "Beginning Machine Learning",
            "Practical Machine Learning",
            "Machine Learning for Developers",
            "Applied Artificial Intelligence",
            "Modern Machine Learning"
        ],

        "Manning Publications": [
            "Grokking Machine Learning",
            "Machine Learning in Action",
            "Deep Learning with Python",
            "Machine Learning with TensorFlow",
            "Machine Learning Systems"
        ]
    },

    "Artificial Intelligence": {
        "O'Reilly Media": [
            "AI Engineering",
            "Generative AI on AWS",
            "Practical Artificial Intelligence",
            "AI for Developers",
            "Responsible AI"
        ],

        "Packt Publishing": [
            "Artificial Intelligence with Python",
            "Generative AI with Python",
            "AI Projects",
            "Applied AI",
            "Modern Artificial Intelligence"
        ],

        "No Starch Press": [
            "The AI Revolution",
            "Practical AI Projects",
            "Artificial Intelligence Basics",
            "Python AI",
            "Building Intelligent Systems"
        ],

        "Apress": [
            "Beginning AI",
            "AI for Everyone",
            "Practical Artificial Intelligence",
            "Artificial Intelligence Essentials",
            "Intelligent Systems Development"
        ],

        "Manning Publications": [
            "AI in Action",
            "Grokking Artificial Intelligence",
            "Deep Learning in Action",
            "Generative AI in Action",
            "AI-Powered Applications"
        ]
    },

    "Web Development": {
        "O'Reilly Media": [
            "Learning HTML & CSS",
            "JavaScript: The Definitive Guide",
            "High Performance Browser Networking",
            "Designing Web APIs",
            "Programming JavaScript Applications"
        ],

        "Packt Publishing": [
            "Mastering React",
            "ASP.NET Core Cookbook",
            "Full Stack Web Development",
            "Angular Projects",
            "Modern JavaScript"
        ],

        "No Starch Press": [
            "The Linux Command Line",
            "Web Security for Developers",
            "JavaScript for Beginners",
            "The Missing README",
            "Web Development Projects"
        ],

        "Apress": [
            "Pro ASP.NET Core",
            "Beginning ASP.NET Core",
            "Modern Web Development",
            "JavaScript Recipes",
            "Web API Development"
        ],

        "Manning Publications": [
            "React in Action",
            "ASP.NET Core in Action",
            "Fullstack Vue",
            "Web Development with Blazor",
            "Frontend Development Projects"
        ]
    }},
  "Furniture": {
    "Sofa": {
        "IKEA": [
            "KIVIK",
            "LANDSKRONA",
            "VIMLE",
            "SÖDERHAMN",
            "UPPLAND"
        ],

        "Ashley Furniture": [
            "Altari",
            "Bovarian",
            "Abinger",
            "Darcy",
            "Next-Gen DuraPella"
        ],

        "La-Z-Boy": [
            "Meyer",
            "Collins",
            "Kennedy",
            "Pinnacle",
            "Trouper"
        ],

        "Wayfair": [
            "Andover Mills Harper",
            "Mercury Row Garren",
            "Three Posts Hattie",
            "Wade Logan Avery",
            "Lark Manor Briar"
        ],

        "West Elm": [
            "Harmony",
            "Andes",
            "Haven",
            "Axel",
            "Zander"
        ]
    },

    "Bed": {
        "IKEA": [
            "MALM",
            "HEMNES",
            "BRIMNES",
            "SLATTUM",
            "SONGESAND"
        ],

        "Ashley Furniture": [
            "Drystan",
            "Bostwick Shoals",
            "Brinxton",
            "Charmond",
            "Willenburg"
        ],

        "La-Z-Boy": [
            "Harbor Bed",
            "Summit Bed",
            "Willow Bed",
            "Retreat Bed",
            "Heritage Bed"
        ],

        "Wayfair": [
            "Andover Mills Platform",
            "Mercury Row Upholstered",
            "Three Posts Storage",
            "Wade Logan Modern",
            "Lark Manor Classic"
        ],

        "West Elm": [
            "Mid-Century Bed",
            "Simple Bed",
            "Quinn Bed",
            "Emmett Bed",
            "Andes Bed"
        ]
    },

    "Dining Table": {
        "IKEA": [
            "INGATORP",
            "MÖRBYLÅNGA",
            "LISABO",
            "NORDVIKEN",
            "EKEDALEN"
        ],

        "Ashley Furniture": [
            "Skempton",
            "Bolanburg",
            "Havalance",
            "Ralene",
            "Caitbrook"
        ],

        "La-Z-Boy": [
            "Aspen Dining",
            "Oakridge",
            "Heritage Table",
            "Modern Farmhouse",
            "Summit Dining"
        ],

        "Wayfair": [
            "Mercury Row Dining",
            "Andover Mills Farmhouse",
            "Three Posts Extendable",
            "Wade Logan Glass",
            "Lark Manor Oak"
        ],

        "West Elm": [
            "Anton Dining",
            "Emmerson",
            "Box Frame",
            "Mid-Century Expandable",
            "Industrial Dining"
        ]
    },

    "Chair": {
        "IKEA": [
            "POÄNG",
            "BERGMUND",
            "ODGER",
            "TEODORES",
            "NORDMYRA"
        ],

        "Ashley Furniture": [
            "Centiar",
            "Moriville",
            "Skempton Chair",
            "Whitesburg",
            "Realyn"
        ],

        "La-Z-Boy": [
            "Pinnacle Recliner",
            "Astor Recliner",
            "Greyson Recliner",
            "James Recliner",
            "Rowan Chair"
        ],

        "Wayfair": [
            "Mercury Row Accent",
            "Andover Mills Dining",
            "Three Posts Windsor",
            "Lark Manor Armchair",
            "Wade Logan Office"
        ],

        "West Elm": [
            "Slope Chair",
            "Finn Chair",
            "Cooper Chair",
            "Mid-Century Chair",
            "Haven Lounge"
        ]
    },

    "Wardrobe": {
        "IKEA": [
            "PAX",
            "BRIMNES",
            "KLEPPSTAD",
            "PLATSA",
            "SONGESAND"
        ],

        "Ashley Furniture": [
            "Willenburg Wardrobe",
            "Drystan Chest",
            "Bostwick Armoire",
            "Brinxton Wardrobe",
            "Charmond Armoire"
        ],

        "La-Z-Boy": [
            "Classic Wardrobe",
            "Summit Armoire",
            "Heritage Closet",
            "Modern Storage",
            "Premium Wardrobe"
        ],

        "Wayfair": [
            "Andover Mills Armoire",
            "Mercury Row Wardrobe",
            "Three Posts Closet",
            "Lark Manor Storage",
            "Wade Logan Modern"
        ],

        "West Elm": [
            "Mid-Century Wardrobe",
            "Anton Armoire",
            "Simple Wardrobe",
            "Industrial Storage",
            "Modern Closet"
        ]
    }
}                 
}

#Cost price ranges for each product category
COST_PRICE_RANGES = {
    "Electronics": {"Laptop": (50000, 200000), "Smartphone": (2000, 15000), "Tablet": (1000, 10000), "Headphones": (2000, 10000), "Smartwatch": (1000, 5000), "Camera": (10000, 100000), "Television": (15000, 100000), "Monitor": (5000, 50000), "Printer": (3000, 20000), "Router": (1000, 10000)},
    "Home Appliances": {"Refrigerator": (15000, 45000), "Washing Machine": (20000, 120000), "Microwave": (1500, 10000), "Air Conditioner": (20000, 100000), "Vacuum Cleaner": (3000, 20000), "Dishwasher": (2000, 15000), "Coffee Maker": (2500, 25000)},
    "Fashion": {"T-Shirt": (500, 1000), "Jeans": (700, 1500), "Dress": (250, 2500), "Sneakers": (400, 3000), "Jacket": (500, 3000), "Handbag": (300, 3000)},
    "Books": {"Python Programming": (200, 500), "Data Science": (200, 1000), "Machine Learning": (500, 1500), "Artificial Intelligence": (500, 1500), "Web Development": (200, 1000)},
    "Furniture": {"Sofa": (3000, 20000), "Bed": (2000, 15000), "Dining Table": (1500, 12000), "Chair": (500, 5000), "Wardrobe": (500, 5000)}
}

# Profit margin ranges for each product category
UNIT_PRICE_RANGES = {
    "Electronics": {"Laptop": (0.1, 0.3), "Smartphone": (0.1, 0.4), "Tablet": (0.1, 0.3), "Headphones": (0.1, 0.4), "Smartwatch": (0.1, 0.3), "Camera": (0.1, 0.3), "Television": (0.1, 0.5), "Monitor": (0.1, 0.3), "Printer": (0.1, 0.3), "Router": (0.1, 0.3)},
    "Home Appliances": {"Refrigerator": (0.1, 0.5), "Washing Machine": (0.1, 0.5), "Microwave": (0.1, 0.3), "Air Conditioner": (0.1, 0.4), "Vacuum Cleaner": (0.1, 0.3), "Dishwasher": (0.1, 0.3), "Coffee Maker": (0.1, 0.3)},
    "Fashion": {"T-Shirt": (0.1, 0.3), "Jeans": (0.1, 0.4), "Dress": (0.1, 0.3), "Sneakers": (0.1, 0.5), "Jacket": (0.1, 0.3), "Handbag": (0.1, 0.3)},
    "Books": {"Python Programming": ( 0.1, 0.3), "Data Science": (0.1, 0.3), "Machine Learning": (0.1, 0.3), "Artificial Intelligence": (0.1, 0.3), "Web Development": (0.1, 0.3)},
    "Furniture": {"Sofa": (0.1, 0.5), "Bed": (0.1, 0.4), "Dining Table": (0.1, 0.3), "Chair": (0.1, 0.5), "Wardrobe": (0.1, 0.3)} }

#Stock quantity ranges for each product category
STOCK_QUANTITY_RANGES = {
    "Electronics": {"Laptop": (10, 100), "Smartphone": (20, 200), "Tablet": (15, 150), "Headphones": (50, 500), "Smartwatch": (25, 250), "Camera": (10, 100), "Television": (5, 50), "Monitor": (20, 200), "Printer": (15, 150), "Router": (30, 300)},
    "Home Appliances": {"Refrigerator": (5, 50), "Washing Machine": (3, 30), "Microwave": (10, 100), "Air Conditioner": (5, 50), "Vacuum Cleaner": (20, 200), "Dishwasher": (10, 100), "Coffee Maker": (25, 250)},
    "Fashion": {"T-Shirt": (100, 1000), "Jeans": (50, 500), "Dress": (30, 300), "Sneakers": (25, 250), "Jacket": (20, 200), "Handbag": (50, 500)},
    "Books": {"Python Programming": (100, 1000), "Data Science": (100, 1000), "Machine Learning": (100, 1000), "Artificial Intelligence": (100, 1000), "Web Development": (100, 1000)},
    "Furniture": {"Sofa": (5, 50), "Bed": (10, 100), "Dining Table": (5, 50), "Chair": (25, 250), "Wardrobe": (15, 150)}
}

# Functions to generate a random product

# Function to get a random category
def get_random_category():
    return random.choice(list(PRODUCT_CATEGORIES.keys()))

# Function to get a random product type within a category
def get_random_product_type(category):
    return random.choice(list(PRODUCT_CATEGORIES[category].keys()))

# Function to get a random brand within a product type
def get_random_brand(category, product_type):
    return random.choice(list(PRODUCT_CATEGORIES[category][product_type].keys()))

# Function to get a random product name within a brand
def get_random_product_name(category, product_type, brand):
    return random.choice(PRODUCT_CATEGORIES[category][product_type][brand])

# Function to get a random cost price within the specified range for a product type
def get_random_cost_price(category, product_type):
    min_price, max_price = COST_PRICE_RANGES[category][product_type]
    return round(random.uniform(min_price, max_price), 2)

# Function to get a random unit price within the specified range for a product type
def get_random_unit_price(category, product_type, cost_price):
    min_price, max_price = UNIT_PRICE_RANGES[category][product_type]
    margin= round(random.uniform(min_price, max_price), 2)
    unit_price = cost_price * (1 + margin)
    return round(unit_price, 2)
   
# Function to get a random stock quantity within the specified range for a product type
def get_random_stock_quantity(category, product_type):
    min_qty, max_qty = STOCK_QUANTITY_RANGES[category][product_type]
    return random.randint(min_qty, max_qty)

# Main function to generate a random product
def generate_random_product():
    category = get_random_category()
    product_type = get_random_product_type(category)
    brand = get_random_brand(category, product_type)
    product_name = get_random_product_name(category, product_type, brand)
    cost_price = get_random_cost_price(category, product_type)
    unit_price = get_random_unit_price(category, product_type, cost_price)
    stock_quantity = get_random_stock_quantity(category, product_type)

    return {
        "Category": category,
        "ProductType": product_type,
        "Brand": brand,
        "ProductName": product_name,
        "CostPrice": cost_price,
        "UnitPrice": unit_price,
        "Stock": stock_quantity
    }

# Function to generate a list of products
def generate_products(num_products):
    products = []
    for _ in range(num_products):
        product = generate_random_product()
        products.append(product)
    return products

# Example usage
if __name__ == "__main__":
    num_products_to_generate = 500 
    generated_products = generate_products(num_products_to_generate)
    insert_product_data(generated_products) 