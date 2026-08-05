t = [
    ("Falcon", 34.05, -118.24),
    ("Ghost", 99.9, 12.0),
    ("Condor", 40.71, -74.00)
]

valid = []

# Check validity
for codename, lat, lon in t:
    if lat < -90 or lat > 90 or lon < -180 or lon > 180:
        print(f"INVALID: {codename} ({lat}, {lon})")
    else:
        valid.append((codename, lat, lon))

# Sort by latitude (North -> South)
valid.sort(key=lambda x: x[1], reverse=True)

print("Briefing (N->S):")
for codename, lat, lon in valid:
    print(f"    {codename} -> Lat: {lat:.2f}, Lon: {lon:.2f}")