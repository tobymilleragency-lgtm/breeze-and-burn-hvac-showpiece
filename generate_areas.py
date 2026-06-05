import os

areas_data = [
    {
        "filename": "webb-city-mo.html",
        "city_name": "Webb City, MO",
        "badge_text": "NORTH ZONE DISPATCH DISPENSARY",
        "distance": "6 Miles (North)",
        "latency": "Demo Area",
        "active_crews": "Sample Zone",
        "humidity": "78% RH",
        "meta_desc": "Premium HVAC diagnostics and thermal repairs in Webb City, MO by Breeze & Burn. Demo service-area page for HVAC diagnostics and thermal repair content structure.",
        "description": "Webb City sits directly north of our Joplin hub. Our diagnostic technicians cycle through this residential corridor daily, ensuring rapid scheduling options for temperature split tests and blower duct calibrations."
    },
    {
        "filename": "carl-junction-mo.html",
        "city_name": "Carl Junction, MO",
        "badge_text": "NORTHWEST REGION LOGISTICS",
        "distance": "8 Miles (Northwest)",
        "latency": "< 50 Mins",
        "active_crews": "Sample Zone",
        "humidity": "77% RH",
        "meta_desc": "Expert HVAC diagnostics and air conditioning services in Carl Junction, MO by Breeze & Burn. Balanced R-value calculations.",
        "description": "Carl Junction residents face rapid thermal changes due to local exposure curves. We specialize in structural load balancing, attic insulation auditing, and variable-speed fan calibration in this municipal zone."
    },
    {
        "filename": "carthage-mo.html",
        "city_name": "Carthage, MO",
        "badge_text": "EASTERN SECTOR FIELD UNITS",
        "distance": "15 Miles (Northeast)",
        "latency": "Demo Area",
        "active_crews": "Sample Zone",
        "humidity": "79% RH",
        "meta_desc": "High-efficiency furnace calibrations and AC diagnostics in Carthage, MO by Breeze & Burn. Static flow balancing tests.",
        "description": "Servicing historic Carthage homes requires custom engineering. We check old cast-iron layouts, balance trunk line splits, and run combustion carbon monoxide tests on local furnace installations."
    },
    {
        "filename": "neosho-mo.html",
        "city_name": "Neosho, MO",
        "badge_text": "SOUTHERN SERVICE ROUTE",
        "distance": "20 Miles (South)",
        "latency": "Demo Area",
        "active_crews": "Sample Zone",
        "humidity": "80% RH",
        "meta_desc": "Attic load calibrations and duct seal integrity testing in Neosho, MO by Breeze & Burn. Evaporator flow analysis.",
        "description": "Neosho serves as our southern service boundary. Our crews routinely perform thermal duct-leakage scans, humidifier integrations, and compressor capacitor diagnostics along this corridor."
    },
    {
        "filename": "galena-ks.html",
        "city_name": "Galena, KS",
        "badge_text": "CROSS-BORDER KANSAS DIVISION",
        "distance": "7 Miles (West)",
        "latency": "Demo Area",
        "active_crews": "Sample Zone",
        "humidity": "78% RH",
        "meta_desc": "HVAC diagnostic and static duct service-area page for Galena, KS by Breeze & Burn. Demo concept copy.",
        "description": "Galena is located just west of the Missouri-Kansas line. This demo page models Kansas-side HVAC diagnostic service copy without claiming verified licensing or active dispatch."
    },
    {
        "filename": "baxter-springs-ks.html",
        "city_name": "Baxter Springs, KS",
        "badge_text": "SOUTHWEST SECTOR RADAR GRID",
        "distance": "15 Miles (Southwest)",
        "latency": "Demo Area",
        "active_crews": "Sample Zone",
        "humidity": "79% RH",
        "meta_desc": "Whole-house airflow tuning and AC charging diagnostics in Baxter Springs, KS by Breeze & Burn. Demo concept copy.",
        "description": "Baxter Springs sits on historic Route 66. We deliver professional diagnostic scans, motor lubrication, heat exchanger flue gas evaluations, and whole-house fan balancing to local homeowners."
    }
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{meta_desc}" />
  <title>HVAC Diagnostics & AC Service in {city_name} — Breeze & Burn</title>
  <link rel="stylesheet" href="../styles.css" />
</head>
<body>

  <!-- NAVIGATION RAIL -->
  <header class="nav-container">
    <nav class="navbar" aria-label="Main Navigation">
      <a href="../index.html" class="nav-brand">
        <div class="brand-icon"></div>
        <span>Breeze & Burn</span>
      </a>
      <div class="nav-menu">
        <a href="../index.html#diagnostics" class="nav-link">Diagnostics</a>
        <a href="../index.html#simulator" class="nav-link">Simulator</a>
        <a href="../index.html#services" class="nav-link">Services</a>
        <a href="../index.html#areas" class="nav-link active">Coverage</a>
        <a href="../index.html#book" class="nav-link">Book Scan</a>
      </div>
      <div class="nav-right">
        <div class="nav-status">
          <div class="status-dot"></div>
          <span>LOCALIZED AREA DISPATCH</span>
        </div>
        <a href="../index.html#book" class="btn btn-primary" style="min-height: 38px; padding: 6px 16px; font-size: 11px; font-family: var(--font-mono); text-transform: uppercase;">Run Scan</a>
      </div>
    </nav>
  </header>

  <main>
    
    <!-- PAGE HERO -->
    <header class="page-header-hero" style="background: linear-gradient(180deg, var(--color-bg-alt), var(--color-bg));">
      <div class="page-header-inner">
        <div class="badge-outline">
          <span class="status-dot" style="background: var(--color-green); box-shadow: 0 0 8px var(--color-green);"></span>
          <span>{badge_text}</span>
        </div>
        <h1 class="page-header-title">HVAC Diagnostics in {city_name}</h1>
        <p class="page-header-desc">{description}</p>
      </div>
    </header>

    <!-- METRICS DISPLAY GRID -->
    <section class="section">
      <div class="section-inner">
        <div class="simulator-panel" style="grid-template-columns: 1fr 1fr; padding: 40px; background: var(--color-bg-alt);">
          
          <div style="display: flex; flex-direction: column; justify-content: center; gap: 16px;">
            <h2 class="portal-title" style="color: var(--color-cold); font-size: var(--text-md); border-bottom: 1px solid var(--color-border); padding-bottom: 12px;">{city_name} Regional Load Profiles</h2>
            <p style="color: var(--color-muted); font-size: var(--text-sm); line-height: 1.5;">Localized summer temperatures average 91°F with {humidity} humidity loads. This extreme thermal strain drops suction pressures and causes evaporator frosting. We scan coils directly to restore performance coefficients.</p>
          </div>

          <div class="sim-results" style="background: oklch(100% 0 0 / 0.015); border: 1px solid var(--color-border); gap: 14px;">
            <h3 class="results-header" style="border-bottom: 0; padding-bottom: 0;">Operational Sensor Data</h3>
            
            <div class="portal-stats-grid" style="grid-template-columns: 1fr 1fr; gap: 12px;">
              <div class="stat-box">
                <span class="stat-lbl">Hub Distance</span>
                <span class="stat-val">{distance}</span>
              </div>
              <div class="stat-box">
                <span class="stat-lbl">Average Latency</span>
                <span class="stat-val" style="color: var(--color-green);">{latency}</span>
              </div>
              <div class="stat-box">
                <span class="stat-lbl">Demo Coverage Model</span>
                <span class="stat-val">{active_crews}</span>
              </div>
              <div class="stat-box">
                <span class="stat-lbl">Typical Load Split</span>
                <span class="stat-val">17.2°F Delta-T</span>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>

    <!-- CONTENT CARDS -->
    <section class="section" style="background: var(--color-bg-alt);">
      <div class="section-inner">
        <div class="services-grid">
          
          <div class="service-card" style="padding: 24px;">
            <span class="service-icon">Cooling Calibrations</span>
            <h3 class="service-card-title">{city_name} A/C Service</h3>
            <p class="service-card-desc">Condenser cleaning, electrical capacitor tests, refrigerant leak checks, and evaporator split-temperatures calculations.</p>
          </div>

          <div class="service-card" style="padding: 24px;">
            <span class="service-icon">Heating Diagnostics</span>
            <h3 class="service-card-title">{city_name} Furnace Tuning</h3>
            <p class="service-card-desc">CO safety inspections, combustion fuel-to-air calibrations, burner assembly sweeps, and safety limit checks.</p>
          </div>

          <div class="service-card" style="padding: 24px;">
            <span class="service-icon">Air Purification</span>
            <h3 class="service-card-title">{city_name} IAQ Swapping</h3>
            <p class="service-card-desc">MERV 13 filter installations, whole-house moisture balancing, UV-C sterilizer mapping, and dust dander audits.</p>
          </div>

        </div>
      </div>
    </section>

    <!-- BOOK SCAN LINK -->
    <section class="section">
      <div class="section-inner" style="text-align: center;">
        <h2 class="portal-title" style="font-size: var(--text-xl); margin-bottom: 16px;">Schedule your {city_name} diagnostics scan</h2>
        <p style="color: var(--color-muted); max-width: 600px; margin: 0 auto 32px; font-size: var(--text-sm);">Our engineering crews measure R-values, airflow drops, and static pressure splits. Optimize your home heating and cooling system today.</p>
        <a href="../index.html#book" class="btn btn-primary">Book {city_name} Service Scan</a>
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer-inner">
      <div class="footer-bottom">
        <span class="footer-copy">© 2026 Breeze & Burn Systems. Technical contractor design concept.</span>
        <div class="footer-legal">
          <a href="../index.html">Back to Homepage</a>
        </div>
      </div>
    </div>
  </footer>

</body>
</html>
"""

output_dir = "/home/toby/hvac-joplin-masterpiece/areas"
os.makedirs(output_dir, exist_ok=True)

for area in areas_data:
    content = html_template.format(
        meta_desc=area["meta_desc"],
        city_name=area["city_name"],
        badge_text=area["badge_text"],
        description=area["description"],
        humidity=area["humidity"],
        distance=area["distance"],
        latency=area["latency"],
        active_crews=area["active_crews"]
    )
    
    file_path = os.path.join(output_dir, area["filename"])
    with open(file_path, "w") as f:
        f.write(content)
    print(f"Generated: {file_path}")
